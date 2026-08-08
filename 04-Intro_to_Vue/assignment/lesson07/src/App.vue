<script setup>
//import HelloWorld from './components/HelloWorld.vue'

import { ref, computed } from "vue";

import IndexPage from './components/IndexPage.vue'
import ImageGallery from './components/ImageGallery.vue'
import GridSystem from './components/GridSystem.vue'
import LandingPage from './components/LandingPage.vue'
import AccordionPage from './components/AccordionPage.vue'

/*
export default {
  name: 'App',
  components: {
    //HelloWorld,
    IndexPage,
    ImageGallery,
    GridSystem,
    LandingPage,
    AccordionPage,
  }
}
*/

// Excerpted from code in video demonstration.
/* Start: Routing. */

const routes = {
  "/": IndexPage,
  "/landing-page": LandingPage,
  "/images": ImageGallery,
  "/accordion": AccordionPage,
  "/grid-system": GridSystem,
}

const currentPath = ref(window.location.hash);

window.addEventListener("hashchange", () => {
  currentPath.value = window.location.hash;
});

const currentView = computed(() => {
  return routes[currentPath.value.slice(1) || "/"] || IndexPage;
});

/* End: Routing. */

</script>

<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <nav>
      <!-- Nav-bar where user can navigate between four pages. -->
      <ul>
        <li>
          <a href="#/landing-page">
            Landing Page
          </a>
        </li>
        <li>
          <a href="#/images">
            Images
          </a>
        </li>
        <li>
          <a href="#/accordion">
            Accordion Page
          </a>
        </li>
        <li>
          <a href="#/grid-system">
            Grid System
          </a>
        </li>
      </ul>
    </nav>
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

<!--
# Instructions
In the last assignment (Lesson 3), you created a responsive website with Bootstrap. In this assignment, you'll rebuild it with Vue.
Continue to work with the repository you have been working with.
Check the README.md file in lesson04/assignment for further details.
## Requirements
    Configure a router/routes for the navigation between pages (components)
    All repeated content must be from variables defined in the .vue page, using "v-for" to iterate through and build the content.
    You must use at least one "v-if v-else" statement to change content or UI.
    For the image page, use a "v-for" loop to iterate through an array of images.
    For the accordion page, use a "v-for" to iterate through an object to fill out the content in an accordion.
    Don't forget to add comments to your code explaining Bootstrap classes you added and your VUE code.
-->
