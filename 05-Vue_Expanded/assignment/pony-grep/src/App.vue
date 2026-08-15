<script setup>

  import { ref, computed } from "vue";

  import IndexPage from './components/IndexPage.vue'
  import EpisodeDirectory from './components/EpisodeDirectory.vue'
  import TranscriptSearch from './components/TranscriptSearch.vue'
  import DossierPage from './components/DossierPage.vue'

  // Excerpted from code in video demonstration.

  /* Start: Routing. */
  const routes = {
    "/": IndexPage,
    "/episodeDirectory": EpisodeDirectory,
    "/transcriptSearch": TranscriptSearch,
    "/dossier": DossierPage,
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
      href: "#/transcriptSearch",
      text: "Transcript Search",
    },
    {
      href: "#/episodeDirectory",
      text: "Episode Directory",
    },
    {
      href: "#/dossier",
      text: "Dossier",
    },
  ]);
  /* End: Routing. */

</script>

<template>
  <div id="app">
    <header>
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
        <a class="external" href="https://github.com/lucaong/minisearch">
          MiniSearch
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
