"""
Scrapes the following episode data for MLP G4.
{
  seasonNo: number,
  episodeNo: number,
  title: string,
  urlName: string,
  summary: Array<string>,
  airdate: string,
}
Also scrapes unformatted transcript data.
"""

import json
from pathlib import Path
import logging

import requests
import cloudscraper
import bs4

class MetadataScrapers:
    """
    """
    ROOT = "https://mlp.fandom.com"

    # FIM
    ## episodes (X)
    # - https://mlp.fandom.com/wiki/Friendship_is_Magic_animated_media#Episodes
    ## clip show
    # - https://mlp.fandom.com/wiki/Friendship_is_Magic_animated_media#Clip_shows
    ## films
    # - https://mlp.fandom.com/wiki/Friendship_is_Magic_animated_media#Films
    ## specials
    # - https://mlp.fandom.com/wiki/Friendship_is_Magic_animated_media#Specials
    ## shorts
    # - https://mlp.fandom.com/wiki/Friendship_is_Magic_animated_media#Animated_shorts

    # EQG
    ## films
    # - https://mlp.fandom.com/wiki/Equestria_Girls_animated_media#Films
    ## shorts
    # - https://mlp.fandom.com/wiki/Equestria_Girls_animated_media#Animated_shorts
    ## specials
    # - https://mlp.fandom.com/wiki/Equestria_Girls_animated_media#Specials
    ## digital series
    # - https://mlp.fandom.com/wiki/Equestria_Girls_animated_media#Digital_Series

    @classmethod
    def scrape_episode_index(cls):
        """
        Scrapes following episode data from online episode index.
        - seasonNo
        - episodeNo
        - title
        - urlName
        - summary
        - airdate
        """
        #url = "https://mlp.fandom.com/wiki/List_of_episodes"
        url = "https://mlp.fandom.com/wiki/Friendship_is_Magic_animated_media"
        scraper = cloudscraper.create_scraper()
        logging.debug("Sending GET to '%s'.", url)
        soup = bs4.BeautifulSoup(scraper.get(url).text, "html.parser")
        #table_fields = ( "episodeNo", "title", "writer", "airdate", # transcript # gallery)
        index = []
        for season_no, tbody in enumerate(soup.css.select(".table-dotted-rows > tbody"), start=1):
            logging.debug("Fetching data for S%d", season_no)
            for episode_no, tr in enumerate(tbody.find_all("tr"), start=1):
                # seasonNo
                logging.debug("Fetching data for E%d", episode_no)
                episode = {"seasonNo": season_no}
                for col_no, td in enumerate(tr.find_all("td")):
                    if col_no not in (0, 1, 3):
                        continue
                    td_text = td.text
                    if col_no == 0:
                        # episodeNo
                        try:
                            episode["episodeNo"] = td_text[:td_text.index(" ")]
                        except ValueError:
                            # expect to fail upon reaching S10
                            logging.debug("All data fetched.")
                            return index
                    elif col_no == 1:
                        # title, urlName, summary
                        episode["title"] = td_text
                        href = td.find('a')['href']
                        episode["urlName"] = href.split('/')[-1]
                        episode["summary"] = cls.scrape_episode_summary(cls.ROOT + href)
                    elif col_no == 3:
                        # airdate
                        episode["airdate"] = td_text
                index.append(episode)

    @staticmethod
    def scrape_episode_summary(url):
        """
        """
        scraper = cloudscraper.create_scraper()
        soup = bs4.BeautifulSoup(scraper.get(url).text, "html.parser")
        #print(soup)
        summary_lines = []
        for _tag in soup.css.select(".mw-content-ltr.mw-parser-output > *"):
            #print(_tag)
            if _tag.name == "p":
                summary_lines.append(_tag.text)
                continue
                #print(_tag.name)
            if "id" in _tag.attrs and _tag['id'] == "toc":
                break
        logging.debug("Fetched %d summary-lines.", len(summary_lines))
        return summary_lines

class TranscriptScrapers:
    """
    """
    ROOT = "https://mlp.fandom.com"
    NUM_SEASONS = 9

    @staticmethod
    def scrape_episode_transcript(url):
        """
        """
        scraper = cloudscraper.create_scraper()
        logging.debug("Sending GET to '%s'.", url)
        soup = bs4.BeautifulSoup(scraper.get(url).text, "html.parser")
        transcript_lines = []
        for dd in soup.css.select_one(".mw-content-ltr.mw-parser-output").find("dl").find_all("dd"):
            line = dd.text
            try:
                speaker = line[:line.index(": ")]
                dialogue = line[line.index(": ") + 2:]
            except ValueError:
                speaker = None
                dialogue = line
            transcript_lines.append((speaker, dialogue))
        # assumes every table has dl as the first element.
        for _sibling in soup.css.select_one(".mw-content-ltr.mw-parser-output").find("dl").find_next_siblings():
            if _sibling.name == "dl":
                for dd in _sibling.find_all("dd"):
                    line = dd.text
                    try:
                        speaker = line[:line.index(": ")]
                        dialogue = line[line.index(": ") + 2:]
                    except ValueError:
                        speaker = None
                        dialogue = line
                    transcript_lines.append((speaker, dialogue))
            elif _sibling.name == "table":
                for dl in _sibling.find_all("dl"):
                    speaker_dialogue = []
                    for dd_no, dd in enumerate(dl.find_all("dd")):
                        if not dd_no:
                            dd_text = dd.text.rstrip(": \n\r")
                        else:
                            dd_text = dd.text
                        speaker_dialogue.append(dd_text)
                    transcript_lines.append(tuple(speaker_dialogue))
        for tagno, _tag in enumerate(soup.css.select(".mw-content-ltr.mw-parser-output > *")):
            if not tagno and _tag.name == "table":
                logging.error("Transcript table for '%s' has a table tag as the first element.", url)
            break
        logging.info("Number of lines retrieved from '%s': %d", url, len(transcript_lines))
        return transcript_lines

    @classmethod
    def scrape_episode_transcripts(cls):
        """
        """
        url = "https://mlp.fandom.com/wiki/Friendship_is_Magic_animated_media"
        scraper = cloudscraper.create_scraper()
        logging.debug("Sending GET to '%s'.", url)
        soup = bs4.BeautifulSoup(scraper.get(url).text, "html.parser")
        # save to (season_no, episode_no) key
        transcripts = {}
        for season_no, tbody in enumerate(soup.css.select(".table-dotted-rows > tbody"), start=1):
            if season_no > cls.NUM_SEASONS:
                break
            logging.debug("Fetching transcript for S%d", season_no)
            for episode_no, tr in enumerate(tbody.find_all("tr"), start=1):
                logging.debug("Fetching transcript for E%d", episode_no)
                for col_no, td in enumerate(tr.find_all("td")):
                    td_text = td.text
                    if col_no == 0:
                        true_episode_no = td_text[:td_text.index(" ")]
                        continue
                    elif col_no < 4:
                        continue
                    elif col_no > 4:
                        break
                    else:
                        href = td.find("a")['href']
                        transcripts[(season_no, int(true_episode_no.lstrip("0")))] = cls.scrape_episode_transcript(cls.ROOT + href)
        return transcripts

class CharacterMetadataScraper:
    """
    Character data
    - name
    - urlName
    - type
    - gender
    - episodes: {
        vocally: [],
        silently: [],
        inBackground: [],
        inFantasy: [],
        inMedia: [],
        mentioned: [],
      }
    """
    ROOT = "https://mlp.fandom.com"

    @classmethod
    def scrape_unicorn_appearances(cls, url):
        """
        """
        scraper = cloudscraper.create_scraper()
        logging.debug("Sending GET to '%s'.", url)
        soup = bs4.BeautifulSoup(scraper.get(url).text, "html.parser")
        appearances = {}
        season_conversion_table = {
            "Season one": 1,
            "Season two": 2,
            "Season three": 3,
            "Season four": 4,
            "Season five": 5,
            "Season six": 6,
            "Season seven": 7,
            "Season eight": 8,
            "Season nine": 9,
        }
        for table in soup.css.select("table.wikitable.appearances"):
            try:
                season_no = season_conversion_table[table.find("caption").text.strip()]
            except AttributeError as e:
                continue
            for episode_no, td in enumerate(table.find("tbody").find("tr").find_next_sibling().find_all("td"), start=1):
                appearances["S%d-E%02d" % (season_no, episode_no)] = td.text
        logging.debug("Compiled %d appearances", len(appearances))
        return appearances

    @classmethod
    def scrape_unicorn_profiles(cls):
        """
        - name
        - urlName
        - species
        - gender
        - episodes: {
            vocally: [],
            silently: [],
            inBackground: [],
            inFantasy: [],
            inMedia: [],
            mentioned: [],
          }
        """
        #url = "https://mlp.fandom.com/wiki/Friendship_is_Magic_animated_media"
        url = "https://mlp.fandom.com/wiki/List_of_ponies/Unicorn_ponies"
        scraper = cloudscraper.create_scraper()
        logging.debug("Sending GET to '%s'.", url)
        soup = bs4.BeautifulSoup(scraper.get(url).text, "html.parser")
        index = []
        table_fields = (
            "name",
            "kind",
            "group",
            "coat color",
            "mane color",
            "eye color",
            "first appearance",
            "description",
            "image",
        )
        for tr in soup.css.select(".wikitable.listofponies tbody tr"):
            profile = {"species": "Unicorn"}
            for table_field, td in zip(table_fields, tr.find_all("td")):
                #print(table_field, td.text)
                if table_field not in (
                    "name",
                    #"kind",
                    "group",
                    "description",
                ):
                    continue
                if table_field == "name":
                    profile["name"] = td.text
                elif table_field == "group":
                    profile["gender"] = td.text
                elif table_field == "description":
                    if td.text.startswith("See ") and td.find("a") is not None and profile['name'] in td.find("a").text:
                        href = td.find("a")['href']
                        profile["urlName"] = href.split("/")[-1]
                        profile["episodes"] = cls.scrape_unicorn_appearances(cls.ROOT + href)
            index.append(profile)
        logging.debug("Compiled %d entries into the index", len(index))
        return index

if __name__ == "__main__":
    logging.basicConfig(
        filename=".scrapers.log",
        level=logging.INFO,
        format="%(levelname)s:%(module)s.%(funcName)s: %(message)s",
    )
    def save_episode_index():
        """
        """
        filename = "output/FiM/indexes/episodes.json"
        if Path(filename).exists():
            logging.info("'%s' already exists. Skipping.", filename)
            return
        index = MetadataScrapers.scrape_episode_index()
        with open(filename, mode="w") as wfile:
            json.dump(index, wfile, indent=2)
    def save_episode_transcripts():
        """
        """
        dirname = "output/FiM/transcripts/"
        #if tuple(Path(dirname).iterdir()):
            #logging.info("'%s' is already populated. Skipping.", dirname)
            #return
        #logging.debug("Scraping episode transcripts.")
        transcripts = TranscriptScrapers.scrape_episode_transcripts()
        logging.info("Done scraping episode transcripts.")
        for (season_no, episode_no), transcript_lines in transcripts.items():
            transcript_subpath = Path(dirname, "S%d" % season_no)
            transcript_subpath.mkdir(exist_ok=True)
            with open(transcript_subpath.joinpath("E%02d.json" % episode_no), mode="w") as wfile:
                json.dump(transcript_lines, wfile, indent=2)
        logging.info("Done dumping episode transcripts into '%s'.", dirname)
    def save_unicorn_profiles():
        """
        """
        filepath = Path("output/FiM/indexes/unicorns.json")
        index = CharacterMetadataScraper.scrape_unicorn_profiles()
        logging.debug("Done scraping unicorn profiles.")
        if filepath.exists():
            logging.debug("Updating index with existing on-disk index at '%s'", filepath)
            with open(filepath) as rfile:
                old_index = json.load(rfile)
            assert len(old_index) == len(index)
            for old, new in zip(old_index, index):
                if "episodes" not in old or "episodes" not in new:
                    continue
                new["episodes"].update(old["episodes"])
            logging.debug("Done updating index.")
        with open(filepath, mode="w") as wfile:
            json.dump(index, wfile, indent=2)
        logging.debug("Dumped unicorn index into '%s'.", filepath)
    #save_episode_index()
    save_episode_transcripts()
    #save_unicorn_profiles()
    #FiMScrapers.scrape_episode_summary("https://mlp.fandom.com/wiki/Owl%27s_Well_That_Ends_Well")
    #url = "https://mlp.fandom.com/wiki/Equestria_Girls_animated_media"
    #CharacterMetadataScraper.scrape_unicorn_profiles()
    #appearances = CharacterMetadataScraper.scrape_unicorn_appearances("https://mlp.fandom.com/wiki/Mistmane")
    #print(appearances)

