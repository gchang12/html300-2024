<script setup>
  import { ref } from "vue";

  const selectedSeason = ref(-1);
  const selectedSeasonImage = ref("");
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

  function selectSeason(e) {
    // add CSS class for highlighting
    e.currentTarget.classList.add("selected");
    //console.log(e.currentTarget);
    const season = e.currentTarget.dataset.season;
    // change season
    selectedSeason.value = Number(season);
    // change image source
    selectedSeasonImage.value = seasonImages.find(seasonImage => seasonImage.seasonNo == season).imgName;
    //console.log(selectedSeasonImage);
  }

  function deselectSeason(e) {
    // add CSS class for highlighting
    e.currentTarget.classList.remove("selected");
    // change season
    selectedSeason.value = -1;
    // change image source
    selectedSeasonImage.value = "My_Little_Pony_Theme_Song.webp";
    //console.log(selectedSeasonImage);
  }

</script>

<template>
  <div class="vue-container" id="index">
    <article>
      <h1>Welcome to Pony <code>grep</code>!</h1>
      <article>
        <h2>About Us</h2>
        <p>Trying to remember a line that a children's cartoon horse might have said? This is the perfect tool for finding that out!</p>
        <p>This website scans every dialogue of if a character from <i>My Little Pony: Friendship is Magic</i> and checks if any character in this show ever said the thing you queried.</p>
        <p>Just go on over to <a href="#/transcriptSearch">Transcript Search</a> and input your query.</p>
      </article>
      <article>
        <h2>Episode Directory</h2>
        <p>Wanna just read the transcripts and re-experience the magic of friendship through the magic of reading? Head on over to our <a href="#/episodeDirectory">Episode Directory</a>!</p>
      </article>
      <!-- <article> -->
        <!-- <h2>Dossier</h2> -->
        <!-- <p>Wanna find out which episodes your favorite characters have appeared in, stood silently in, and made cameos in? We've compiled a list, just for you! Find the aforementioned list in our <a href="#/dossier">Dossier</a>!</p> -->
        <!-- <p>Wanna find out which episodes your favorite characters have appeared in, stood silently in, and made cameos in? We've compiled a list, just for you! Find the aforementioned list in our <a href="#/dossier">Dossier</a>!</p> -->
        <!-- </article> -->
      <article class="episode-jumper">
        <h2>Jump to an Episode Now! (WIP)</h2>
        <figure>
          <img v-if="selectedSeason > 0" :src="'/images/' + selectedSeasonImage" />
          <img v-else src="/images/My_Little_Pony_Theme_Song.webp" />
          <figcaption v-if="selectedSeason > 0">Season {{ selectedSeason }}</figcaption>
        </figure>
        <div id="season-selector">
          <div class="container">
            <div class="row" v-for="number in [0, 3, 6]" :key="number">
              <div @mouseleave="deselectSeason" @mouseover="selectSeason" :data-season="seasonImage.seasonNo" class="col-2" v-for="seasonImage in seasonImages.slice(number, number + 3)" :key="seasonImage.seasonNo">
                <!-- NOTE: Not functional yet! -->
                <!-- <a :href="'/#/episodeDirectory/S' + seasonImage.seasonNo">S{{ seasonImage.seasonNo }}</a> -->
                <a>S{{ seasonImage.seasonNo }}</a>
              </div>
            </div>
          </div>
        </div>
      </article>
    </article>
  </div>
</template>

