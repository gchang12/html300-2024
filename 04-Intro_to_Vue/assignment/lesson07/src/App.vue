<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}

/* Imported from video demonstration. */

/*
import { ref, computed } from "vue";
import Home from "./components/Home.vue";
import About from "./components/About.vue";
import NotFound from "./components/NotFound.vue";

const routes = {
  "/": Index,
  "/landing-page": LandingPage,
  "/images": Images,
  "/accordion": Accordion,
  "/grid-system": GridSystem,
}

const currentPath = ref(window.location.hash);

window.addEventListener("hashchange", () => {
  currentPath.value = window.location.hash;
});

const currentView = computed(() => {
  return routes[currentPath.value.slice(1) || "/"] || NotFound;
});
*/

/* Imported from video demonstration. */

</script>

<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <component :is="currentView" />
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
