<script setup>
  // Don't forget to add comments to your code explaining Bootstrap classes you added and your VUE code.

  import { ref } from "vue";
  import unicorns from "../constants/unicorns.js";
  //import episodeIdToObj from "../functions/episodeIdToObj.js";

  unicorns.forEach(unicorn => unicorn.isShown = false);
  const unicornList = ref(unicorns);
  const ponyEpisodes = ref([]);

  function toggleVisibility(e) {
    const id = e.target.dataset.id;
    //console.log(id, typeof id);
    const unicorn = unicornList.value.find(unicorn => unicorn.id == id);
    //unicorns.forEach(unicorn => console.log(typeof unicorn.id));
    //console.log(unicorn);
    unicorn.isShown = !unicorn.isShown;
    // convert to list of {seasonNo, episodeNo, title}
    ponyEpisodes.value = unicorn.episodes;
    console.log(unicorn);
    /*
    ponyEpisodes.value.speaking = ponyEpisodes.value.speaking.map(episodeIdToObj);
    ponyEpisodes.value.silent = ponyEpisodes.value.silent.map(episodeIdToObj);
    ponyEpisodes.value.background = ponyEpisodes.value.background.map(episodeIdToObj);
    ponyEpisodes.value.imagined = ponyEpisodes.value.imagined.map(episodeIdToObj);
    ponyEpisodes.value.inMedia = ponyEpisodes.value.inMedia.map(episodeIdToObj);
    ponyEpisodes.value.mentioned = ponyEpisodes.value.mentioned.map(episodeIdToObj);
    console.log(ponyEpisodes.value);
    */
  }

</script>

<template>
  <div id="dossier">
    <article>
      <h1>Dossier</h1>
      <article>
        <h2>Unicorns</h2>
        <div class="accordion" id="unicorn-dossier">
          <div class="card" v-for="unicorn in unicornList" :key="unicorn.id">
            <!-- HEAD -->
            <div class="card-header">
              <h2 class="mb-0" data-toggle="tooltip" title="Collapse / Expand">
                <button :data-id="unicorn.id" @click="toggleVisibility" class="btn btn-link" data-toggle="collapse" aria-expanded="false">
                  {{ unicorn.name }}
                </button>
              </h2>
            </div>
            <!-- BODY -->
            <div :data-id="unicorn.id" v-if="unicorn.isShown" class="collapse show" data-parent="#unicorn-dossier">
              <div class="card-body">
                <dl>
                  <dt>Species</dt>
                  <dd>{{ unicorn.species }}</dd>
                  <dt>Gender</dt>
                  <dd>{{ unicorn.gender }}</dd>
                </dl>
                <article>
                  <h3>Summary</h3>
                  <p v-for="line in unicorn.summary" :key="line">{{ line }}</p>
                </article>
                <!-- <article> <h3>Appearances</h3> <section> <h4>Speaking</h4> <ol> <li v-for="episode in ponyEpisodes" :key="episode.id"> (S{{ episode.seasonNo }} E{{ episode.episodeNo }}) {{ episode.title }} </li> </ol> </section> </article> -->
                <p>Wanna learn more? Check out {{ unicorn.name }}'s <a :href="'https://mlp.fandom.com/wiki/' + unicorn.urlName">page on the MLP Wikia</a>!</p>
              </div>
            </div>
          </div>
        </div>
      </article>
    </article>
  </div>
</template>
