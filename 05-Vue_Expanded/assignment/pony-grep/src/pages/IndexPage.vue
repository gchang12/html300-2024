<script setup>
  /* Landing Page */
  /* Image Page */
</script>

<template>
  <div id="index">
    <!-- Bootstrap: 'w-75' to make text within more compact and readable. -->
    <article class="container w-75">
      <h1>Welcome to <code>ponygrep</code>!</h1>
      <div class="WelcomeMessage">
        <p>Trying to remember something a MLP:FiM character might have said?</p>
        <p>You've come to the right place!
        <p><code>ponygrep</code> allows you to search all of MLP G4 for the bit of dialogue you're thinking of.</p>
      </div>
      <hr />
      <article class="container">
        <h2>Searching</h2>
        <section class="Usage-Example">
          <h3>Example</h3>
          <div class="Usage-Step d-flex">
            <!-- Bootstrap: 'img-thumbnail' for the image border. -->
            <img class="img-thumbnail" src="/images/search-form.png" />
            <ol class="m-5">
              <!-- Bootstrap: 'm-3' because the spaces between each line of instruction makes it more readable. -->
              <li class="Help m-3">&ldquo;I want to see if &lsquo;friendship is magic&rsquo; is said in MLP G4. I'll input <span class="_fieldValue">friendship is magic</span> into the <span class="_fieldName">Dialogue</span> box now.&rdquo;</li>
              <li class="Help m-3">&ldquo;I want to see if Discord or Twilight says it. I'll input <span class="_fieldValue">Discord|Twilight</span> into the <span class="_fieldName">Character</span> field.&rdquo;</li> 
              <li class="Help m-3">&ldquo;Let's see if either Discord or Twilight say &lsquo;friendship is magic&rsquo; by hitting the <span class="_fieldName">Search</span> button.&rdquo;</li>
            </ol>
          </div>
        </section>
      </article>
      <hr />
      <article class="BrowsingTranscripts w-75 container">
        <h2>Browsing Transcripts</h2>
        <hr />
        <section class="BrowsingStep">
          <h3>1. Select Season</h3>
          <img width="500px" class="img-thumbnail" src="/images/season-index.png" />
        </section>
        <hr />
        <section class="BrowsingStep">
          <h3>2. Select Episode</h3>
          <img width="500px" class="img-thumbnail" src="/images/episode-index.png" />
        </section>
        <hr />
        <section class="BrowsingStep">
          <h3>3. Scroll Down and View</h3>
          <img width="500px" class="img-thumbnail" src="/images/transcript.png" />
        </section>
        <hr />
        <section class="BrowsingStep">
          <h3>4. Close Transcript</h3>
          <img width="500px" class="img-thumbnail" src="/images/close-transcript.png" />
        </section>
        <hr />
      </article>
    </article>
  </div>
</template>

<!-- NOTE: For possible recycling. Ignore, please! -->

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
