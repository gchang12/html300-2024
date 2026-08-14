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

# reformat episode index
# regenerate episode index with id's
# generate transcript line index

import json
from pathlib import Path
import logging
