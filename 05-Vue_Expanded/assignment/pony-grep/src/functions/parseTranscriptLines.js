import transcriptLines from "../constants/transcriptLines.js";
import episodeList from "../constants/episodeList.js";

export default function parseTranscriptLines(searchResults) {
  // searchResults: Array<{episodeId, lineNo}>
  const parsedTranscriptLines = [];
  // get 'title', 'seasonNo', and 'episodeNo' fields.
  // for each [episodeId, lineNo] in searchResults:
  // - fetch episode.title, episode.seasonNo, episode.episodeNo
  // - fetch transcript lines within threshold
  const contextLength = 2;
  for (const searchResult of searchResults) {
    const { title, seasonNo, episodeNo } = episodeList.find(episode => episode.id === searchResult.episodeId);
    // get context lines within radius two of targeted line
    const contextLines = transcriptLines.filter(transcriptLine => {
      return (
        transcriptLine.episodeId === searchResult.episodeId
        && Math.abs(transcriptLine.lineNo - searchResult.lineNo) <= contextLength
      );
    });
    parsedTranscriptLines.push(
      // desired fields
      {
        id: searchResult.id,
        title,
        seasonNo,
        episodeNo,
        lineNo: searchResult.lineNo,
        contextLines,
        isShown: false,
      }
    );
  }
  /* TODO: Figure out how to sort results.
  parsedTranscriptLines.sort((a, b) => a.lineNo - b.lineNo);
  parsedTranscriptLines.sort((a, b) => a.seasonNo - b.seasonNo);
  parsedTranscriptLines.sort((a, b) => a.episodeNo - b.episodeNo);
  */
  return parsedTranscriptLines;
}
