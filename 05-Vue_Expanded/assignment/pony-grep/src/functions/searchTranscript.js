import MiniSearch from "minisearch";

import transcriptLines from "../constants/transcriptLines.js";

export function searchTranscript(searchCriteria) {
  const { isSung, seasonNo, episodeNo, dialoguePattern, speaker } = searchCriteria;
  let miniSearch = new MiniSearch({
    //fields: ["seasonNo", "episodeNo", "dialogue", "speaker"],
    idField: "id",
    fields: ["dialogue"],
    storeFields: ["episodeId", "lineNo"],
  });
  const filteredTranscriptLines = transcriptLines.filter(lineEntry => {
    const conditions = [];
    // Limiting results to entries that include the speaker
    conditions.push(lineEntry.speaker.includes(speaker));
    // If isSung -> true, check if the speaker has brackets around; otherwise include everything.
    conditions.push(isSung == false || lineEntry.speaker.startsWith("[") && lineEntry.speaker.endsWith("]"));
    // if seasonNo is specified, limit results to entries with that seasonNo; otherwise include everything
    conditions.push(seasonNo == null || seasonNo === lineEntry.seasonNo);
    // if seasonNo is specified and so is episodeNo, limit results to entries with the specified episodeNo; otherwise include everything.
    conditions.push(seasonNo == null || episodeNo == null || episodeNo === lineEntry.episodeNo);
    return conditions.every((condition) => condition === true);
  });
  miniSearch.addAll(filteredTranscriptLines);
  const results = miniSearch.search(dialoguePattern);
  return results;
}
