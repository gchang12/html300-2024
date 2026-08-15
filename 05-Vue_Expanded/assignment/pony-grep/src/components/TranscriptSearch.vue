<script setup>

  import { ref } from "vue";

  import searchTranscript from "../functions/searchTranscript.js";
  import parseTranscriptLines from "../functions/parseTranscriptLines.js";

  let searchResults = ref([]);
  let dialoguePattern = ref("");
  function searchAndParseResults(e) {
    /*
    const submitButton = document.getElementById("search-button");
    console.log(submitButton);
    if (!submitButton.reportValidity()) {
      console.log(submitButton);
      return;
    }
    */
    //console.log(e);
    //console.log(typeof e);
    //console.log(e.target.form);
    const formData = new FormData(e.target.form);
    if (formData.get("dialoguePattern") === "") {
      alert("'Pattern' cannot be blank!")
      return;
    }
    //console.log(formData);
    const searchCriteria = Object.fromEntries(formData.entries());
    const fetchedSearchResults = searchTranscript(searchCriteria);
    //console.log(fetchedSearchResults);
    const parsedSearchResults = parseTranscriptLines(fetchedSearchResults);
    //console.log(parsedSearchResults);
    searchResults.value = parsedSearchResults;
    //console.log(searchResults);
    dialoguePattern.value = formData.get("dialoguePattern");
  }
  function toggleVisibility(e) {
    const id = e.target.dataset.id;
    //console.log(id);
    //searchResults.value.forEach(result => console.log(typeof result.id, typeof id));
    const lineEntry = searchResults.value.find(result => id == result.id)
    lineEntry.isShown = !lineEntry.isShown;
  }

</script>

<template>
  <div class="vue-container" id="transcript-search">
    <article>
      <h1>Search Transcripts</h1>
      <p>Try to find out if somebody said something in <i>My Little Pony: Friendship is Magic</i> by inputting a string into the <code>Regex Pattern</code> box.</p>
      <p>Try to find out if somebody in particular said something by inputting their name into the <code>Character</code> box.</p>
      <p>Wanna find out if they said it in a song? Check the <code>Search in songs only?</code>.</p>
      <p>To find out if they said it in a particular season, input the season number into the <code>Season</code>.</p>
      <p>Trying to find out if they said it in a particular episode in a season? Input a number into the <code>Episode</code> box; note that this only works if you have the <code>Season</code> box already populated.</p>
      <form>
        <fieldset>
          <label>
            Regex Pattern <span aria-required="true">*</span>
            <input type="text" name="dialoguePattern" required />
          </label>
          <label>
            Search in songs only?
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
        <button id="search-button" @click="searchAndParseResults" type="button">Search</button>
      </form>
      <!-- If no results, say so -->
      <span v-if="dialoguePattern !== ''" id="result-notification">
        The query '{{ dialoguePattern }}' returned {{ searchResults.length }} results.
      </span>
      <!-- Otherwise, show table of results -->
      <div class="accordion" id="search-results">
        <div class="card" v-for="result in searchResults" :key="result.id">
          <!-- HEAD -->
          <div class="card-header">
            <h2 class="mb-0" data-toggle="tooltip" title="Collapse / Expand">
              <button :data-id="result.id" @click="toggleVisibility" class="btn btn-link" data-toggle="collapse" aria-expanded="false">
                S{{ result.seasonNo }} E{{ result.episodeNo }} - {{ result.title }} @{{result.lineNo}}
              </button>
            </h2>
          </div>
          <!-- BODY -->
          <div :data-id="result.id" v-if="result.isShown" class="collapse show" data-parent="#search-results">
            <div class="card-body">
              <div class="dialogue-block" v-for="line in result.contextLines" :key="line.id">
                <dl class="matched-line" v-if="line.lineNo === result.lineNo">
                  <dt>{{ line.speaker }}</dt>
                  <dd>{{ line.dialogue }}</dd>
                </dl>
                <dl v-else>
                  <dt>{{ line.speaker }}</dt>
                  <dd>{{ line.dialogue }}</dd>
                </dl>
              </div>
            </div>
          </div>
        </div>
      </div>
    </article>
  </div>
</template>

