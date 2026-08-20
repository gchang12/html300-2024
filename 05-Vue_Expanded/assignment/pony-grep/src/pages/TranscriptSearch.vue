<script setup>
  /* Accordion Page */

  import { ref } from "vue";

  import searchTranscript from "../functions/searchTranscript.js";
  import parseTranscriptLines from "../functions/parseTranscriptLines.js";

  let searchResults = ref([]);
  let dialoguePattern = ref("");
  let activeSeries = ref("FiM");

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
  }

  function resetResults() {
    dialoguePattern.value = "";
    searchResults.value = [];
    disableAccordions();
  }

  function setActiveSeries(e) {
    const button = e.currentTarget;
    const series = button.dataset.series;
    if (activeSeries.value === series) {
      activeSeries.value = "";
    } else {
      activeSeries.value = series;
    }
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
          <div class="accordion" id="accordionExample">
            <div class="accordion-item">
              <h3 class="accordion-header" id="headingOne">
                <!-- Bootstrap: 'd-flex', 'justify-content-between' to separate series title and result-count.-->
                <!-- Bootstrap: 'btn-block' so that it spans entire width of container.-->
                <button disabled data-series="FiM" @click="setActiveSeries" class="ShowResults d-flex justify-content-between btn btn-lg btn-block accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                  <span class="SeriesTitle">My Little Pony: Friendship is Magic</span><span v-if="searchResults.length > 0" class="ResultCount">{{ searchResults.length }}</span>
                </button>
              </h3>
              <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample" v-if="activeSeries === 'FiM' && searchResults.length > 0">
                <div class="SearchResults accordion-body">
                  <!-- Bootstrap: 'table-striped' for line visibility. -->
                  <table class="table table-primary table-light table-striped">
                    <thead>
                      <tr>
                        <th>Speaker</th>
                        <th>Line</th>
                        <th>Episode</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="result in searchResults" :key="result.id">
                        <th>
                          {{ result.line.speaker }}
                        </th>
                        <td>
                          {{ result.line.dialogue }}
                        </td>
                        <td>
                          – S{{ result.seasonNo }} E{{ result.episodeNo }} –<br />
                          <i>{{result.title}}</i>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
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
