"""
Scraper and index compiler for MLP data.
Things to scrape:
    Episode data
    - seasonNo
    - episodeNo
    - title
    - urlName
    - summary
    - airdate
    Episode transcripts
    - episodeId
    - lineNo
    - speaker
    - lineText
    Character data
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
