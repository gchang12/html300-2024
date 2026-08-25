<script setup>
  /* Accordion Page */

  import { ref } from "vue";

  import searchTranscript from "../functions/searchTranscript.js";
  import parseTranscriptLines from "../functions/parseTranscriptLines.js";

  import AccordionElement from "../components/AccordionElement.vue";

  let searchResults = ref([]);
  let dialoguePattern = ref("");

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
    //console.log(searchResults.length);
  }

  function resetResults() {
    dialoguePattern.value = "";
    searchResults.value = [];
  }

  const vHighlight = {
    inserted: (el) => {
      const re = new RegExp(dialoguePattern.value, "ig");
      //console.log("vHighlight: el", el);
      //console.log(el.innerHTML);
      //console.log("vHighlight: re", re);
      //console.log("vHighlight: el.innerHTML", el.innerHTML);
      el.innerHTML = el.innerHTML.replaceAll(re, (match) => "<span class='highlighted'>" + match + "</span>" );
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
          <AccordionElement 
            seriesName="FiM"
            collapseKey="1"
             >
             <template v-slot:header>
              <span class="SeriesTitle">My Little Pony: Friendship is Magic</span><span class="ResultCount">{{ searchResults.length }}</span>
             </template>
             <template v-slot:body>
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
                    <td v-highlight>
                      {{ result.line.dialogue }}
                    </td>
                    <td>
                      – S{{ result.seasonNo }} E{{ result.episodeNo }} –<br />
                      <i>{{result.title}}</i>
                    </td>
                  </tr>
                </tbody>
              </table>
             </template>
          </AccordionElement>
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
