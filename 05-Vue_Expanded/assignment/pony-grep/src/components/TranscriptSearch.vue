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
      <div class="accordion" v-if="searchResults.length > 0">
        <thead>
          <tr>
            <th>Episode</th>
            <th>Character</th>
            <th>Line</th>
          </tr>
        </thead>
        <!-- Implemented accordion content structure here. -->
        <div class="card" v-for="searchResult in searchResults" :key="definition.word">
          <div class="card-header" :id="definition.cardHeader">
            <!-- NOTE: Added tooltip here! -->
            <h5 class="mb-0" data-toggle="tooltip" title="Click me for a definition!">
              <!-- Press to activate accordion -->
              <button v-on:click="changeActiveWord" class="btn btn-link" data-toggle="collapse" :data-target="definition.dataToggle" :data-word="definition.word" aria-expanded="true" :aria-controls="definition.ariaControls">
                {{ definition.word }}
              </button>
            </h5>
          </div>
          <!-- Conditionally renders -->
          <div v-if="activeWord === definition.word" :id="definition.cardHeader" class="collapse show" :aria-labelledby="definition.cardHeader" data-parent="#accordion">
            <div class="card-body">
              <dl v-for="([partOfSpeech, defText]) in definition.definitions" :key="defText">
                <dt>{{partOfSpeech}}</dt>
                <dd>{{defText}}</dd>
              </dl>
            </div>
          </div>
          <div v-else class="card-body">
            (Press word-text to view definitions)
          </div>
        </div>
      </div>
      <!-- If no results, say so -->
      <!-- Otherwise, show table of results -->
    </article>
  </div>
</template>

