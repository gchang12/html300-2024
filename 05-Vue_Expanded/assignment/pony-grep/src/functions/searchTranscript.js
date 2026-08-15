import MiniSearch from "minisearch";

import transcriptLines from "../constants/transcriptLines.js";

export default function searchTranscript(searchCriteria) {
  const { isSung, seasonNo, episodeNo, dialoguePattern, speaker } = searchCriteria;
  let miniSearch = new MiniSearch({
    //fields: ["seasonNo", "episodeNo", "dialogue", "speaker"],
    idField: "id",
    fields: ["dialogue"],
    storeFields: ["id", "episodeId", "lineNo"],
  });
  //console.log(typeof isSung, typeof seasonNo, typeof episodeNo, typeof speaker);
  const filteredTranscriptLines = transcriptLines.filter(lineEntry => {
    if (lineEntry.speaker == null) {
      return false;
    }
    const conditions = [];
    //lineEntry;
    // Limiting results to entries that include the speaker
    // if speaker is null, lineEntry.speaker should be null too; otherwise lineEntry
    // if speaker is null, true
    // otherwise check if lineEntry.speaker includes speaker
    if (speaker !== "") {
      conditions.push(lineEntry.speaker != null && lineEntry.speaker.includes(speaker));
    }
    // If isSung -> true, check if the speaker has brackets around; otherwise include everything.
    //conditions.push(isSung == null || 
    if (isSung != null) {
      conditions.push(lineEntry.speaker != null && lineEntry.speaker.startsWith("[") && lineEntry.speaker.endsWith("]"));
    }
    if (seasonNo !== "") {
      conditions.push(lineEntry.seasonNo == seasonNo);
      if (episodeNo !== "") {
        conditions.push(lineEntry.episodeNo == episodeNo);
      }
    }
    // if seasonNo is specified, limit results to entries with that seasonNo; otherwise include everything
    //conditions.push(seasonNo == null || seasonNo === lineEntry.seasonNo);
    // if seasonNo is specified and so is episodeNo, limit results to entries with the specified episodeNo; otherwise include everything.
    //conditions.push(seasonNo == null || episodeNo == null || episodeNo === lineEntry.episodeNo);
    return conditions.every((condition) => condition === true);
  });
  //console.log(filteredTranscriptLines);
  miniSearch.addAll(filteredTranscriptLines);
  const searchResults = miniSearch.search(dialoguePattern);
  return searchResults;
}
