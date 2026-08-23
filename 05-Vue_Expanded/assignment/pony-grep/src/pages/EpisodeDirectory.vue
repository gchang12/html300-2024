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

  import ImageButton from "../components/ImageButton.vue";
  import LinkButton from "../components/LinkButton.vue";

  const currentEpisode = ref({});
  const activeSeason = ref(-1);

  const seasonImages = [
    {
      seasonNo: 1,
      imgName: "My_Little_Pony_Theme_Song.webp",
      alt: "MLP Opening Cinematic (1st)"
    },
    {
      seasonNo: 2,
      imgName: "My_Little_Pony_Theme_Song.webp",
      alt: "MLP Opening Cinematic (1st)"
    },
    {
      seasonNo: 3,
      imgName: "My_Little_Pony_Theme_Song.webp",
      alt: "MLP Opening Cinematic (1st)"
    },
    {
      seasonNo: 4,
      imgName: "Photo_Finish_taking_photo_S4_Opening.webp",
      alt: "MLP Opening Cinematic (2nd, with Twilight as alicorn)"
    },
    {
      seasonNo: 5,
      imgName: "Photo_Finish_taking_photo_S4_Opening.webp",
      alt: "MLP Opening Cinematic (2nd, with Twilight as alicorn)"
    },
    {
      seasonNo: 6,
      imgName: "Photo_Finish_taking_photo_S6_opening.webp",
      alt: "MLP Opening Cinematic (3rd, with nervous Starlight)"
    },
    {
      seasonNo: 7,
      imgName: "Photo_Finish_taking_photo_S7_opening.webp",
      alt: "MLP Opening Cinematic (3rd, with happy Starlight)"
    },
    {
      seasonNo: 8,
      imgName: "Photo_Finish_taking_the_class_photo_S8_opening.webp",
      alt: "MLP Opening Cinematic (4th, class photo at School of Friendship)"
    },
    {
      seasonNo: 9,
      imgName: "Photo_Finish_taking_the_class_photo_S8_opening.webp",
      alt: "MLP Opening Cinematic (4th, class photo at School of Friendship)"
    },
  ];

  function setSeason(e) {
    const seasonNo = e.currentTarget.dataset.season;
    if (activeSeason.value != seasonNo) {
      activeSeason.value = seasonNo;
    } else {
      activeSeason.value = -1;
    }
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
                <ImageButton
                    :src="'/images/' + seasonImage.imgName"
                    :alt="seasonImage.alt"
                    :title="'View episodes for Season ' + seasonImage.seasonNo"
                    :data-season="seasonImage.seasonNo" 
                    :onClick="setSeason"
                    :captionText="'S' + seasonImage.seasonNo"
                    />
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
                <!-- TODO: Cannot figure out how to implement dropdown. Temporary fix. -->
                <ol>
                  <li v-for="episode in episodeList.filter(episode => episode.seasonNo == activeSeason)" :data-id="episode.id" @click="selectEpisode" :key="episode.id">
                    <LinkButton
                        :title="episode.title"
                        :captionText="'E' + episode.episodeNo"
                        />
                  </li>
                </ol>
              </article>
            </div>
          </article>
        </div>

      </div>

      <!-- NOTE: Technically, this is its own page, but I couldn't make it so due to technical limitations.
        i.e. in 'src/App.vue' I'd have to extend 'routes' to include about 200 entries.
      -->
      <div class="row EpisodeData">

        <div class="col col-3">
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
            <span v-else>
              Transcript appears here after selecting a season and an episode.
            </span>
          </main>
        </div>

      </div>

    </div>
  </div>
</template>
