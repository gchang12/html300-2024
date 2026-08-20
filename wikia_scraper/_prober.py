from pathlib import Path
import json

import bs4
import cloudscraper

#response = scraper.get("https://mlp.fandom.com/wiki/Make_Up_Shake_Up")

#raise Exception("%s, %s" % (dir(response), response.url))

'''
for x, y, z in Path("output", "FiM", "transcripts").walk():
    if y:
        continue
    if not x.parts[-1].startswith("S"):
        continue
    for filename in z:
        filepath = x.joinpath(filename)
        with open(filepath) as rfile:
            lines = json.load(rfile)
        for indexno, (speaker, dialogue) in enumerate(lines, start=1):
            if speaker is None and not (dialogue.startswith("[") and dialogue.endswith("]")):
                print(filepath, indexno, dialogue)
                break
'''

'''
soup = bs4.BeautifulSoup(Path("output", "EqG", "transcripts", "My_Little_Pony_Equestria_Girls:_Better_Together_(season_1)#Turf_War.html").read_text(), "html.parser")
anchor_id = "#School_of_Rock"
title = "School of Rock"

try:
    anchor = soup.css.select_one(anchor_id)
except Exception as e:
    #logging.warning("Error: %s", e)
    #span = soup.css.select_one("#" + anchor_id)
    for _tag in soup.css.select(".mw-content-ltr.mw-parser-output > *"):
        tag_text = _tag.text.strip().rstrip("[]") 
        if tag_text == title:
            anchor = _tag
            break
#transcript_dict = {}
#transcript_dict[anchor_id.lstrip("#")] = []
transcript_lines = []
#print(anchor)

anchor2 = anchor.find_next_sibling()


for indexno, _sibling in enumerate(anchor2.find_all(), start=1):
    #print(_sibling)
    #print(indexno)
    #print(indexno, _sibling.name)
    #print(_sibling.find_all(recursive=False))
    #print(_sibling.name)
    if _sibling.name == "dl":
        #print("dl", _sibling)
        for dd in _sibling.find_all("dd", recursive=False):
            line = dd.text
            print(line)
            #speaker, dialogue = get_speaker_and_dialogue(line)
            #transcript_lines.append((speaker, dialogue))
    elif _sibling.name == "table":
        #print("table", _sibling)
        for dl in _sibling.find_all("dl", recursive=False):
            line = dl.text
            print(line)
            #speaker, dialogue = get_speaker_and_dialogue(line)
            #transcript_lines.append((speaker, dialogue))
    elif _sibling.name == "h2":
        #print("h2", _sibling)
        break
    elif "class" in _sibling.attrs and "navbox" in _sibling['class']:
        break

print(transcript_lines)
'''

'''
filename = "output/EqG/html/Equestria_Girls_animated_media.html"
soup = bs4.BeautifulSoup(Path(filename).read_text(), "html.parser")
for table in soup.css.select(".table-dotted-rows"):
    for tr in table.find_all("tr"):
'''

'''
filename = "output/EqG/indexes/shorts.json"
with open(filename) as rfile:
    index = json.load(rfile)
urlnames = set()
for entry in filter(lambda entry: 'urlName' in entry, index):
    if entry['urlName'].startswith("Animated_shorts"):
        url_name = entry['urlName'][:entry['urlName'].index("#")]
        if entry['seasonNo'] == "Rainbow Rocks":
            url_name = "My_Little_Pony_Equestria_Girls:_Rainbow_Rocks/" + url_name
        elif entry['seasonNo'] == "Friendship Games":
            url_name = "My_Little_Pony_Equestria_Girls:_Friendship_Games/" + url_name
    elif "#" in entry['urlName']:
        url_name = entry['urlName'][:entry['urlName'].index("#")]
    else:
        url_name = entry['urlName']
    urlnames.add(url_name)
for name in urlnames:
    print(name)
'''

scraper = cloudscraper.create_scraper()
ROOT = "https://mlp.fandom.com/wiki/Transcripts/"
hrefs = (
    "My_Little_Pony_Equestria_Girls:_Friendship_Games/Animated_shorts",
    "My_Little_Pony_Equestria_Girls:_Rainbow_Rocks/Animated_shorts",
    "Friendship_Through_the_Ages",
    "Perfect_Day_for_Fun",
    "Run_to_Break_Free",
    "Find_the_Magic",
    "Get_the_Show_on_the_Road",
    "Shake_Things_Up!",
    "Coinky-Dink_World",
    "Monday_Blues",
    "Mad_Twience",
    "Good_Vibes",
    "The_Other_Side",
    "Let_It_Rain",
    "My_Little_Pony_Equestria_Girls:_Summertime_Shorts",
    "So_Much_More_to_Me",
    "My_Past_is_Not_Today",
    "Shake_Your_Tail",
    "My_Little_Pony_Equestria_Girls:_Better_Together_(season_1)",
    "My_Little_Pony_Equestria_Girls:_Better_Together_(season_2)",
    "I%27m_on_a_Yacht",
    "Life_is_a_Runway",
    "Five_to_Nine",
    "Cheer_You_On",
    "My_Little_Pony_Equestria_Girls:_Choose_Your_Own_Ending_(season_1)",
    "My_Little_Pony_Equestria_Girls:_Choose_Your_Own_Ending_(season_2)",
)
for href in hrefs:
    response = scraper.get(ROOT + href)
    if response.ok:
        Path("output", "EqG", "transcripts", href + ".html").write_text(response.text, encoding="utf-8")
    else:
        print(href)
