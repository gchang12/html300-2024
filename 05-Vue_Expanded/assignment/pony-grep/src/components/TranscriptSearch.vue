<script setup>

  import { ref } from "vue";

  import searchTranscript from "../functions/searchTranscript.js";
  import parseTranscriptLines from "../functions/parseTranscriptLines.js";

  let searchResults = ref([]);
  let dialoguePattern = ref("");
  let activeSeries = ref(["mlp-fim"]);

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
    if (formData.get("dialoguePattern") === "" || formData.get("dialoguePattern").length < 3) {
      alert("'Pattern' cannot be blank or fewer than three characters!")
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

</script>

<template>
  <div class="vue-container" id="transcript-search">
    <article>
      <h1>Search</h1>
      <!-- <p>Try to find out if somebody said something in <i>My Little Pony: Friendship is Magic</i> by inputting a string into the <code>Regex Pattern</code> box.</p> -->
      <!-- <p>Try to find out if somebody in particular said something by inputting their name into the <code>Character</code> box.</p> -->
      <!-- <p>Wanna find out if they said it in a song? Check the <code>In songs only</code> box.</p> -->
      <!-- <p>To find out if they said it in a particular season, input the season number into the <code>Season</code>.</p> -->
      <!-- <p>Trying to find out if they said it in a particular episode in a season? Input a number into the <code>Episode</code> box; note that this only works if you have the <code>Season</code> box already populated.</p> -->
      <form>
        <fieldset>
          <label>
            Regex Pattern <span aria-required="true">*</span>
            <input type="text" name="dialoguePattern" required />
          </label>
          <label>
            Lyrics Only
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
      <div id="search-results">
        <div id="mlp-fim" class="search-results" v-if="activeSeries.includes('mlp-fim') && searchResults.length > 0">
          <table>
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
                  S{{ result.seasonNo }} E{{ result.episodeNo }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </article>
  </div>
</template>

