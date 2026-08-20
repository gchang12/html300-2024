<script setup>
  /* Image Page */
  /* Grid System Page */
  /* Tooltip Page */

  import { ref } from "vue";

  // All of G4
  //import episodeList from "../constants/animationIndex.js";
  //import transcriptLines from "../constants/transcriptLines.js";

  import episodeList from "../constants/episodeList.js";
  import transcriptLines from "../constants/smallTranscriptLines.js";

  const currentEpisode = ref({});
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
    const seasonNo = e.currentTarget.dataset.season;
    if (activeSeason.value != seasonNo) {
      activeSeason.value = seasonNo;
    } else {
      activeSeason.value = -1;
    }
    console.log(activeSeason);
  }

  function selectEpisode(e) {
    const id = e.currentTarget.dataset.id;
    if (id == currentEpisode.value.id) {
      currentEpisode.value = {};
    } else {
      currentEpisode.value = episodeList.find(episode => episode.id == id);
    }
  }

</script>

<template>
  <div id="episode-directory">
    <h1>Transcripts</h1>
    <!-- Bootstrap: 'container' to give content padding within root container. -->
    <div class="container">
      <!-- Bootstrap: 'row' to set up Grid System layout. 2 rows, 2 columns.
        (Seasons, Episodes)
        (Transcript, Episode Info)
      -->

      <div class="row">

        <div class="col">
          <h2>Seasons</h2>
          <aside id="mlp-fim" class="EpisodeIndex">
            <h3>MLP:FiM</h3>
            <!-- Bootstrap: 'navbar-nav' for soon-to-be-added dropdown support -->
            <ol class="navbar-nav">
              <li class="nav-item" v-for="seasonImage in seasonImages" :key="seasonImage.seasonNo">
                <!-- TODO:
                  For the image page, convert the image markup into a separate component in its own file, be sure to import it into the corresponding 'page' component
                  The image component should have props for at least the image src, alt, & title attributes, use prop validation.
                  Create a mixin for the image component that should toggle on/off a border around the image on click, apply the mixin to the image component.
                -->
                <!-- Bootstrap: 'btn' to remove default button styling and especially for zero-opacity -->
                <button class="btn" :data-season="seasonImage.seasonNo" @click="setSeason">
                  <figure>
                    <img :src="'/images/' + seasonImage.imgName" class="img-thumbnail" />
                    <figcaption>
                      <a class="nav-link" role="button">
                        <!-- NOTE: Dropdown not working. Temporary fix. -->
                        <!-- Bootstrap: 'btn-block' to make button width span container width -->
                        <button class="btn btn-block btn-primary">
                          S{{seasonImage.seasonNo}}
                        </button>
                      </a>
                    </figcaption>
                  </figure>
                </button>
              </li>
            </ol>
          </aside>
        </div>

        <!-- Bootstrap: 'col-2' because episode buttons don't need much width -->
        <div class="col-2">
          <article>
            <h2>Episodes</h2>
            <div class="EpisodeList">
              <article class="container" v-if="activeSeason != -1">
                <h3>S{{ activeSeason }}</h3>
                <!-- TODO: Dropdown not working. Temporary fix. -->
                <ol>
                  <li v-for="episode in episodeList.filter(episode => episode.seasonNo == activeSeason)" :data-id="episode.id" @click="selectEpisode" :key="episode.id">
                    <a class="EpisodeEntry" role="button">
                      <!-- Bootstrap: 'btn-secondary' to indicate that episodes are secondary wrt seasons; also for the background color -->
                      <button :title="episode.title" class="btn btn-secondary">E{{ episode.episodeNo }}</button>
                    </a>
                  </li>
                </ol>
              </article>
            </div>
          </article>
        </div>

      </div>

      <!-- NOTE: Technically, this is its own page, but I couldn't make it so due to technical limitations. -->
      <div class="row EpisodeData">

        <div class="col-3">
          <aside class="EpisodeInfo">
            <div v-if="Object.keys(currentEpisode).length !== 0">
              <h3>{{currentEpisode.title }}</h3>
              <!-- Bootstrap: 'table' for sensible defaults, and 'table-light' for visibility. -->
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
              <a class="External" target="_blank" :href="'https://mlp.fandom.com/wiki/' + currentEpisode.urlName">MLP Wikia Page</a>
            </div>
          </aside>
        </div>

        <div class="col">
          <main class="Transcript">
            <div class="content" v-if="Object.keys(currentEpisode).length !== 0">
              <!-- Bootstrap: 'table-striped' to distinguish between consecutive lines of dialogue. -->
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

      </div>

    </div>
  </div>
</template>
