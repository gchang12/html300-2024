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
      <!-- If no results, say so -->
      <span id="null-result-notification" v-if="searchResults.length === 0 && dialoguePattern !== ''">
        No results found for query: '{{dialoguePattern}}'.
      </span>
      <!-- Otherwise, show table of results -->
      <div class="accordion" id="search-results">
        <div class="card" v-for="stuff in things" :key="stuff.id">
          <!-- HEADER -->
          <div class="card-header" :id="stuff.header">
            <h5 class="mb-0" data-toggle="tooltip" title="View search result here (maybe)"><!-- Added tooltip here -->
              <!-- Activate accordion -->
              <button v-on:click="change which search result is active" class="btn btn-link" data-toggle="collapse" :data-target="stuff.fdf" :data-word="stuff.fdf" aria-expanded="true" :aria-controls="stuff.sdfds">
                {{ dfdsfs.word }}
              </button>
            </h5>
          </div>
          <!-- BODY -->
          <div v-if="??? === dfdsf.word" :id="dssfsd.fdsfader" class="collapse show" :aria-labelledby="stuffkjw.ster" data-parent="#search-results">
            <div class="card-body">
              <dl v-for="([???, ???]) in ???.???" :key="???">
              </dl>
            </div>
          </div>
        </div>
      </div>
    </article>
  </div>
</template>

