<script setup>
  //import { ref } from "vue";

  /*
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
  */

</script>

<template>
  <div id="index">
    <article class="container w-50">
      <h1>Welcome to <code>ponygrep</code>!</h1>
      <section>
        <h2>About Us</h2>
        <p>Trying to remember if a MLP:FiM character said something?</p>
        <p>You've come to the right place!
        <p><code>ponygrep</code> allows you to search all of MLP G4 for the bit of dialgoue you're thinking of.</p>
        <article class="w-75 container">
          <h2>Searching</h2>
          <section>
            <h3>Example</h3>
            <ol>
              <li class="Help">&ldquo;I want to see if &lsquo;friendship is magic&rsquo; is said in MLP G4. I'll input <span class="_fieldValue">friendship is magic</span> into the <span class="_fieldName">Dialogue</span> box now.&rdquo;</li>
              <li class="Help">&ldquo;I want to see if Discord or Twilight says it. I'll input <span class="_fieldValue">Discord|Twilight</span> into the <span class="_fieldName">Character</span> field.&rdquo;</li> 
              <li class="Help">&ldquo;Let's see if either Discord or Twilight say &lsquo;friendship is magic&rsquo; by hitting the <span class="_fieldName">Search</span> button.&rdquo;</li>
            </ol>
          </section>
        </article>
        <article class="w-75 container">
          <h2>Browsing Transcripts</h2>
          <section class="d-flex align-items-center flex-column">
            <h3>Instructions</h3>
            <ol>
              <li>Select season from index.</li>
              <li>Select episode from episode index.</li>
              <li>Scroll down and view transcript.</li>
              <li>Select episode again to close the transcript.</li>
            </ol>
          </section>
        </article>
      </section>
      <!-- <article> -->
      <!-- <p>Trying to remember a line that a children's cartoon horse might have said? This is the perfect tool for finding that out!  This website scans every dialogue of if a character from <i>My Little Pony: Friendship is Magic</i> and checks if any character in this show ever said the thing you queried.  Just go on over to <a href="#/">Search</a> and input your query.</p> -->
      <!-- </article> -->
      <!-- <article> -->
      <!-- <h2>Episode Directory</h2> -->
        <!-- <p>Wanna just read the transcripts and re-experience the magic of friendship through the magic of reading? Head on over to our <a href="#/transcripts">Transcripts</a> directory!</p> -->
        <!-- <article id="mlp-fim"> -->
        <!-- <h3>MLP:FiM</h3> -->
        <!-- <div class="seasons"> -->
        <!-- <a :href="'#/transcripts/FiM/S' + seasonImage.seasonNo" v-for="seasonImage in seasonImages" :key="seasonImage.seasonNo"> -->
        <!-- <figure> -->
        <!-- <img :src="'/images/' + seasonImage.imgName" /> -->
        <!-- <figcaption>S{{ seasonImage.seasonNo }}</figcaption> -->
        <!-- </figure> -->
              <!-- </a> -->
              <!-- </div> -->
              <!-- </article> -->
              <!-- </article> -->
    </article>
  </div>
</template>

