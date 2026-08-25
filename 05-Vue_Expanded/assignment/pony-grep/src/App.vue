<script setup>

  import { ref, computed } from "vue";

  import IndexPage from './pages/IndexPage.vue'
  import EpisodeDirectory from './pages/EpisodeDirectory.vue'
  import TranscriptSearch from './pages/TranscriptSearch.vue'

  // Excerpted from code in video demonstration.
  /* Start: Routing. */
  const routes = {
    "/": TranscriptSearch,
    "/about": IndexPage,
    "/transcripts": EpisodeDirectory,
  }
  const currentPath = ref(window.location.hash);
  window.addEventListener("hashchange", () => {
    currentPath.value = window.location.hash;
  });
  const currentView = computed(() => {
    return routes[currentPath.value.slice(1) || "/"] || IndexPage;
  });
  /* End: Routing. */

  /* TODO
  Source comprehensive transcript file and index file.
  Modify index file and update transcript file to match it.
  Add dropdown menus to episode-directory
  Add fieldset to search form to allow user to specify where to grep
  Put episode-transcript into its own set of pages.
  Add new accordions for search results.
  Make accordions appear only for specified series.
  Get new images to use for indexes of other MLP G4 series. 
  For CYOA shorts, implement branched transcripts
  Highlight matched patterns
  */

</script>

<template>
  <div id="app">
    <header>
      <!-- Bootstrap: 'container' declares grid layout; 1 row, 2 columns. (Logo, Navibar) -->
      <div class="container"> 
        <div class="NaviBar row justify-content-between align-items-center">
          <!-- Bootstrap: 'col-auto' makes container width shrink to fit contents -->
          <div class="col-auto">
            <a href="/#/" class="img-link Logo">
              <img src="./assets/banner.png" />
            </a>
          </div>
          <div class="col-auto">
            <nav>
              <!-- Bootstrap: 'nav' makes container an actual navibar -->
              <ul class="nav">
                <li class="nav-item">
                  <a class="nav-link" href="/#/about">About</a>
                </li>
                <li class="nav-item">
                  <!-- Bootstrap: 'nav-link' provides v-centering. -->
                  <a class="nav-link" href="/#/transcripts">Transcripts</a>
                </li>
              </ul>
            </nav>
          </div>
        </div>
      </div> 
    </header>
    <main>
      <component :is="currentView" />
    </main>
    <footer>
      <article class="Credits">
        <span class="FooterSectionHeader">
          Credits
        </span>
        <ul>
          <li>
            All textual content is owned by <a target="_blank" class="External" href="https://www.fandom.com/licensing">Fandom</a>
          </li>
          <li>
            This project's <a target="_blank" class="External" href="https://github.com/gchang12/html300-2024/tree/lesson8">GitHub</a> page
          </li>
          <li>
            Site logo provided by <a href="https://fontmeme.com/friendship-is-magic-font/" target="_blank" class="External">this site</a>
          </li>
        </ul>

        <div class="Disclaimer">All images are owned by Hasbro</div>
        <div class="Disclaimer">Made with no AI</div>
      </article>
    </footer>
  </div>
</template>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /*margin-top: 60px;*/
  /*min-height: 100%;*/
}
</style>

