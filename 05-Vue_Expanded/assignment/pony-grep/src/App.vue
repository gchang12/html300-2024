<script setup>

  /* TODO:
    ( ) For the image page, convert the image markup into a separate component in its own file, be sure to import it into the corresponding 'page' component
    ( ) The image component should have props for at least the image src, alt, & title attributes, use prop validation.
    ( ) Creation and use of slot for header component
    ( ) Create a mixin for the image component that should toggle on/off a border around the image on click, apply the mixin to the image component.
    (X) Don't forget to add comments to your code explaining Bootstrap classes you added and your VUE code.
  */

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

        <span class="Disclaimer">All images are owned by Hasbro</span>
        <span class="Disclaimer">Made with no AI</span>
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

<!--
# Instructions

Expand on your course project website. In the Lesson04 assignment, you converted Bootstrap to Vue. Now, we're going to take that site and refactor it into some components. You'll be adding in some functionality through props and mixins.

These are the pages that will be making up your final project, so use the content (text, images) you want included in that final site.

## Requirements

    For the image page, convert the image markup into a separate component in its own file, be sure to import it into the corresponding 'page' component
    The image component should have props for at least the image src, alt, & title attributes, use prop validation.
    Creation and use of slot for header component
    Create a mixin for the image component that should toggle on/off a border around the image on click, apply the mixin to the image component.
    Don't forget to add comments to your code explaining Bootstrap classes you added and your VUE code.

Bonus: Use other components for existing content.    

Extra Bonus: Use custom directives or a modifier.  
		
Lesson 08 Assignment
Criteria	Ratings	Pts
Components
	
2 pts
Complete
Refactored into component with props & validation
1 pts
Incomplete
Missing props/validation
0 pts
Missing
Not refactored
	
/ 2 pts
Slots
	
2 pts
Complete
Creation and use of slot for header component
1 pts
Incomplete
Didn’t fully build out slot with named attribute and default
0 pts
Missing
No use of slot
	
/ 2 pts
Mixin
	
2 pts
Complete
Created and used mixin
1 pts
Incomplete
Didn’t fully implement mixin
0 pts
Missing
Didn’t use a mixin
	
/ 2 pts
Vue CLI
	
2 pts
Complete
Built correctly using Vue CLI
1 pts
Incomplete
Somewhat uses Vue CLI/Vue features
0 pts
Missing
No Vue CLI present/static files
	
/ 2 pts
-->
