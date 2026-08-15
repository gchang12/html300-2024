<script setup>

  import { ref } from "vue";

  //import searchTranscript from "../functions/searchTranscript.js";

  const searchResults = ref([]);
  const dialoguePattern = ref("");

</script>

<template>
  <div id="transcript-search">
    <article>
      <h1>Search Transcripts</h1>
      <p>(Brief explanation of what this is and how to use this)</p>
      <form>
        <fieldset>
          <label>
            Pattern
            <input type="text" name="dialoguePattern" required />
          </label>
          <label>
            Is sung line?
            <input type="checkbox" name="isSung" />
          </label>
        </fieldset>
        <label>
          Character
          <input type="text" name="speaker" />
        </label>
        <fieldset>
          <label>
            Season
            <input min="1" max="9" type="number" name="seasonNo" />
          </label>
          <label>
            Episode
            <input min="1" max="26" type="number" name="episodeNo" />
          </label>
        </fieldset>
        <button type="button">Search</button>
      </form>
      <span id="null-result-notification" v-if="searchResults.length === 0 && dialoguePattern !== ''">
        No results found for query: '{{dialoguePattern}}'.
      </span>
      <!-- If no results, say so -->
      <!-- Otherwise, show table of results -->
    </article>
  </div>
</template>

