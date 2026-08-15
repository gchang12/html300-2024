<script setup>

  import { ref } from "vue";

  import searchTranscript from "../functions/searchTranscript.js";
  import parseTranscriptLines from "../functions/parseTranscriptLines.js";

  let searchResults = ref([]);
  const dialoguePattern = ref("");
  function searchAndParseResults(e) {
    //console.log(e);
    //console.log(typeof e);
    //console.log(e.target.form);
    const formData = new FormData(e.target.form);
    //console.log(formData);
    const searchCriteria = Object.fromEntries(formData.entries());
    const fetchedSearchResults = searchTranscript(searchCriteria);
    //console.log(fetchedSearchResults);
    const parsedSearchResults = parseTranscriptLines(fetchedSearchResults);
    //console.log(parsedSearchResults);
    searchResults.value = parsedSearchResults;
  }

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
        <button @click="searchAndParseResults" type="button">Search</button>
      </form>
      <!-- If no results, say so -->
      <span id="null-result-notification" v-if="searchResults.length === 0 && dialoguePattern !== ''">
        No results found for query: '{{dialoguePattern}}'.
      </span>
      <div v-if="searchResults.length > 0">
        {{ searchResults.length }}
      </div>
      <!-- Otherwise, show table of results -->
    </article>
  </div>
</template>

