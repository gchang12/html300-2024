<script setup>

  import { ref, computed } from "vue";

  import IndexPage from './components/IndexPage.vue'
  import EpisodeDirectory from './components/EpisodeDirectory.vue'
  import TranscriptSearch from './components/TranscriptSearch.vue'

  import EpisodeDirectory1 from './components/episodeDirectories/EpisodeDirectory1.vue'
  import EpisodeDirectory2 from './components/episodeDirectories/EpisodeDirectory2.vue'
  import EpisodeDirectory3 from './components/episodeDirectories/EpisodeDirectory3.vue'
  import EpisodeDirectory4 from './components/episodeDirectories/EpisodeDirectory4.vue'
  import EpisodeDirectory5 from './components/episodeDirectories/EpisodeDirectory5.vue'
  import EpisodeDirectory6 from './components/episodeDirectories/EpisodeDirectory6.vue'
  import EpisodeDirectory7 from './components/episodeDirectories/EpisodeDirectory7.vue'
  import EpisodeDirectory8 from './components/episodeDirectories/EpisodeDirectory8.vue'
  import EpisodeDirectory9 from './components/episodeDirectories/EpisodeDirectory9.vue'
  //import DossierPage from './components/DossierPage.vue'

  // Excerpted from code in video demonstration.

  /* Start: Routing. */
  const routes = {
    "/": TranscriptSearch,
    "/about": IndexPage,
    "/transcripts": EpisodeDirectory,
    "/transcripts/FiM/S1": EpisodeDirectory1,
    "/transcripts/FiM/S2": EpisodeDirectory2,
    "/transcripts/FiM/S3": EpisodeDirectory3,
    "/transcripts/FiM/S4": EpisodeDirectory4,
    "/transcripts/FiM/S5": EpisodeDirectory5,
    "/transcripts/FiM/S6": EpisodeDirectory6,
    "/transcripts/FiM/S7": EpisodeDirectory7,
    "/transcripts/FiM/S8": EpisodeDirectory8,
    "/transcripts/FiM/S9": EpisodeDirectory9,
  }
  const currentPath = ref(window.location.hash);
  window.addEventListener("hashchange", () => {
    currentPath.value = window.location.hash;
  });
  const currentView = computed(() => {
    return routes[currentPath.value.slice(1) || "/"] || IndexPage;
  });
  const pageList = ref([
    {
      href: "#/about",
      text: "About",
    },
    {
      href: "#/transcripts",
      text: "Transcripts",
    },
    //{ href: "#/dossier", text: "Dossier", },
  ]);
  /* End: Routing. */

</script>

<template>
  <div id="app">
    <header>
      <a href="/#/" class="img-link">
        <img src="./assets/banner.png" />
      </a>
      <nav>
        <!-- TODO: Re-add expandable navibar -->
        <menu>
          <li v-for="page in pageList" :key="page.href">
            <a :href="page.href">
              {{ page.text }}
            </a>
          </li>
        </menu>
      </nav>
    </header>
    <main>
      <component :is="currentView" />
    </main>
    <footer>
      <div class="credits">
        <span class="footer-section-header">
          Credits
        </span>
        <a class="external" href="https://www.fandom.com/licensing">
          Fandom
        </a>
        <a class="external" href="https://github.com/gchang12/html300-2024/tree/lesson8">
          GitHub
        </a>
      </div>
    </footer>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
