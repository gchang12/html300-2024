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

def _remove_citation_numbers(line):
    """
    """
    return re.sub(r"\[.+?\]", "", line)

# FIM
## episodes (X)
# - https://mlp.fandom.com/wiki/Friendship_is_Magic_animated_media#Episodes

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
        #"series",
        #"type",
    )
    index2 = list(filter(lambda episode: set(episode.keys()) == set(desired_fields), index))
    # strip newline characters
    for index_no, episode in enumerate(index2):
        #episode['series'] = "FiM"
        #episode['type'] = "episode"
        episode["id"] = index_no
        episode["title"] = episode["title"].strip()
        episode["urlName"] = episode["urlName"].strip()
        episode["airdate"] = episode["airdate"].strip()
        episode["summary"] = list(map(lambda line: _remove_citation_numbers(line).strip(), episode["summary"]))
        episode["episodeNo"] = int(episode["episodeNo"].lstrip("0"))
        # validate airdate
        try:
            date.fromisoformat(episode['airdate'])
        except ValueError as e:
            logging.error("%s has a bad 'airdate' value of '%s'", episode, episode['airdate'])
            raise e
    return sorted(index2, key=lambda episode: "S%d-E%02d" % (episode["seasonNo"], episode["episodeNo"]))

## clip show
# - https://mlp.fandom.com/wiki/Friendship_is_Magic_animated_media#Clip_shows

def regenerate_clipshow_index():
    """
    """
    #episode['series'] = "FiM"
    #episode['seasonNo'] = "FiF"
    #episode['type'] = "episode"

## films
# - https://mlp.fandom.com/wiki/Friendship_is_Magic_animated_media#Films

def regenerate_film_index():
    """
    """
    #episode['series'] = "FiM"
    #episode['seasonNo'] = "The Movie"
    #episode['type'] = "film"

## specials
# - https://mlp.fandom.com/wiki/Friendship_is_Magic_animated_media#Specials

def regenerate_specials_index():
    """
    """
    #episode['series'] = "FiM"
    #episode['seasonNo'] = "Best Gift Ever"
    #episode['seasonNo'] = "Rainbow Roadtrip"
    #episode['type'] = "special"

## shorts
# - https://mlp.fandom.com/wiki/Friendship_is_Magic_animated_media#Animated_shorts

def regenerate_shorts_index():
    """
    """
    #episode['series'] = "FiM"
    #episode['seasonNo'] = "Best Gift Ever"
    #episode['seasonNo'] = None
    #episode['type'] = "short"

# EQG
## films
# - https://mlp.fandom.com/wiki/Equestria_Girls_animated_media#Films

def regenerate_eqg_films_index():
    """
    """
    #episode['series'] = "EqG"
    #episode['seasonNo'] = "Equestria Girls"
    #episode['seasonNo'] = "Rainbow Rocks"
    #episode['seasonNo'] = "Friendship Games"
    #episode['seasonNo'] = "Legend of Everfree"
    #episode['episodeNo'] = 1
    #episode['type'] = "film"

## specials
# - https://mlp.fandom.com/wiki/Equestria_Girls_animated_media#Specials

def regenerate_eqg_specials_index():
    """
    """
    #episode['series'] = "EqG"
    #episode['seasonNo'] = "Movie Magic"
    #...
    #episode['episodeNo'] = 1
    #episode['type'] = "special"

## shorts
# - https://mlp.fandom.com/wiki/Equestria_Girls_animated_media#Animated_shorts
## digital series
# - https://mlp.fandom.com/wiki/Equestria_Girls_animated_media#Digital_Series

def regenerate_eqg_shorts_index():
    """
    """
    #episode['series'] = "EqG"
    #episode['seasonNo'] = "Rainbow Rocks"
    #episode['seasonNo'] = "Friendship Games"
    #episode['type'] = "short"
    #...
    #episode['episodeNo'] = 1

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
    index_no = 0
    for episode in episode_index:
        transcriptline = {
            "episodeId": episode['id'],
            "seasonNo": episode["seasonNo"],
            "episodeNo": episode["episodeNo"],
        }
        with open(Path("output", "FiM", "transcripts", "S%d" % episode['seasonNo'], "E%02d.json" % episode['episodeNo'])) as rfile:
            lines = json.load(rfile)
        #print(lines)
        # consolidate lyrical lines
        lines2 = []
        for indexno, line in enumerate(lines, start=1):
            speaker, dialogue = line
            dialogue = dialogue.strip()
            # remove blank lines
            if dialogue == "":
                if speaker is not None:
                    logging.warning("Speaker '%s' has no line at L%d in S%d E%d", speaker, indexno, episode['seasonNo'], episode['episodeNo'])
                continue
            #if speaker is None: continue
            # ignore lines that have both dialogue and no speaker speaking it
            #if (speaker is None) and 
            previous_speaker = (None if not lines2 else lines2[-1][0])
            if (speaker is None) and ("\n" in dialogue):
                speaker = lines2[-1][0]
                # NOTE: Are these two necessary?
                #and (previous_speaker.endswith("]") \
                    #and previous_speaker.startswith("[")) \
            elif (speaker is None) \
                and (previous_speaker is not None) \
                and not (dialogue.endswith("]") and dialogue.startswith("[")):
                speaker = lines2[-1][0]
                # skip lyrics that lack newlines
                #continue
            if (speaker is None):
                continue
            lines2.append((speaker, dialogue))
        for (line_no, line) in enumerate(lines2, start=1):
            #if len(line) > 2: line[1] = " ".join(line[1:]) line = [line[0], line[1]]
            #if len(line) == 1: print(line)
            #print(line_no)
            speaker, dialogue = line
            transcriptline.update(
                {
                    "id": index_no,
                    "lineNo": line_no,
                    "speaker": (None if speaker is None else speaker.strip()),
                    "dialogue": dialogue.strip().replace("\n", "~ "),
                }
            )
            transcriptline_index.append(transcriptline.copy())
            index_no += 1
    return transcriptline_index


def generate_transcriptline_index2(episode_index):
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
    # read index
    # iterate over all entries and extract all transcript lines
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
        "summary",
    ))
    unicorn_index2 = list(
        filter(
            lambda unicorn: unicorn["episodes"] != {},
            filter(
                lambda unicorn: set(unicorn.keys()) == desired_fields,
                unicorn_index,
            )
        )
    )
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
        unicorn["summary"] = list(map(lambda line: _remove_citation_numbers(line).strip(), unicorn["summary"]))
    unicorn_index3 = []
    index_no = 0
    for unicorn in unicorn_index2:
        if unicorn['name'] in ("Discord", "Big McIntosh"):
            continue
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

    def save_regenerated_animation_index():
        """
        """
        index = []
        # MLP:FIM S1-S9
        index.extend(regenerate_episode_index())
        # MLP:FIM S10 (FIF)
        index.extend(regenerate_clipshow_index())
        # MLP:Movie
        index.extend(regenerate_film_index())
        # MLP:BGE, MLP:RR
        index.extend(regenerate_specials_index())
        # MLP:BGE-Shorts, miscellany
        index.extend(regenerate_shorts_index())
        # MLP:EQG-{,RR,TFG,LoE}
        index.extend(regenerate_eqg_films_index())
        # MLP:EQG-{SB,MM,MM,...}
        index.extend(regenerate_eqg_specials_index())
        # MLP:EQG-{...}
        index.extend(regenerate_eqg_shorts_index())
        # sort by airdate
        # group like items somehow

    def save_transcriptline_index2():
        """
        """
        # get episode index
        # iterate over it, getting the appropriate filenames as appropriate.

    #save_regenerated_animation_index()
    #save_transcriptline_index2()
