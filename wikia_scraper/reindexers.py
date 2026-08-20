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

import string
import re
from datetime import date
import json
from pathlib import Path
import logging
import urllib.parse

# reformat episode index
# regenerate episode index with id's

def _remove_citation_numbers(line):
    """
    """
    return re.sub(r"\[.+?\]", "", line)

def _validate_date(episode):
    """
    """
    try:
        airdate = episode['airdate']
        date.fromisoformat(airdate)
    except KeyError as e:
        logging.error("No 'airdate' field for %s!", episode['title'])
        raise e
    except ValueError as e:
        logging.error("%s has a bad 'airdate' value of '%s'", episode['title'], episode['airdate'])
        raise e

# FIM
## episodes (X)
# - https://mlp.fandom.com/wiki/Friendship_is_Magic_animated_media#Episodes

def _escape_url_chars(url_name):
    """
    """
    episode["urlName"] = urllib.parse.quote(episode["urlName"].strip(), safe=":()")

def regenerate_index(filename, data_to_append: dict):
    """
    """
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
        #"animationType",
    )
    index2 = list(filter(lambda episode: set(episode.keys()) == set(desired_fields), index))
    # strip newline characters
    for index_no, episode in enumerate(index2):
        episode.update(data_to_append)
        #episode['series'] = "FiM"
        #episode['type'] = "episode"
        #episode["id"] = index_no
        episode["title"] = episode["title"].strip()
        episode["urlName"] = episode["urlName"].strip()
        episode["airdate"] = episode["airdate"].strip()
        episode["summary"] = list(map(lambda line: _remove_citation_numbers(line).strip(), episode["summary"]))
        if isinstance(episode["episodeNo"], str):
            episode["episodeNo"] = int(episode["episodeNo"].lstrip("0"))
            #logging.warning("string for an 'episodeNo' value in %r", episode['title'])
        elif not isinstance(episode['episodeNo'], int):
            logging.warning("%r has a non-integer 'episodeNo' value.", episode['title'])
        if isinstance(episode['seasonNo'], str):
            episode["seasonNo"] = episode["seasonNo"].strip()
        # validate airdate
        _validate_date(episode)
    return index2
    #return sorted(index2, key=lambda episode: "S%d-E%02d" % (episode["seasonNo"], episode["episodeNo"]))

def regenerate_episode_index():
    """
    """
    filename = "output/FiM/indexes/episodes.json"
    data_to_append = {
        "series": "FiM",
        "animationType": "episode",
    }
    index = regenerate_index(filename, data_to_append)
    return index
    #return sorted(index2, key=lambda episode: "S%d-E%02d" % (episode["seasonNo"], episode["episodeNo"]))

## clip show
# - https://mlp.fandom.com/wiki/Friendship_is_Magic_animated_media#Clip_shows

def regenerate_clipshow_index():
    """
    """
    filename = "output/FiM/indexes/FiF.json"
    data_to_append = {
        "series": "FiM",
        #"seasonNo": "FiF",
        "animationType": "clipshow",
    }
    index = regenerate_index(filename, data_to_append)
    return index

## films
# - https://mlp.fandom.com/wiki/Friendship_is_Magic_animated_media#Films

def regenerate_film_index():
    """
    """
    filename = "output/FiM/indexes/Movie.json"
    data_to_append = {
        "series": "FiM",
        #"seasonNo": "FiF",
        "animationType": "film",
    }
    index = regenerate_index(filename, data_to_append)
    return index
    #episode['series'] = "FiM"
    #episode['seasonNo'] = "The Movie"
    #episode['type'] = "film"

## specials
# - https://mlp.fandom.com/wiki/Friendship_is_Magic_animated_media#Specials

def regenerate_specials_index():
    """
    """
    data_to_append = {
        "series": "FiM",
        #"seasonNo": "FiF",
        "animationType": "special",
    }
    index = []
    for filename in ("Best_Gift_Ever.json", "Rainbow_Roadtrip.json"):
        full_path = "output/FiM/indexes/" + filename
        index.extend(regenerate_index(full_path, data_to_append))
    return index

    #episode['series'] = "FiM"
    #episode['seasonNo'] = "Best Gift Ever"
    #episode['seasonNo'] = "Rainbow Roadtrip"
    #episode['type'] = "special"

## shorts
# - https://mlp.fandom.com/wiki/Friendship_is_Magic_animated_media#Animated_shorts

def regenerate_shorts_index():
    """
    """
    filename = "output/FiM/indexes/shorts.json"
    data_to_append = {
        "series": "FiM",
        #"seasonNo": "FiF",
        "animationType": "short",
    }
    index = regenerate_index(filename, data_to_append)
    return index
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
    filename = "output/EqG/indexes/films.json"
    data_to_append = {
        "series": "EqG",
        "animationType": "film",
    }
    index = regenerate_index(filename, data_to_append)
    return index

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
    filename = "output/EqG/indexes/specials.json"
    data_to_append = {
        "series": "EqG",
        "animationType": "special",
    }
    index = regenerate_index(filename, data_to_append)
    return index
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
    filename = "output/EqG/indexes/shorts.json"
    #episode['series'] = "EqG"
    #episode['seasonNo'] = "Rainbow Rocks"
    #episode['seasonNo'] = "Friendship Games"
    #episode['type'] = "short"
    #...
    #episode['episodeNo'] = 1
    # Generate new entries for the shorts that branch out into different endings.
    data_to_append = {
        "series": "EqG",
        "animationType": "short",
    }
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
        #"animationType",
    )
    index2 = list(filter(lambda episode: set(episode.keys()) == set(desired_fields), index))
    # strip newline characters
    new_index = []
    for episode in index2:
        episode.update(data_to_append)
        #episode['series'] = "FiM"
        #episode['type'] = "episode"
        #episode["id"] = index_no
        if isinstance(episode['seasonNo'], str):
            episode["seasonNo"] = episode["seasonNo"].strip()
        episode["title"] = episode["title"].strip()
        episode["urlName"] = episode["urlName"].strip()
        episode["airdate"] = episode["airdate"][:10]#.strip().rstrip('] ' + string.ascii_letters + string.digits).rstrip('[')
        op_lines = []
        for line in episode['summary']:
            if isinstance(line, list):
                startstr = "If the viewer chooses "
                is_branched = True
                for line2 in line:
                    if startstr not in line2:
                        is_branched = False
                        break
                    start = line2.index(startstr)
                    stop = line2.index(",")
                    name = line2[start + len(startstr):stop]
                    new_episode = episode.copy()
                    new_episode['title'] += " - " + name
                    new_episode['summary'] = op_lines + [line2]
                    new_index.append(new_episode)
                if is_branched:
                    episode['summary'] = op_lines
                else:
                    new_summary = []
                    for line3 in episode['summary']:
                        if isinstance(line3, str):
                            new_summary.append(line3)
                        elif isinstance(line3, list):
                            new_summary.extend(line3)
                    episode['summary'] = new_summary
                    break
                break
            elif isinstance(line, str):
                op_lines.append(line)
        #if isinstance(episode["episodeNo"], str):
            #episode["episodeNo"] = int(episode["episodeNo"].lstrip("0"))
            #logging.warning("string for an 'episodeNo' value in %r", episode)
        #elif not isinstance(episode['episodeNo'], int):
            #logging.warning("%r has a non-integer 'episodeNo' value.", episode)
        # validate airdate
        _validate_date(episode)
    index2.extend(new_index)
    for episode in index2:
        episode["summary"] = list(map(lambda line: _remove_citation_numbers(line).strip(), episode["summary"]))
    return index2

# generate transcript line index

def restrict_to_transcript_folders(walk_entry):
    """
    """
    dirpath, dirlist, filelist = walk_entry
    return "transcripts" in dirpath.parts

def get_json_files(walk_entry):
    """
    """
    dirpath, dirlist, filelist = walk_entry
    new_filelist = filter(lambda file: file.endswith(".json"), filelist)
    return dirpath, dirlist, new_filelist

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
    index_no = 0
    for episode in episode_index:
        transcriptline = {
            "episodeId": episode['id'],
            "seasonNo": episode["seasonNo"],
            "episodeNo": episode["episodeNo"],
        }
        if isinstance(episode['seasonNo'], int) and isinstance(episode['episodeNo'], int):
            filepath = Path("output", "FiM", "transcripts", "S%d" % episode['seasonNo'], "E%02d.json" % episode['episodeNo'])
        elif isinstance(episode['seasonNo'], str):
            if episode['series'] == "FiM":
                root_path = Path("output", "FiM", "transcripts")
                #print(episode['seasonNo'])
                if episode['seasonNo'] == "The Movie":
                    filepath = root_path.joinpath("Movie").joinpath(episode['urlName'] + ".json")
                elif episode['seasonNo'] == "Best Gift Ever":
                    filepath = root_path.joinpath("Best_Gift_Ever", episode['urlName'] + ".json")
                elif episode['seasonNo'] == "FiF":
                    filepath = root_path.joinpath("FiF").joinpath(episode['urlName'] + ".json")
                elif episode['seasonNo'] == "Rainbow Roadtrip":
                    filepath = root_path.joinpath("Rainbow_Roadtrip").joinpath(episode['urlName'] + ".json")
                else:
                    raise Exception("Unknown episode encountered: %s" % episode['id'])
            elif episode['series'] == "EqG":
                root_path = Path("output", "EqG", "transcripts")
                try:
                    url_name = {
                        "Better Together (season 1)": "My_Little_Pony_Equestria_Girls:_Better_Together_(season_1)/",
                        "Better Together (season 2)": "My_Little_Pony_Equestria_Girls:_Better_Together_(season_2)/",
                        "Choose Your Own Ending (season 1)": "My_Little_Pony_Equestria_Girls:_Choose_Your_Own_Ending_(season_1)/",
                        "Choose Your Own Ending (season 2)": "My_Little_Pony_Equestria_Girls:_Choose_Your_Own_Ending_(season_2)/",
                        "Summertime Shorts": "My_Little_Pony_Equestria_Girls:_Summertime_Shorts/",
                    }[episode['seasonNo']]
                    #print(episode['urlName'].split("#")[-1])
                    if "Choose Your Own Ending" not in episode['seasonNo']:
                        filepath = root_path.joinpath(url_name).joinpath(episode['urlName'].split("#")[-1] + ".json")
                    else:
                        title_parts = episode['title'].split(' - ')
                        if len(title_parts) > 1:
                            name = title_parts[-1]
                            filename = episode['urlName'].split("#")[-1] + "#Choose " + name + "! ending.json"
                            filepath = root_path.joinpath(url_name).joinpath(filename)
                            if not filepath.exists():
                                name = {
                                    "Twilight": "Twilight Sparkle",
                                    "Rainbow": "Rainbow Dash",
                                    "Pinkie": "Pinkie Pie",
                                    "Big McIntosh": "Big Mac",
                                    "Principal Celestia": "Celestia",
                                }[name]
                                filename = episode['urlName'].split("#")[-1] + "#Choose " + name + "! ending.json"
                                filepath = root_path.joinpath(url_name).joinpath(filename)
                                #print(filepath, filepath.exists())
                                #assert filepath.exists()
                        else:
                            filename = episode['urlName'].split("#")[-1] + ".json"
                            filepath = root_path.joinpath(url_name).joinpath(filename)
                            #if not filepath.exists():
                                #new_name = { }
                                #filename = episode['urlName'].split("#")[-1] + "#Choose " + name + "! ending.json"
                                #filepath = root_path.joinpath(url_name).joinpath(filename)
                    #print(filepath)
                except KeyError:
                    pass
                    if episode['seasonNo'] == "My Little Pony Equestria Girls: Rainbow Rocks":
                        url_name = "My_Little_Pony_Equestria_Girls:_Rainbow_Rocks/"
                        if episode['episodeNo'] == 1:
                            filepath = root_path.joinpath(url_name.rstrip('/') + ".json")
                        else:
                            filepath = root_path.joinpath(url_name).joinpath(episode['urlName'].split('/')[-1].replace("#", "/") + ".json")
                    elif episode['seasonNo'] == "My Little Pony Equestria Girls: Friendship Games":
                        url_name = "My_Little_Pony_Equestria_Girls:_Friendship_Games/"
                        if episode['episodeNo'] == 1:
                            filepath = root_path.joinpath(url_name.rstrip('/') + ".json")
                        else:
                            filepath = root_path.joinpath(url_name).joinpath(episode['urlName'].split('#')[-1] + ".json")
                    else:
                        filepath = root_path.joinpath(episode['urlName'] + ".json")
                        #raise Exception("Unknown episode encountered: %s" % episode['id'])
        else:
            # FIM shorts
            filepath = Path("output", "FiM", "transcripts", "shorts").joinpath(episode['urlName'] + ".json")
            #filepath = root_path.joinpath("shorts")

        #print(filepath)
        with open(filepath) as rfile:
            lines = json.load(rfile)

        lines2 = []
        for indexno, line in enumerate(lines, start=1):
            speaker, dialogue = line
            dialogue = dialogue.strip()
            # remove blank lines
            if dialogue == "":
                if speaker is not None:
                    logging.warning("Speaker '%s' has no line at L%d in S%s E%d", speaker, indexno, episode['seasonNo'], episode['episodeNo'])
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

# TODO: Stop here!

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
        #

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
        index.sort(key=lambda entry: date.fromisoformat(entry['airdate']))
        for indexno, episode in enumerate(index):
            episode['id'] = indexno
            try:
                episode['seasonNo'] = {
                    "Rainbow Rocks": "My Little Pony Equestria Girls: Rainbow Rocks",
                    "Friendship Games": "My Little Pony Equestria Girls: Friendship Games",
                }[episode['seasonNo']]
            except KeyError:
                pass
        filename = "output/EqG/websiteIndexes/animationIndex.json"
        with open(filename, mode="w") as wfile:
            json.dump(index, wfile, indent=2)
        # sort by airdate
        # group like items somehow

    def save_transcriptline_index2():
        """
        """
        # get episode index
        # iterate over it, getting the appropriate filenames as appropriate.
        filename = "output/EqG/websiteIndexes/animationIndex.json"
        with open(filename) as rfile:
            episode_index = json.load(rfile)
        transcriptline_index = generate_transcriptline_index2(episode_index)
        filename = "output/EqG/websiteIndexes/transcriptLines.json"
        with open(filename, mode="w") as wfile:
            json.dump(transcriptline_index, wfile, indent=2)

    #save_regenerated_animation_index()
    save_transcriptline_index2()
