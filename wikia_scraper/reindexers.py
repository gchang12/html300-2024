"""
Reformats indexes for succinctness.
Also transforms raw transcript data into the following format.
{
  episodeId: number,
  lineNo: number,
  speaker: string,
  lineText: string,
}
"""

import re
from datetime import date
import json
from pathlib import Path
import logging

# reformat episode index
# regenerate episode index with id's

def regenerate_episode_index():
    """
    """
    filename = "output/FiM/indexes/episodes.json"
    with open(filename) as rfile:
        index = json.load(rfile)
    # take out entries that lack desired fields.
    desired_fields = (
        "seasonNo",
        "episodeNo",
        "title",
        "urlName",
        "summary",
        "airdate",
    )
    index2 = list(filter(lambda episode: set(episode.keys()) == set(desired_fields), index))
    # strip newline characters
    for index_no, episode in enumerate(index2):
        episode["id"] = index_no
        episode["title"] = episode["title"].strip()
        episode["urlName"] = episode["urlName"].strip()
        episode["airdate"] = episode["airdate"].strip()
        episode["summary"] = list(map(lambda line: re.sub(r"\[\d+\]", "", line).strip(), episode["summary"]))
        episode["episodeNo"] = int(episode["episodeNo"].lstrip("0"))
        # validate airdate
        try:
            date.fromisoformat(episode['airdate'])
        except ValueError as e:
            logging.error("%s has a bad 'airdate' value of '%s'", episode, episode['airdate'])
            raise e
    return sorted(index2, key=lambda episode: "S%d-E%02d" % (episode["seasonNo"], episode["episodeNo"]))

# generate transcript line index

def generate_transcriptline_index(episode_index):
    """
    Creates index of the form:
    {
        episodeId: number,
        lineNo: number,
        speaker: string,
        lineText: string,
    }
    """
    transcriptline_index = []
    for episode in episode_index:
        transcriptline = {"episodeId": episode['id']}
        with open(Path("output", "FiM", "transcripts", "S%d" % episode['seasonNo'], "E%02d.json" % episode['episodeNo'])) as rfile:
            lines = json.load(rfile)
        #print(lines)
        # consolidate lyrical lines
        lines2 = []
        for line in lines:
            speaker, dialogue = line
            dialogue = dialogue.strip()
            # remove blank lines
            if not dialogue:
                continue
            # ignore lines that have both dialogue and no speaker speaking it
            #if (speaker is None) and 
            previous_speaker = (None if not lines2 else lines2[-1][0])
            if (speaker is None) and ("\n" in dialogue):
                speaker = lines2[-1][0]
            elif (speaker is None) \
                and (previous_speaker is not None) \
                and (previous_speaker.endswith("]") \
                    and previous_speaker.startswith("[")) \
                and not (dialogue.endswith("]") and dialogue.startswith("[")):
                # skip lyrics that lack newlines
                continue
            lines2.append((speaker, dialogue))
        for (line_no, line) in enumerate(lines2, start=1):
            #if len(line) > 2: line[1] = " ".join(line[1:]) line = [line[0], line[1]]
            #if len(line) == 1: print(line)
            #print(line_no)
            speaker, dialogue = line
            transcriptline.update(
                {
                    "lineNo": line_no,
                    "speaker": (None if speaker is None else speaker.strip()),
                    "dialogue": dialogue.strip().replace("\n", "~ "),
                }
            )
            transcriptline_index.append(transcriptline.copy())
    return transcriptline_index

def get_episode_id(seasonepisode_no, episode_index):
    """
    """
    season_no, episode_no = seasonepisode_no.split("-")
    season_no = int(season_no.lstrip("S"))
    episode_no = int(episode_no.lstrip("E0"))
    episode_id = list(filter(lambda episode: episode['seasonNo'] == season_no and episode['episodeNo'] == episode_no, episode_index)).pop()['id']
    return episode_id

def regenerate_unicorn_index(episode_index):
    """
    """
    character_index = []
    unicornindex_filename = "output/FiM/indexes/unicorns.json"
    with open(unicornindex_filename) as rfile:
        unicorn_index = json.load(rfile)
    desired_fields = set((
        "species",
        "name",
        "gender",
        "urlName",
        "episodes",
    ))
    unicorn_index2 = list(filter(lambda episode: set(episode.keys()) == desired_fields, unicorn_index))
    for unicorn in unicorn_index2:
        episodes = unicorn['episodes'].copy()
        unicorn['gender'] = {
            "mare": "F",
            "filly": "F",
            "stallion": "M",
            "colt": "M",
        }[unicorn["gender"].strip()]
        def convert_appearance_code(appearance_code):
            """
            """
            return list(
                map(
                    lambda seasonepisode_no: get_episode_id(seasonepisode_no, episode_index),
                    map(
                        lambda episode_key: episode_key[0],
                        filter(
                            lambda episode_key: episode_key[1].strip() == appearance_code,
                            episodes.items(),
                        )
                    )
                )
            )
        unicorn['episodes'] = {
            "speaking": convert_appearance_code("Y"), # Y
            "silent": convert_appearance_code("S"), # S
            "background": convert_appearance_code("B"), # B
            "imagined": convert_appearance_code("F"), # F
            "inMedia": convert_appearance_code("P"), # P
            "mentioned": convert_appearance_code("M"), # M
        }
    unicorn_index3 = []
    index_no = 0
    for unicorn in unicorn_index2:
        if unicorn['name'] in ("Discord", "Big McIntosh"):
            continue
        total = 0
        for episodes in unicorn['episodes'].values():
            total += len(episodes)
        if total > 0:
            unicorn['id'] = index_no
            unicorn_index3.append(unicorn)
            index_no += 1
    return unicorn_index3

if __name__ == "__main__":
    def save_regenerated_episode_index():
        """
        """
        index = regenerate_episode_index()
        filename = "output/FiM/websiteIndexes/episodes.json"
        with open(filename, mode="w") as wfile:
            json.dump(index, wfile, indent=2)
    #save_regenerated_episode_index()
    def save_transcriptline_index():
        """
        """
        filename = "output/FiM/websiteIndexes/episodes.json"
        with open(filename) as rfile:
            episode_index = json.load(rfile)
        transcriptline_index = generate_transcriptline_index(episode_index)
        transcriptindex_filename = "output/FiM/websiteIndexes/transcriptLines.json"
        with open(transcriptindex_filename, mode="w") as wfile:
            json.dump(transcriptline_index, wfile, indent=2)
    #save_transcriptline_index()
    def save_unicorn_index():
        """
        """
        filename = "output/FiM/websiteIndexes/episodes.json"
        with open(filename) as rfile:
            episode_index = json.load(rfile)
        unicorn_index = regenerate_unicorn_index(episode_index)
        unicornindex_filename = "output/FiM/websiteIndexes/unicorns.json"
        with open(unicornindex_filename, mode="w") as wfile:
            json.dump(unicorn_index, wfile, indent=2)
    save_unicorn_index()
