<script setup>

  import { ref } from "vue";

  import episodeList from "../constants/episodeList.js";
  import transcriptLines from "../constants/transcriptLines.js";

  const currentEpisode = ref({});
  const activeSeason = ref(-1);

  /*
  function setSeason(e) {
    console.log(e);
    const seasonNo = e.target.dataset.season;
    if (activeSeason.value !== seasonNo) {
      activeSeason.value = seasonNo;
    } else {
      activeSeason.value = -1;
    }
  }
  */

  // TODO: Use for all episode transcript directories and leverage urlParams
  function selectEpisode(e) {
    const id = e.currentTarget.dataset.id;
    currentEpisode.value = episodeList.find(episode => episode.id == id);
  }

</script>

<template>
  <div id="episode-directory">
    <h1>Transcript Viewer</h1>
    <div class="container">
      <div class="row">
        <div class="col">
          <h2>Index</h2>
          <aside class="EpisodeIndex">
            <h3>MLP:FiM</h3>
            <ol>
              <li class="SeasonList" v-for="season in [1, 2, 3, 4, 5, 6, 7, 8, 9]" :key="season">
                <a :href="'/#/transcripts/FiM/S' + season">
                  S{{ season }}
                </a>
                <ol v-if="activeSeason == season" class="season">
                  <li class="episode" v-for="episode in episodeList.filter(episode => episode.seasonNo === season)" :key="episode.id">
                    <button @click="selectEpisode" :data-id="episode.id">
                      {{ episode.title }}
                    </button>
                  </li>
                </ol>
              </li>
            </ol>
          </aside>
        </div>
        <div class="col">
          <main class="transcript">
            <h2>Transcript</h2>
            <div class="content" v-if="Object.keys(currentEpisode).length !== 0">
              <h3>S{{ currentEpisode.seasonNo }} E{{ currentEpisode.episodeNo }} – {{currentEpisode.title }}</h3>
              <table>
                <thead>
                  <tr>
                    <th>Character</th>
                    <th>Line</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="transcriptLine in transcriptLines.filter(transcriptLine => transcriptLine.episodeId === currentEpisode.id)" :key="transcriptLine.id">
                    <th>
                      {{ transcriptLine.speaker }}
                    </th>
                    <td>
                      {{ transcriptLine.dialogue }}
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </main>
        </div>
        <div class="col">
          <aside class="current-episode-info">
            <h2>Episode Info</h2>
            <div v-if="Object.keys(currentEpisode).length !== 0">
              <table>
                <tbody>
                  <tr>
                    <th>Season</th>
                    <td>{{currentEpisode.seasonNo}}</td>
                  </tr>
                  <tr>
                    <th>Episode</th>
                    <td>{{currentEpisode.episodeNo}}</td>
                  </tr>
                  <tr>
                    <th>Airdate</th>
                    <td>{{ currentEpisode.airdate }}</td>
                  </tr>
                </tbody>
              </table>
              <p v-for="line in currentEpisode.summary" :key="line">{{ line }}</p>
              <a :href="'https://mlp.fandom.com/wiki/' + currentEpisode.urlName">MLP Wikia Page</a>
            </div>
          </aside>
        </div>
      </div>
    </div>
  </div>
</template>
