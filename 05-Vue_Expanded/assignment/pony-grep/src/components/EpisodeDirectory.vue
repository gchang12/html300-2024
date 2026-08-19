<script setup>

  import { ref } from "vue";

  import episodeList from "../constants/episodeList.js";
  import transcriptLines from "../constants/transcriptLines.js";

  const currentEpisode = ref({});
  //const currentEpisode = ref(episodeList.find(() => true));
  const activeSeason = ref(-1);

  const seasonImages = [
    {
      seasonNo: 1,
      imgName: "My_Little_Pony_Theme_Song.webp"
    },
    {
      seasonNo: 2,
      imgName: "My_Little_Pony_Theme_Song.webp"
    },
    {
      seasonNo: 3,
      imgName: "My_Little_Pony_Theme_Song.webp"
    },
    {
      seasonNo: 4,
      imgName: "Photo_Finish_taking_photo_S4_Opening.webp"
    },
    {
      seasonNo: 5,
      imgName: "Photo_Finish_taking_photo_S4_Opening.webp"
    },
    {
      seasonNo: 6,
      imgName: "Photo_Finish_taking_photo_S6_opening.webp"
    },
    {
      seasonNo: 7,
      imgName: "Photo_Finish_taking_photo_S7_opening.webp"
    },
    {
      seasonNo: 8,
      imgName: "Photo_Finish_taking_the_class_photo_S8_opening.webp"
    },
    {
      seasonNo: 9,
      imgName: "Photo_Finish_taking_the_class_photo_S8_opening.webp"
    },
  ];

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
    if (id == currentEpisode.value.id) {
      currentEpisode.value = {};
    } else {
      currentEpisode.value = episodeList.find(episode => episode.id == id);
    }
    alert("Scroll down for the transcript of S" + currentEpisode.value.seasonNo + " E" + currentEpisode.value.episodeNo + ", '" + currentEpisode.value.title + "'.");
    //e.currentTarget.classList.add("");
  }

</script>

<template>
  <div id="episode-directory">
    <h1>Transcript Viewer</h1>
    <article class="d-flex align-items-center flex-column">
      <h2>Instructions</h2>
      <ol class="w-25">
        <li>Select season from index.</li>
        <li>Select episode from episode index.</li>
        <li>Scroll down and view transcript.</li>
        <li>Select episode again to close the transcript.</li>
      </ol>
    </article>

    <div class="container">
      <div class="row">
        <div class="col-3">
          <!-- <div v-if="seasonNo == activeSeason"> Active Season: {{ activeSeason }} </div> -->
          <!-- <ol class="dropdown-menu" v-if="seasonNo == activeSeason"> -->
          <article>
            <h2>Episode List</h2>
            <article v-if="activeSeason != -1">
              <h3>Season {{ activeSeason }}</h3>
              <ol class="EpisodeList">
                <li v-for="episode in episodeList.filter(episode => episode.seasonNo == activeSeason)" :data-id="episode.id" @click="selectEpisode" :key="episode.id">
                  <!-- <a role="button" class="dropdown-item"> -->
                  <a class="EpisodeEntry" role="button">
                    <!-- <button class="btn btn-secondary">E{{ episode.episodeNo }}</button>{{ episode.title }} -->
                    <button class="btn btn-secondary">E{{ episode.episodeNo }}</button> {{ episode.title }}
                    <!-- E{{ episode.episodeNo }} {{ episode.title }} -->
                  </a>
                </li>
              </ol>
            </article>
          </article>
        </div>
        <div class="col">
          <h2>Index</h2>
          <aside id="mlp-fim" class="EpisodeIndex">
            <h3>MLP:FiM</h3>
            <ol class="navbar-nav">
              <!-- <li class="nav-item dropdown" v-for="seasonNo in [1, 2, 3, 4, 5, 6, 7, 8, 9]" :key="seasonNo"> -->
              <li class="nav-item" v-for="seasonImage in seasonImages" :key="seasonImage.seasonNo">
                <!-- <a class="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-expanded="false"> -->
                <figure>
                  <img :src="'/images/' + seasonImage.imgName" class="img-thumbnail" />
                  <figcaption>
                    <a class="nav-link" role="button">
                      <!-- TODO: Dropdown not working. Temporary fix. -->
                      <button class="btn btn-block btn-primary" :data-season="seasonImage.seasonNo" @click="setSeason">
                        S{{seasonImage.seasonNo}}
                      </button>
                    </a>
                  </figcaption>
                </figure>
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
