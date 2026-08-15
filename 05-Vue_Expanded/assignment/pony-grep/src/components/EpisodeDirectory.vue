
<script setup>
  import { ref } from "vue";

  import episodeList from "../constants/episodeList.js";
  import transcriptLines from "../constants/transcriptLines.js";
  const currentEpisode = ref({});

  function selectEpisode(e) {
    const id = e.currentTarget.dataset.id;
    //console.log(id);
    currentEpisode.value = episodeList.find(episode => episode.id == id);
    //console.log(currentEpisode.value);
  }

</script>

<template>
  <div class="vue-container" id="episode-directory">
    <h1><i>My Little Pony: Friendship is Magic</i> (An Episode Directory)</h1>
    <div class="content">
      <aside class="episode-index">
        <div class="index-container" v-for="season in [1, 2, 3, 4, 5, 6, 7, 8, 9]" :key="season.id">
          <h2>Season {{ season }}</h2>
          <ol class="season">
            <li class="episode" v-for="episode in episodeList.filter(episode => episode.seasonNo === season)" :key="episode.id">
              <button @click="selectEpisode" :data-id="episode.id">
                <h3>Episode {{episode.episodeNo}}: {{ episode.title }}</h3>
              </button>
            </li>
          </ol>
        </div>
      </aside>
      <main class="transcript">
        <table v-if="Object.keys(currentEpisode).length !== 0">
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
        TRANSCRIPT HERE
      </main>
      <aside class="current-episode-info">
        <div v-if="Object.keys(currentEpisode).length !== 0">
          <article>
            <h2>Season: {{currentEpisode.seasonNo}}</h2>
            <article>
              <h3>Episode: {{currentEpisode.episodeNo}}</h3>
              <span class="airdate">Airdate: {{ currentEpisode.airdate }}</span>
              <section>
                <h4>Summary</h4>
                <p v-for="line in currentEpisode.summary" :key="line">{{ line }}</p>
              </section>
              <p>Still need more info? Visit <a :href="'https://mlp.fandom.com/wiki/' + currentEpisode.urlName">https://mlp.fandom.com/wiki/{{ currentEpisode.urlName }}</a></p>
            </article>
          </article>
        </div>
      </aside>
    </div>
  </div>
</template>
