<script setup>
  /* Accordion Page */

  import { ref } from "vue";

  import searchTranscript from "../functions/searchTranscript.js";
  import parseTranscriptLines from "../functions/parseTranscriptLines.js";

  import AccordionResults from "../components/AccordionResults.vue";

  let searchResults = ref([]);
  let dialoguePattern = ref("");

  function enableAccordions() {
    const resultsButtons = document.querySelectorAll(".ShowResults");
    for (const button of resultsButtons) {
      button.removeAttribute("disabled");
    }
  }

  function disableAccordions() {
    const resultsButtons = document.querySelectorAll(".ShowResults");
    for (const button of resultsButtons) {
      button.setAttribute("disabled", "disabled");
    }
  }

  function searchAndParseResults(e) {
    const formData = new FormData(e.currentTarget.form);
    if (!e.currentTarget.reportValidity() || formData.get("dialoguePattern") === "") {
      return;
    }
    const searchCriteria = Object.fromEntries(formData.entries());
    const fetchedSearchResults = searchTranscript(searchCriteria);
    const parsedSearchResults = parseTranscriptLines(fetchedSearchResults);
    searchResults.value = parsedSearchResults;
    dialoguePattern.value = formData.get("dialoguePattern");
    e.preventDefault();
    enableAccordions();
    console.log(searchResults.length);
  }

  function resetResults() {
    dialoguePattern.value = "";
    searchResults.value = [];
    disableAccordions();
  }

</script>

<template>
  <div id="transcript-search">
    <h1>Search Transcripts</h1>

    <!-- Bootstrap: 'container' for Grid System layout. 1 row, 2 columns. (Parameters, Results). -->
    <div class="container">
      <div class="row">

        <article class="col-3">
          <h2>Parameters</h2>
          <form>
            <div class="row">
              <div class="col Dialogue Field">
                <label for="dialoguePattern">Dialogue</label>
                <!-- Bootstrap: 'form-control' for a text-box spanning the container width. -->
                <input placeholder="friendship is magic" minlength="3" id="dialoguePattern" class="form-control" type="text" name="dialoguePattern" required />
                <div class="Help form-text">Pattern to search for in all G4 dialogue.</div>
              </div>
            </div>
            <div class="row">
              <div class="col Character Field">
                <label for="speaker">Character</label>
                <input placeholder="discord|mane six" id="speaker" class="form-control" type="text" name="speaker" />
                <!-- Bootstrap: 'form-text' for spacing. -->
                <div class="Help form-text">Limit results to lines spoken only by specified character(s).</div>
              </div>
            </div>
            <button class="btn btn-primary" id="search-button" @click="searchAndParseResults">Search</button>
            <button class="btn btn-secondary" id="reset-button" type="button" @click="resetResults">Reset</button>
          </form>
        </article>

        <article class="col">
          <h2>Results</h2>
          <AccordionResults 
            :searchResults="searchResults"
            seriesName="FiM"
            collapseKey="1"
             >
             <template v-slot:header>
              <span class="SeriesTitle">My Little Pony: Friendship is Magic</span><span class="ResultCount">{{ searchResults.length }}</span>
             </template>
          </AccordionResults>
        </article>

      </div>
    </div>

  </div>
</template>

<!-- NOTE: For recycling. Ignore! -->

<!-- <div class="col-2 Lyrics Field"> -->
<!-- <label for="isSung" class="form-label">Lyrics</label> -->
<!-- <input id="isSung" class="form-check" type="checkbox" name="isSung" /> -->
<!-- <div class="form-text">Search in lyrics as well?</div> -->
<!-- </div> -->
<!-- <div class="row"> -->
<!-- <div class="col Series Field"> -->
<!-- NOTE: Placeholder -->
<!-- <fieldset> -->
<!-- <legend>Series</legend> -->
<!-- <div class="MLP-FiM Field Choice"> -->
<!-- <label for="mlp-fim" class="form-label">MLP: FiM</label> -->
<!-- <input id="mlp-fim" class="form-check" disabled readonly checked type="checkbox" aria-label="readonly" /> -->
<!-- </div> -->
<!-- </fieldset> -->
<!-- </div> -->
<!-- </div> -->
