<script setup>

  import { ref } from "vue";

  import searchTranscript from "../functions/searchTranscript.js";
  import parseTranscriptLines from "../functions/parseTranscriptLines.js";

  let searchResults = ref([]);
  let dialoguePattern = ref("");
  let activeSeries = ref(["mlp-fim"]);

  function searchAndParseResults(e) {
    if (!e.currentTarget.reportValidity()) {
      return;
    }
    const formData = new FormData(e.currentTarget.form);
    const searchCriteria = Object.fromEntries(formData.entries());
    const fetchedSearchResults = searchTranscript(searchCriteria);
    const parsedSearchResults = parseTranscriptLines(fetchedSearchResults);
    searchResults.value = parsedSearchResults;
    dialoguePattern.value = formData.get("dialoguePattern");
    e.preventDefault();
  }

</script>

<template>
  <div id="transcript-search">
    <h1>Search</h1>
    <article>
      <h2>Query</h2>
      <!-- <p>Try to find out if somebody said something in <i>My Little Pony: Friendship is Magic</i> by inputting a string into the <code>Regex Pattern</code> box.</p> -->
      <!-- <p>Try to find out if somebody in particular said something by inputting their name into the <code>Character</code> box.</p> -->
      <!-- <p>Wanna find out if they said it in a song? Check the <code>In songs only</code> box.</p> -->
      <!-- <p>To find out if they said it in a particular season, input the season number into the <code>Season</code>.</p> -->
      <!-- <p>Trying to find out if they said it in a particular episode in a season? Input a number into the <code>Episode</code> box; note that this only works if you have the <code>Season</code> box already populated.</p> -->
      <form>
        <div class="Dialogue Field">
          <label for="dialoguePattern" class="form-label">Dialogue</label>
          <input minlength="3" id="dialoguePattern" class="form-control" type="text" name="dialoguePattern" required />
        </div>
        <div class="Lyrics Field">
          <label for="isSung" class="form-label">Lyrics Only</label>
          <input id="isSung" class="form-check" type="checkbox" name="isSung" />
        </div>
        <div class="Character Field">
          <label for="speaker" class="form-label">Character</label>
          <input id="speaker" class="form-control" type="text" name="speaker" />
        </div>
        <div class="Series Field">
          <!-- NOTE: Placeholder -->
          <fieldset>
            <legend>Series</legend>
            <div class="MLP-FiM Field Choice">
              <label for="mlp-fim" class="form-label">MLP: FiM</label>
              <input id="mlp-fim" class="form-check" disabled readonly checked type="checkbox" aria-label="readonly" />
            </div>
          </fieldset>
        </div>
        <button class="btn btn-primary" id="search-button" @click="searchAndParseResults">Search</button>
      </form>
    </article>

    <!-- If no results, say so -->
    <article>
      <h2>Results</h2>
      <span v-if="dialoguePattern !== ''" id="result-notification">
        {{ searchResults.length }} results for '{{ dialoguePattern }}'
      </span>
      <!-- Otherwise, show table of results -->
      <div id="search-results">
        <div id="mlp-fim" class="SearchResults" v-if="activeSeries.includes('mlp-fim') && searchResults.length > 0">
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

