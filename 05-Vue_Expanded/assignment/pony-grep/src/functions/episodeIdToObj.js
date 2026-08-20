//import episodeList from "../constants/animationIndex.js";
import episodeList from "../constants/episodeList.js";

export default function episodeIdToObj(episodeId) {
  //console.log(episodeId, typeof episodeId);
  //console.log(episodeList);
  const {id, seasonNo, episodeNo, title} = episodeList.find(episode => episode.id === episodeId);
  return {
    id,
    seasonNo,
    episodeNo,
    title,
  };
}

