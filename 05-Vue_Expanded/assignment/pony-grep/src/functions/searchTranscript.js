//import MiniSearch from "minisearch";

// All of G4
//import transcriptLines from "../constants/transcriptLines.js";
// MLP:FiM S1-S9
import transcriptLines from "../constants/smallTranscriptLines.js";

export default function searchTranscript(searchCriteria) {
  //const { isSung, seasonNo, episodeNo, dialoguePattern, speaker } = searchCriteria;
  //const { isSung, dialoguePattern, speaker } = searchCriteria;
  const { dialoguePattern, speaker } = searchCriteria;
  /*
  let miniSearch = new MiniSearch({
    idField: "id",
    fields: ["dialogue"],
    storeFields: ["id", "episodeId", "lineNo"],
  });
  */
  const speakerRegex = new RegExp(speaker, "i");
  const dialogueRegex = new RegExp(dialoguePattern, "i");
  //console.log(dialoguePattern, regex);
  const searchResults = transcriptLines.filter(lineEntry => {
    //const conditions = [];
    // check if lineEntry.speaker includes speaker
    if (speaker !== "") {
      if (!(speakerRegex.test(lineEntry.speaker))) {
        return false;
      }
    }
    // If isSung -> true, check if the speaker has brackets around; otherwise include everything.
    /*
    if (isSung != null) {
      if (!(lineEntry.speaker.startsWith("[") && lineEntry.speaker.endsWith("]"))) {
        return false;
      }
    } else {
      if (!(lineEntry.speaker.startsWith("[") && lineEntry.speaker.endsWith("]"))) {
        return false;
      }
    }
    */
    // if seasonNo is specified and so is episodeNo, limit results to entries with the specified episodeNo; otherwise include everything.
    /*
    if (seasonNo !== "") {
      if (!(lineEntry.seasonNo == seasonNo)) {
        return false;
      }
      if (episodeNo !== "") {
        if (!(lineEntry.episodeNo == episodeNo)) {
          return false;
        }
      }
    }
    */
    if (!dialogueRegex.test(lineEntry.dialogue)) {
      return false;
    }
    return true;
  });
  //miniSearch.addAll(filteredTranscriptLines);
  //console.log(regex.test("treetops"));
  return searchResults;
}
