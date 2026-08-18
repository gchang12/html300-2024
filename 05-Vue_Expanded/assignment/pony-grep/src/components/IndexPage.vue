<script setup>
  //import { ref } from "vue";

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

</script>

<template>
  <div class="vue-container" id="index">
    <article>
      <h1>Search for a Line in the Dialogue of Every Episode in MLP:FiM Here, at Pony <code>grep</code>!</h1>
      <!-- <article> -->
      <!-- <h2>About Us</h2> -->
      <!-- <p>Trying to remember a line that a children's cartoon horse might have said? This is the perfect tool for finding that out!  This website scans every dialogue of if a character from <i>My Little Pony: Friendship is Magic</i> and checks if any character in this show ever said the thing you queried.  Just go on over to <a href="#/">Search</a> and input your query.</p> -->
      <!-- </article> -->
      <article>
        <h2>Episode Directory</h2>
        <!-- <p>Wanna just read the transcripts and re-experience the magic of friendship through the magic of reading? Head on over to our <a href="#/transcripts">Transcripts</a> directory!</p> -->
        <article id="mlp-fim">
          <h3>MLP:FiM</h3>
          <div class="seasons">
            <a :href="'#/transcripts/FiM/S' + seasonImage.seasonNo" v-for="seasonImage in seasonImages" :key="seasonImage.seasonNo">
              <figure>
                <img :src="'/images/' + seasonImage.imgName" />
                <figcaption>S{{ seasonImage.seasonNo }}</figcaption>
              </figure>
            </a>
          </div>
        </article>
      </article>
    </article>
  </div>
</template>

