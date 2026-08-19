<script setup>

  import { ref } from "vue";

  import episodeList from "../constants/episodeList.js";
  import transcriptLines from "../constants/transcriptLines.js";

  //const currentEpisode = ref({});
  const currentEpisode = ref(episodeList.find(() => true));
  const activeSeason = ref(-1);

  function setSeason(e) {
    //console.log(e);
    const seasonNo = e.currentTarget.dataset.season;
    if (activeSeason.value != seasonNo) {
      activeSeason.value = seasonNo;
    } else {
      activeSeason.value = -1;
    }
    console.log(activeSeason);
  }

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
          <aside id="mlp-fim" class="EpisodeIndex">
            <h3>MLP:FiM</h3>
            <ol class="navbar-nav">
              <!-- <li class="nav-item dropdown" v-for="seasonNo in [1, 2, 3, 4, 5, 6, 7, 8, 9]" :key="seasonNo"> -->
              <li class="nav-item" v-for="seasonNo in [1, 2, 3, 4, 5, 6, 7, 8, 9]" :key="seasonNo">
                <!-- <a class="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-expanded="false"> -->
                <a class="nav-link" role="button">
                  <!-- TODO: Dropdown not working. Temporary fix. -->
                  <button class="btn btn-primary" :data-season="seasonNo" @click="setSeason">
                    S{{seasonNo}}
                  </button>
                </a>
                <!-- <div v-if="seasonNo == activeSeason"> Active Season: {{ activeSeason }} </div> -->
                <!-- <ol class="dropdown-menu" v-if="seasonNo == activeSeason"> -->
                <ol class="EpisodeList" v-if="seasonNo == activeSeason">
                  <li :data-id="episode.id" @click="selectEpisode" v-for="episode in episodeList.filter(episode => episode.seasonNo == seasonNo)" :key="episode.id">
                    <!-- <a role="button" class="dropdown-item"> -->
                    <a class="EpisodeEntry" role="button">
                      <!-- <button class="btn btn-secondary">E{{ episode.episodeNo }}</button>{{ episode.title }} -->
                      <button class="btn btn-secondary">E{{ episode.episodeNo }}</button> {{ episode.title }}
                      <!-- E{{ episode.episodeNo }} {{ episode.title }} -->
                    </a>
                  </li>
                </ol>
              </li>
            </ol>
          </aside>
        </div>
      </div>

      <div class="row">
        <div class="col">
          <main class="Transcript">
            <h2>Transcript</h2>
            <div class="content" v-if="Object.keys(currentEpisode).length !== 0">
              <table class="table table-light table-striped">
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

        <div class="col-3">
          <aside class="EpisodeInfo">
            <h2>Episode Info</h2>
            <div v-if="Object.keys(currentEpisode).length !== 0">
              <h3>{{currentEpisode.title }}</h3>
              <table class="table table-light">
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
