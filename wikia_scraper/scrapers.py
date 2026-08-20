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

SCRAPER = cloudscraper.create_scraper()

def get_speaker_and_dialogue(line):
    """
    """
    if ":" in line and "]" in line:
        colon_loc = line.index(":")
        bracket_loc = line.index("]")
        if colon_loc < bracket_loc:
            speaker = line[:colon_loc]
        else:
            speaker = line[:bracket_loc + 1]
        dialogue = line[min([colon_loc, bracket_loc]) + 1:]
    elif ":" in line:
        colon_loc = line.index(":")
        speaker = line[:colon_loc]
        dialogue = line[colon_loc + 1:]
    elif "]" in line and not line.endswith("]"):
        bracket_loc = line.index("]")
        speaker = line[:bracket_loc + 1]
        dialogue = line[bracket_loc + 1:]
    else:
        speaker = None
        dialogue = line
    return (speaker, dialogue)

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

    @staticmethod
    def download_unicorn_page(path, url):
        """
        """
        scraper = SCRAPER
        #logging.debug("Sending GET to '%s'.", url)
        return path.write_text(scraper.get(url).text, encoding="utf-8")
        #soup = bs4.BeautifulSoup(scraper.get(url).text, "html.parser")

    @staticmethod
    def parse_unicorn_appearances(soup):
        """
        """
        #scraper = cloudscraper.create_scraper()
        #logging.debug("Sending GET to '%s'.", url)
        #soup = bs4.BeautifulSoup(scraper.get(url).text, "html.parser")
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

    @staticmethod
    def parse_unicorn_summary(soup):
        """
        """
        summary_lines = []
        for _tag in soup.css.select(".mw-content-ltr.mw-parser-output > *"):
            if _tag.name == "p":
                summary_lines.append(_tag.text)
            elif "id" in _tag.attrs and _tag["id"] == "toc":
                break
        return summary_lines

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
        scraper = SCRAPER
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
                        filepath = Path("output", "FiM", "html", profile["urlName"] + ".html")
                        if not filepath.exists():
                            cls.download_unicorn_page(filepath, cls.ROOT + href)
                        soup = bs4.BeautifulSoup(filepath.read_text(), "html.parser")
                        #scraper = cloudscraper.create_scraper()
                        #logging.debug("Sending GET to '%s'.", url)
                        #soup = bs4.BeautifulSoup(scraper.get(url).text, "html.parser")
                        profile["episodes"] = cls.parse_unicorn_appearances(soup)
                        profile["summary"] = cls.parse_unicorn_summary(soup)
            index.append(profile)
        logging.debug("Compiled %d entries into the index", len(index))
        return index

# TODO: Scrape summaries of shorts
# TODO: Scrape shorts with multiple endings
# TODO: Scrape shorts with their own pages

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

    @staticmethod
    def download_page(filepath, url):
        """
        """
        scraper = SCRAPER
        logging.debug("Sending GET to '%s'.", url)
        response = scraper.get(url)
        filepath.with_name(response.url.split("/")[-1] + ".html").write_text(response.text, encoding="utf-8")
        return response

    @classmethod
    def scrape_clipshow_index(cls):
        """
        Scrapes following episode data from online episode index.
        - seasonNo
        - episodeNo
        - title
        - urlName
        - summary: get page
        - airdate
        """
        #url = "https://mlp.fandom.com/wiki/List_of_episodes"
        url = "https://mlp.fandom.com/wiki/Friendship_is_Magic_animated_media"
        filepath = Path("output", "FiM", "html", url.split('/')[-1] + ".html")
        if not filepath.exists():
            cls.download_page(filepath, url)
        keyword = "Clip shows"
        index = []
        season_no = "FiF"
        soup = bs4.BeautifulSoup(filepath.read_text(), "html.parser")
        h3 = soup.css.select_one("#Clip_shows").parent
        logging.debug("About to iterate through h3 siblings.")
        for _sibling in h3.find_next_siblings():
            if _sibling.name == "table":
                logging.debug("Found table. Scraping data.")
                for tr in _sibling.find("tbody").find_all("tr"):
                    # no, title, writer, airdate, transcript, gallery
                    entry = {"seasonNo": season_no}
                    for col_no, td in enumerate(tr.find_all("td")):
                        if col_no not in (0, 1, 3):
                            continue
                        if col_no == 0:
                            entry["episodeNo"] = int(td.text.lstrip("0"))
                        elif col_no == 1:
                            href = td.find("a")['href']
                            entry["urlName"] = href.split('/')[-1]
                            entry['title'] = td.text
                            filepath2 = Path('output', 'FiM', 'html', entry['urlName'] + ".html")
                            if not filepath2.exists():
                                cls.download_page(filepath2, cls.ROOT + href)
                            soup2 = bs4.BeautifulSoup(filepath2.read_text(), "html.parser")
                            entry['summary'] = cls.scrape_episode_summary(soup2)
                        elif col_no == 3:
                            title = td.find("span")['title']
                            entry['airdate'] = title[:title.index(' ')]
                    index.append(entry)
            if index:
                logging.debug("Index is full. Returning.")
                return index

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
        scraper = SCRAPER
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
    def scrape_episode_summary(soup):
        """
        """
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

    @classmethod
    def scrape_eqg_films(cls):
        """
        - seasonNo
        - episodeNo
        - title
        - urlName
        - summary
        - airdate
        """
        dirname = "output/EqG/"
        # scrape transcripts, indexes, and html
        url = "https://mlp.fandom.com/wiki/Equestria_Girls_animated_media"
        filepath = Path(dirname, "html", url.split("/")[-1] + ".html")
        if not filepath.exists():
            cls.download_page(filepath, url)
        soup = bs4.BeautifulSoup(filepath.read_text(), "html.parser")
        table = soup.css.select_one(".table-dotted-rows")
        index = []
        for indexno, tr in enumerate(table.find_all("tr")):
            if not indexno:
                continue
            #entry = {"seasonNo": None, "episodeNo": None}
            entry = {}
            entry['episodeNo'] = 1
            for col_no, td in enumerate(tr.find_all("td")):
                if col_no not in (0, 2, 3):
                    continue
                if col_no == 0:
                    entry['title'] = td.text
                    entry['seasonNo'] = td.text
                    href = td.find("a")['href']
                    entry['urlName'] = href.split('/')[-1] + ".html"
                    filepath2 = Path(dirname, "html", entry['urlName'])
                    url = cls.ROOT + href
                    if not filepath2.exists():
                        cls.download_page(filepath2, url)
                    soup = bs4.BeautifulSoup(filepath2.read_text(), "html.parser")
                    entry['summary'] = cls.scrape_episode_summary(soup)
                elif col_no == 2:
                    entry['airdate'] = td.text
                elif col_no == 3:
                    href2 = td.find('a')['href']
                    filepath3 = Path(dirname, "transcripts", entry['urlName'] + ".html")
                    url = cls.ROOT + href2
                    if not filepath3.exists():
                        cls.download_page(filepath3, url)
            index.append(entry)
        for _sibling in table.find_next_siblings():
            if _sibling.name == "h2":
                break
            if _sibling.name != "table":
                continue
            entry = {}
            entry['episodeNo'] = 1
            table = _sibling
            for indexno, tr in enumerate(table.find_all("tr")):
                if not indexno:
                    continue
                #entry = {"seasonNo": None, "episodeNo": None}
                entry = {}
                entry['episodeNo'] = 1
                for col_no, td in enumerate(tr.find_all("td")):
                    if col_no not in (0, 2, 3):
                        continue
                    if col_no == 0:
                        entry['title'] = td.text
                        entry['seasonNo'] = td.text
                        href = td.find("a")['href']
                        entry['urlName'] = href.split('/')[-1]
                        filepath2 = Path(dirname, "html", entry['urlName'])
                        url = cls.ROOT + href
                        if not filepath2.exists():
                            cls.download_page(filepath2, url)
                        soup = bs4.BeautifulSoup(filepath2.read_text(), "html.parser")
                        entry['summary'] = cls.scrape_episode_summary(soup)
                    elif col_no == 2:
                        entry['airdate'] = td.text
                    elif col_no == 3:
                        href2 = td.find('a')['href']
                        filepath3 = Path(dirname, "transcripts", entry['urlName'] + ".html")
                        url = cls.ROOT + href2
                        if not filepath3.exists():
                            cls.download_page(filepath3, url)
                index.append(entry)
        return index

    @classmethod
    def scrape_eqg_specials(cls, *, anchor_id = "#Specials"):
        """
        - seasonNo
        - episodeNo
        - title
        - urlName
        - summary
        - airdate
        """
        dirname = "output/EqG/"
        # scrape transcripts, indexes, and html
        url = "https://mlp.fandom.com/wiki/Equestria_Girls_animated_media"
        filepath = Path(dirname, "html", url.split("/")[-1] + ".html")
        if not filepath.exists():
            cls.download_page(filepath, url)
        soup = bs4.BeautifulSoup(filepath.read_text(), "html.parser")
        span = soup.css.select_one(anchor_id)
        #print("span", span)
        h2 = span.parent
        #print(span)
        #print("h2", h2)
        for _sibling in h2.find_next_siblings():
            if _sibling.name == "table":
                table = _sibling
                break
        #table = soup.css.select_one(".table-dotted-rows")
        index = []
        for tr in table.find_all("tr"):
            #if not indexno: continue
            #entry = {"seasonNo": None, "episodeNo": None}
            entry = {}
            entry['episodeNo'] = 1
            for col_no, td in enumerate(tr.find_all("td")):
                if col_no not in (1, 3, 4):
                    continue
                if col_no == 1:
                    entry['title'] = td.text
                    entry['seasonNo'] = td.text
                    href = td.find("a")['href']
                    entry['urlName'] = href.split('/')[-1]
                    filepath2 = Path(dirname, "html", entry['urlName'] + ".html")
                    url = cls.ROOT + href
                    if not filepath2.exists():
                        cls.download_page(filepath2, url)
                    soup = bs4.BeautifulSoup(filepath2.read_text(), "html.parser")
                    entry['summary'] = cls.scrape_episode_summary(soup)
                elif col_no == 3:
                    entry['airdate'] = td.text
                elif col_no == 4:
                    href2 = td.find('a')['href']
                    filepath3 = Path(dirname, "transcripts", entry['urlName'] + ".html")
                    url = cls.ROOT + href2
                    if not filepath3.exists():
                        cls.download_page(filepath3, url)
            index.append(entry)
        for _sibling in table.find_next_siblings():
            if _sibling.name == "h2":
                break
            if _sibling.name != "table":
                continue
            entry = {}
            entry['episodeNo'] = 1
            table = _sibling
            for tr in table.find_all("tr"):
                #if not indexno: continue
                #entry = {"seasonNo": None, "episodeNo": None}
                entry = {}
                entry['episodeNo'] = 1
                for col_no, td in enumerate(tr.find_all("td")):
                    if col_no not in (1, 3, 4):
                        continue
                    if col_no == 1:
                        entry['title'] = td.text
                        entry['seasonNo'] = td.text
                        href = td.find("a")['href']
                        entry['urlName'] = href.split('/')[-1]
                        filepath2 = Path(dirname, "html", entry['urlName'] + ".html")
                        url = cls.ROOT + href
                        if not filepath2.exists():
                            cls.download_page(filepath2, url)
                        soup = bs4.BeautifulSoup(filepath2.read_text(), "html.parser")
                        entry['summary'] = cls.scrape_episode_summary(soup)
                    elif col_no == 3:
                        entry['airdate'] = td.text
                    elif col_no == 4:
                        href2 = td.find('a')['href']
                        filepath3 = Path(dirname, "transcripts", entry['urlName'] + ".html")
                        url = cls.ROOT + href2
                        if not filepath3.exists():
                            cls.download_page(filepath3, url)
                index.append(entry)
        return index

    @classmethod
    def scrape_eqg_shorts(cls):
        """
        """
        dirname = "output/EqG/"
        # scrape transcripts, indexes, and html
        url = "https://mlp.fandom.com/wiki/Equestria_Girls_animated_media"
        filepath = Path(dirname, "html", url.split("/")[-1] + ".html")
        if not filepath.exists():
            cls.download_page(filepath, url)
        soup = bs4.BeautifulSoup(filepath.read_text(), "html.parser")
        span = soup.css.select_one("#Animated_shorts")
        #print("span", span)
        h2 = span.parent
        #print(span)
        #print("h2", h2)
        index = []
        for _sibling in h2.find_next_siblings():
            if _sibling.name == "h2":
                break
            if _sibling.name == "h3":
                season_no = _sibling.text.strip().rstrip("[]")
                try:
                    season_no = season_no[:season_no.index(" animated shorts")]
                except ValueError:
                    pass
            if _sibling.name == "table":
                table = _sibling
            #table = soup.css.select_one(".table-dotted-rows")
                for indexno, tr in enumerate(table.find('tbody').find_all("tr"), start=1):
                    #if not indexno: continue
                    #entry = {"seasonNo": None, "episodeNo": None}
                    entry = {}
                    entry['seasonNo'] = season_no
                    entry['episodeNo'] = indexno
                    for col_no, td in enumerate(tr.find_all("td")):
                        if col_no not in (1, 3, 4):
                            continue
                        if col_no == 1:
                            entry['title'] = td.text.strip()
                            href = td.find("a")['href']
                            entry['urlName'] = href.split('/')[-1]
                            filepath2 = Path(dirname, "html", entry['urlName'] + ".html")
                            url = cls.ROOT + href
                            #response = cls.download_page(filepath2, url)
                            #entry['urlName'] = response.url.split('/')[-1]
                            if not filepath2.exists():
                                response = cls.download_page(filepath2, url)
                                entry['urlName'] = response.url.split('/')[-1]
                            else:
                                for filepath in Path("output", "EqG", "html").iterdir():
                                    if not filepath.name.endswith(entry['urlName'] + ".html"):
                                        continue
                                    if filepath.name.endswith(entry['urlName'] + ".html") and filepath.name != entry['urlName'] + ".html":
                                        entry['urlName'] = filepath.name
                                        break
                            filepath2 = Path(dirname, "html", entry['urlName'] + ".html")
                            soup = bs4.BeautifulSoup(filepath2.read_text(), "html.parser")
                            if "#" not in entry['urlName']:
                                entry['summary'] = cls.scrape_episode_summary(soup)
                            else:
                                entry['summary'] = cls.scrape_shorts_summary(soup, entry['urlName'], entry['title'])
                                if not entry['summary']:
                                    entry['summary'] = cls.scrape_shorts_summary(soup, entry['urlName'], entry['title'], h = 4)
                        elif col_no == 3:
                            entry['airdate'] = td.text
                        elif col_no == 4:
                            href2 = td.find('a')['href']
                            filepath3 = Path(dirname, "transcripts", entry['urlName'] + ".html")
                            url = cls.ROOT + href2
                            if not filepath3.exists():
                                cls.download_page(filepath3, url)
                    index.append(entry)
        return index

    @classmethod
    def scrape_eqg_digital_shorts(cls):
        """
        """
        dirname = "output/EqG/"
        # scrape transcripts, indexes, and html
        url = "https://mlp.fandom.com/wiki/Equestria_Girls_animated_media"
        filepath = Path(dirname, "html", url.split("/")[-1] + ".html")
        if not filepath.exists():
            cls.download_page(filepath, url)
        soup = bs4.BeautifulSoup(filepath.read_text(), "html.parser")
        span = soup.css.select_one("#Digital_Series")
        #print("span", span)
        h2 = span.parent
        #print(span)
        #print("h2", h2)
        index = []
        for _sibling in h2.find_next_siblings():
            if _sibling.name == "h2":
                break
            if _sibling.name == "h3":
                season_no = _sibling.text.strip().rstrip("[]")
            if _sibling.name == "table":
                table = _sibling
            #table = soup.css.select_one(".table-dotted-rows")
                entry = {}
                for indexno, tr in enumerate(table.find('tbody').find_all("tr"), start=1):
                    #if not indexno: continue
                    #entry = {"seasonNo": None, "episodeNo": None}
                    entry = {}
                    entry['episodeNo'] = indexno
                    entry['seasonNo'] = season_no
                    for col_no, td in enumerate(tr.find_all("td")):
                        if col_no not in (1, 3, 4):
                            continue
                        if col_no == 1:
                            entry['title'] = td.text.strip()
                            href = td.find("a")['href']
                            entry['urlName'] = href.split('/')[-1]
                            if "." in entry['urlName']:
                                logging.warning("Period found in url-name: '%s'", entry['urlName'])
                            url = cls.ROOT + href
                            filepath2 = Path(dirname, "html", entry['urlName'] + ".html")
                            if not filepath2.exists():
                                response = cls.download_page(filepath2, url)
                                entry['urlName'] = response.url.split('/')[-1]
                            else:
                                for filepath in Path("output", "EqG", "html").iterdir():
                                    if not filepath.name.endswith(entry['urlName'] + ".html"):
                                        continue
                                    if filepath.name.endswith(entry['urlName'] + ".html") and filepath.name != entry['urlName'] + ".html":
                                        entry['urlName'] = filepath.name
                                        break
                            #soup = bs4.BeautifulSoup(filepath2.read_text(), "html.parser")
                            filepath2 = Path(dirname, "html", entry['urlName'] + ".html")
                            soup = bs4.BeautifulSoup(filepath2.read_text(), "html.parser")
                            if "#" not in entry['urlName']:
                                entry['summary'] = cls.scrape_episode_summary(soup)
                            else:
                                entry['summary'] = cls.scrape_shorts_summary(soup, entry['urlName'], entry['title'])
                                if not entry['summary']:
                                    entry['summary'] = cls.scrape_shorts_summary(soup, entry['urlName'], entry['title'], h = 4)
                        elif col_no == 3:
                            entry['airdate'] = td.text
                        elif col_no == 4:
                            href2 = td.find('a')['href']
                            filepath3 = Path(dirname, "transcripts", entry['urlName'] + ".html")
                            url = cls.ROOT + href2
                            if not filepath3.exists():
                                cls.download_page(filepath3, url)
                    index.append(entry)
        return index

    @staticmethod
    def scrape_shorts_summary(soup, anchor_id, title, *, h = 3):
        """
        """
        try:
            anchor_id = anchor_id[anchor_id.index("#") + 1:]
            logging.debug("Scanning for anchor id '%s'", anchor_id)
            span = soup.css.select_one("#" + anchor_id)
            h2 = span.parent
        except Exception as e:
            logging.debug("Scanning for title '%s'", title)
            logging.warning("Error: %s", e)
            #span = soup.css.select_one("#" + anchor_id)
            for _tag in soup.css.select(".mw-content-ltr.mw-parser-output > *"):
                tag_text = _tag.text.strip().rstrip("[]") 
                if tag_text == title:
                    h2 = _tag
                    break
        scan_for_text = False
        summary_lines = []
        for _sibling in h2.find_next_siblings():
            if _sibling.name == "h%d" % h:
                if _sibling.text.strip().rstrip("[]") == "Summary":
                    scan_for_text = True
            if scan_for_text is True:
                if _sibling.name == "p":
                    summary_lines.append(_sibling.text)
                if _sibling.name == "h%d" % (h - 1):
                    break
                if _sibling.name == "ul":
                    listitems = []
                    for li in _sibling.find_all("li", recursive=False):
                        listitems.append(li.text)
                    summary_lines.append(listitems)
        return summary_lines

class TranscriptScrapers:
    """
    """
    ROOT = "https://mlp.fandom.com"
    NUM_SEASONS = 9

    @staticmethod
    def download_episode_transcript(path, url):
        """
        """
        scraper = SCRAPER
        logging.warning("Sending GET to '%s'.", url)
        return path.write_text(scraper.get(url).text, encoding="utf-8")

    @staticmethod
    def parse_episode_transcript(soup):
        """
        """
        #scraper = cloudscraper.create_scraper()
        #logging.debug("Sending GET to '%s'.", url)
        #soup = bs4.BeautifulSoup(scraper.get(url).text, "html.parser")
        transcript_lines = []
        for dd in soup.css.select_one(".mw-content-ltr.mw-parser-output").find("dl").find_all("dd", recursive=False):
            line = dd.text
            speaker, dialogue = get_speaker_and_dialogue(line)
            transcript_lines.append((speaker, dialogue))
        # assumes every table has dl as the first element.
        for _sibling in soup.css.select_one(".mw-content-ltr.mw-parser-output").find("dl").find_next_siblings():
            if _sibling.name == "dl":
                for dd in _sibling.find_all("dd", recursive=False):
                    line = dd.text
                    speaker, dialogue = get_speaker_and_dialogue(line)
                    transcript_lines.append((speaker, dialogue))
            elif _sibling.name == "table":
                for dl in _sibling.find_all("dl", recursive=False):
                    line = dl.text
                    speaker, dialogue = get_speaker_and_dialogue(line)
                    transcript_lines.append((speaker, dialogue))
        for tagno, _tag in enumerate(soup.css.select(".mw-content-ltr.mw-parser-output > *")):
            if not tagno and _tag.name == "table":
                logging.error("Transcript table has a table tag as the first element.")
            break
        logging.info("Number of lines retrieved: %d", len(transcript_lines))
        return transcript_lines

    @staticmethod
    def parse_shorts_transcript(soup, anchor_id, title):
        """
        """
        #soup = bs4.BeautifulSoup(Path("output", "FiM", "transcripts", "shorts", "Ail-icorn.html").read_text(), "html.parser")
        #for h2 in soup.find_all("h2"):
            #print(h2.text)
        #anchor_id = "#Triple_Pony_Dare_Ya"
        #logging.debug("Searching for id='%s'", anchor_id)
        #anchor = soup.css.select_one(anchor_id).parent
        try:
            logging.debug("Scanning for anchor id='%s'", anchor_id)
            anchor = soup.css.select_one(anchor_id).parent
        except Exception as e:
            logging.debug("Scanning for title '%s'", title)
            logging.warning("Error: %s", e)
            #span = soup.css.select_one("#" + anchor_id)
            for _tag in soup.css.select(".mw-content-ltr.mw-parser-output > *"):
                tag_text = _tag.text.strip().rstrip("[]") 
                if tag_text == title:
                    anchor = _tag
                    break
        #transcript_dict = {}
        #transcript_dict[anchor_id.lstrip("#")] = []
        transcript_lines = []
        for indexno, _sibling in enumerate(anchor.find_next_siblings(), start=1):
            logging.debug("Line number: %d", indexno)
            if _sibling.name == "dl":
                for dd in _sibling.find_all("dd", recursive=False):
                    line = dd.text
                    speaker, dialogue = get_speaker_and_dialogue(line)
                    transcript_lines.append((speaker, dialogue))
            elif _sibling.name == "table":
                for dl in _sibling.find_all("dl", recursive=False):
                    line = dl.text
                    speaker, dialogue = get_speaker_and_dialogue(line)
                    transcript_lines.append((speaker, dialogue))
            elif _sibling.name == "h2":
                logging.debug("Number of lines compiled for '%s': %d", anchor_id, len(transcript_lines))
                break
                '''
                try:
                    anchor_id = _sibling.find("span")['id']
                except Exception as e:
                    logging.debug("_sibling: %s", _sibling)
                    logging.debug("anchor: %s", anchor)
                    raise e
                if "." in anchor_id:
                    logging.warning("Period found in anchor_id: '%s'", anchor_id)
                    anchor_id = anchor_id.replace(".", "%")
                transcript_dict[anchor_id.lstrip("#")] = []
                transcript_lines = transcript_dict[anchor_id.lstrip("#")]
                '''
            elif "class" in _sibling.attrs and "navbox" in _sibling['class']:
                break
        # stop when .navbox
        logging.debug("Number of lines retrieved: %r", len(transcript_lines))
        return transcript_lines

    @staticmethod
    def parse_multipart_shorts_transcript(soup, anchor_id, title):
        """
        """
        #anchor_id = "#Triple_Pony_Dare_Ya"
        try:
            logging.debug("Scanning for anchor id='%s'", anchor_id)
            anchor = soup.css.select_one(anchor_id).parent
        except Exception as e:
            logging.debug("Scanning for title '%s'", title)
            logging.warning("Error: %s", e)
            #span = soup.css.select_one("#" + anchor_id)
            for _tag in soup.css.select(".mw-content-ltr.mw-parser-output > *"):
                tag_text = _tag.text.strip().rstrip("[]") 
                if tag_text == title:
                    anchor = _tag
                    break
        #transcript_dict[anchor_id.lstrip("#")] = []
        transcript_dict = {None: []}
        transcript_lines = transcript_dict[None]
        logging.debug("anchor: %r", anchor)
        short_name = anchor_id
        for indexno, _sibling in enumerate(anchor.find_next_siblings(), start=1):
            logging.debug("Line number: %d", indexno)
            if _sibling.name == "dl":
                for dd in _sibling.find_all("dd", recursive=False):
                    line = dd.text
                    speaker, dialogue = get_speaker_and_dialogue(line)
                    transcript_lines.append((speaker, dialogue))
            elif _sibling.name == "table":
                for dl in _sibling.find_all("dl", recursive=False):
                    line = dl.text
                    speaker, dialogue = get_speaker_and_dialogue(line)
                    transcript_lines.append((speaker, dialogue))
            elif _sibling.name == "h3":
                logging.debug("Number of lines compiled for '%s': %d", anchor_id, len(transcript_lines))
                if len(transcript_lines) == 0:
                    logging.error("Zero lines found for: {short_name: %r, anchor_id: %r, title: %r}", short_name, anchor_id, title)
                try:
                    anchor_id = _sibling.find("span")['id']
                except Exception as e:
                    logging.debug("%s", anchor)
                    raise e
                if "." in anchor_id:
                    logging.warning("Period found in anchor_id: '%s'", anchor_id)
                    anchor_id = anchor_id.replace(".", "%")
                transcript_dict[anchor_id.lstrip("#")] = []
                transcript_lines = transcript_dict[anchor_id.lstrip("#")]
            elif _sibling.name == "h2":
                break
        logging.debug("Number of parts retrieved: %r", len(transcript_dict))
        return transcript_dict

    @classmethod
    def scrape_episode_transcripts(cls):
        """
        """
        url = "https://mlp.fandom.com/wiki/Friendship_is_Magic_animated_media"
        scraper = SCRAPER
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
                        dirpath = Path("output", "FiM", "html", "S%d" % season_no)
                        dirpath.mkdir(exist_ok=True)
                        filepath = dirpath.joinpath("E%02d.html" % episode_no)
                        if not filepath.exists():
                            cls.download_episode_transcript(filepath, cls.ROOT + href)
                        soup = bs4.BeautifulSoup(filepath.read_text(), 'html.parser')
                        transcripts[(season_no, int(true_episode_no.lstrip("0")))] = cls.parse_episode_transcript(soup)
        return transcripts

if __name__ == "__main__":
    logging.basicConfig(
        filename=".scrapers.log",
        level=logging.DEBUG,
        filemode="w",
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
    def save_clipshow_index():
        """
        """
        filename = "output/FiM/indexes/clipshow.json"
        index = MetadataScrapers.scrape_clipshow_index()
        with open(filename, mode="w") as wfile:
            json.dump(index, wfile, indent=2)
    def save_specials_transcripts():
        """
        """
        for dirpath, _, filelist in Path("output", "FiM", "transcripts").walk():
            for htmlfile in filter(lambda file: file.endswith(".html"), filelist):
                if dirpath.parts[-1] == "shorts":
                    continue
                filepath = dirpath.joinpath(htmlfile)
                soup = bs4.BeautifulSoup(filepath.read_text(encoding="utf-8"), "html.parser")
                transcript_lines = TranscriptScrapers.parse_episode_transcript(soup)
                with open(filepath.with_suffix(".json"), mode="w") as wfile:
                    json.dump(transcript_lines, wfile, indent=2)
        for dirpath, _, filelist in Path("output", "FiM", "transcripts").walk():
            if dirpath.parts[-1] != "shorts":
                continue
            for htmlfile in filter(lambda file: file.endswith(".html"), filelist):
                dirpath = Path("output", "FiM", "transcripts", "shorts")
                soup = bs4.BeautifulSoup(dirpath.joinpath("Ail-icorn.html").read_text(), "html.parser")
                anchor_id = "#Triple_Pony_Dare_Ya"
                transcript_dict = TranscriptScrapers.parse_shorts_transcript(soup, anchor_id)
                for anchor_id, lines in transcript_dict.items():
                    with open(dirpath.joinpath(anchor_id).with_suffix(".json"), mode="w") as wfile:
                        json.dump(lines, wfile, indent=2)
                break
    def save_eqg_films_index():
        """
        """
        filename = "output/EqG/indexes/films.json"
        #index = TranscriptScrapers.scrape_eqg_films()
        index = MetadataScrapers.scrape_eqg_films()
        with open(filename, mode="w") as wfile:
            json.dump(index, wfile, indent=2)
        dirname = "output/EqG/transcripts/"
        for entry in filter(lambda entry: "urlName" in entry, index):
            #for entry in index:
            url_name = entry['urlName']
            filepath = Path(dirname, url_name + ".html")
            soup = bs4.BeautifulSoup(filepath.read_text(), "html.parser")
            lines = TranscriptScrapers.parse_episode_transcript(soup)
            with open(filepath.with_suffix(".json"), mode="w") as wfile:
                json.dump(lines, wfile, indent=2)

    #save_specials_transcripts()
    #save_eqg_films_index()
    def save_eqg_specials_index():
        """
        """
        filename = "output/EqG/indexes/specials.json"
        #index = TranscriptScrapers.scrape_eqg_films()
        index = MetadataScrapers.scrape_eqg_specials()
        with open(filename, mode="w") as wfile:
            json.dump(index, wfile, indent=2)
        dirname = "output/EqG/transcripts/"
        for entry in filter(lambda entry: "urlName" in entry, index):
            url_name = entry['urlName']
            filepath = Path(dirname, url_name + ".html")
            soup = bs4.BeautifulSoup(filepath.read_text(), "html.parser")
            lines = TranscriptScrapers.parse_episode_transcript(soup)
            with open(filepath.with_suffix(".json"), mode="w") as wfile:
                json.dump(lines, wfile, indent=2)
    #save_eqg_films_index()
    #save_eqg_specials_index()

    def save_eqg_shorts_index():
        """
        """
        filename = "output/EqG/indexes/shorts.json"
        index = MetadataScrapers.scrape_eqg_shorts()
        index2 = MetadataScrapers.scrape_eqg_digital_shorts()
        index.extend(index2)
        with open(filename, mode="w") as wfile:
            json.dump(index, wfile, indent=2)
        #dirname = "output/EqG/transcripts/"
        #for entry in filter(lambda entry: "urlName" in entry, index):
            #url_name = entry['urlName']
            #filepath = Path(dirname, url_name + ".html")
            #soup = bs4.BeautifulSoup(filepath.read_text(), "html.parser")
            #lines = TranscriptScrapers.parse_episode_transcript(soup)
            #with open(filepath.with_suffix(".json"), mode="w") as wfile:
                #json.dump(lines, wfile, indent=2)
    #save_eqg_shorts_index()

    '''
    def save_eqg_shorts_transcripts():
        """
        """
        filename = "output/EqG/indexes/shorts.json"
        with open(filename) as rfile:
            index = json.load(rfile)
        dirname = "output/EqG/transcripts/"
        for entry in filter(lambda entry: "urlName" in entry, index):
            url_name = entry['urlName']
            filepath = Path(dirname, url_name + ".html")
            soup = bs4.BeautifulSoup(filepath.read_text(), "html.parser")
            season_no = entry['seasonNo']
            title = entry['title'].strip()
            logging.debug("season_no: %s, url_name: %s", season_no, url_name)
            if "Choose Your Own Ending" in season_no:
                logging.debug("TranscriptScrapers.parse_multipart_shorts_transcript(soup, '%s', '%s')", anchor_id, title)
                anchor_id = url_name[url_name.index("#") + 1:]
                lines_dict = TranscriptScrapers.parse_multipart_shorts_transcript(soup, "#" + anchor_id, title)
                logging.debug("lines_dict: %r", lines_dict)
                for anchor_id, lines in lines_dict.items():
                    suffix = ("#" + anchor_id if anchor_id is not None else "")
                    dirpath = Path(dirname, season_no)
                    dirpath.mkdir(exist_ok=True)
                    filepath = Path(dirname, season_no, url_name[url_name.index("#") + 1:] + suffix + ".json")
                    logging.debug("Saving to: %r", filepath)
                    if len(lines) == 0:
                        logging.error("season_no: %r, url_name: %r, title: %r, len(lines): %r", season_no, url_name, title, len(lines))
                    with open(filepath, mode="w") as wfile:
                        json.dump(lines, wfile, indent=2)
            elif "#" in url_name:
                anchor_id = url_name[url_name.index("#") + 1:]
                logging.debug("TranscriptScrapers.parse_shorts_transcript(soup, '%s', '%s')", anchor_id, title)
                lines = TranscriptScrapers.parse_shorts_transcript(soup, "#" + anchor_id, title)
                if len(lines) == 0:
                    logging.error("season_no: %r, url_name: %r, title: %r, len(lines): %r", season_no, url_name, title, len(lines))
                suffix = "#" + url_name + "#" + anchor_id
                with open(Path(dirname, suffix + ".json"), mode="w") as wfile:
                    json.dump(lines, wfile, indent=2)
                #for line in lines:
            else:
                lines = TranscriptScrapers.parse_episode_transcript(soup)
                if len(lines) == 0:
                    logging.error("season_no: %r, url_name: %r, title: %r, len(lines): %r", season_no, url_name, title, len(lines))
                with open(Path(dirname, url_name + ".json"), mode="w") as wfile:
                    json.dump(lines, wfile, indent=2)
    '''
    def save_eqg_shorts_transcripts():
        """
        """
        #filename = "output/EqG/indexes/shorts.json"
        #with open(filename) as rfile:
            #index = json.load(rfile)
        dirname = "output/EqG/transcripts/"
        for dirpath, _, filelist in Path(dirname).walk():
            for file in filter(lambda file: file.endswith(".html"), filelist):
                filepath = dirpath.joinpath(file)
                soup = bs4.BeautifulSoup(filepath.read_text(), "html.parser")
                if "Choose_Your_Own_Ending" in filepath.name:
                    for h2 in soup.css.select("h2.open-section"):
                        transcript_dict = {None: []}
                        transcript_lines = transcript_dict[None]
                        section = h2.find_next_sibling()
                        assert section.name == "section"
                        for dl in section.find_all("dl", recursive=False):
                            for dd in dl.find_all("dd", recursive=False):
                                line = dd.text
                                speaker, dialogue = get_speaker_and_dialogue(line)
                                transcript_lines.append((speaker, dialogue))
                        for _sibling in section.find_next_siblings():
                            if _sibling.name == "h3":
                                transcript_lines = []
                                transcript_dict[_sibling.text.strip().rstrip("[]")] = transcript_lines
                            if _sibling.name == "h2":
                                break
                            if _sibling.name == "table":
                                if "class" in _sibling.attrs and "navbox" in _sibling['class']:
                                    pass
                                else:
                                    logging.warning("table in %s", filepath, _sibling)
                            if _sibling.name == "dl":
                                for dd in _sibling.find_all("dd", recursive=False):
                                    line = dd.text
                                    speaker, dialogue = get_speaker_and_dialogue(line)
                                    transcript_lines.append((speaker, dialogue))
                        #print(transcript_dict)
                        for scenario, lines in transcript_dict.items():
                            suffix = ("" if scenario is None else "#" + scenario)
                            filepath2 = filepath.with_suffix("").joinpath(h2['id'].strip() + suffix + ".json")
                            #logging.error("No lines for %r!%r", filepath, scenario)
                            if not lines:
                                logging.error("No lines for %r!%r", filepath, scenario)
                            with open(filepath2, mode="w") as wfile:
                                json.dump(lines, wfile, indent=2)
                            #print(dirpath2)
                else:
                    for h2 in soup.css.select("h2.open-section"):
                        lines = []
                        section = h2.find_next_sibling()
                        assert section.name == "section"
                        filepath2 = filepath.with_suffix("").joinpath(h2['id'].strip() + ".json")
                        for _tag in section.find_all():
                            #print(filepath2)
                            if _tag.name == "table":
                                if "class" in _tag.attrs and "navbox" in _tag['class']:
                                    pass
                                if _tag.find("dl") is None:
                                    continue
                                else:
                                    for td in _tag.find_all("td"):
                                        line = td.text
                                        speaker, dialogue = get_speaker_and_dialogue(line)
                                        lines.append((speaker, dialogue))
                                        #logging.warning("table in %s: %s", filepath, _tag)
                                    pass
                            if _tag.name == "h2":
                                break
                            if _tag.name == "dl":
                                for dd in _tag.find_all("dd", recursive=False):
                                    line = dd.text
                                    speaker, dialogue = get_speaker_and_dialogue(line)
                                    lines.append((speaker, dialogue))
                        if not lines:
                            logging.error("No lines for %s!%r", filepath2, scenario)
                        with open(filepath2, mode="w") as wfile:
                            json.dump(lines, wfile, indent=2)
                        #print(filepath2)
                    #print(dirpath2)
                    #print(filepath, section)
                #print(filepath)
        #for entry in filter(lambda entry: "urlName" in entry, index):
            #pass
    save_eqg_shorts_transcripts()
