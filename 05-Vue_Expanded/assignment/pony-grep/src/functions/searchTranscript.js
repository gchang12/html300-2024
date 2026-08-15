import MiniSearch from "minisearch";

import transcriptLines from "../constants/transcriptLines.js";

export default function searchTranscript(searchCriteria) {
  const { isSung, seasonNo, episodeNo, dialoguePattern, speaker } = searchCriteria;
  let miniSearch = new MiniSearch({
    idField: "id",
    fields: ["dialogue"],
    storeFields: ["id", "episodeId", "lineNo"],
  });
  const filteredTranscriptLines = transcriptLines.filter(lineEntry => {
    const conditions = [];
    // check if lineEntry.speaker includes speaker
    if (speaker !== "") {
      conditions.push(lineEntry.speaker.includes(speaker));
    }
    // If isSung -> true, check if the speaker has brackets around; otherwise include everything.
    if (isSung != null) {
      conditions.push(lineEntry.speaker.startsWith("[") && lineEntry.speaker.endsWith("]"));
    }
    // if seasonNo is specified and so is episodeNo, limit results to entries with the specified episodeNo; otherwise include everything.
    if (seasonNo !== "") {
      conditions.push(lineEntry.seasonNo == seasonNo);
      if (episodeNo !== "") {
        conditions.push(lineEntry.episodeNo == episodeNo);
      }
    }
    return conditions.every((condition) => condition === true);
  });
  miniSearch.addAll(filteredTranscriptLines);
  const searchResults = miniSearch.search(dialoguePattern);
  return searchResults;
}
