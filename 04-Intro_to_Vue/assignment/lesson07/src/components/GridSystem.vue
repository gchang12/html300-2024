<script setup>
  import { ref } from 'vue';
  const wordList = ref([
    {
      id: 0,
      word: "mercurial",
      partOfSpeech: "noun",
      defText: "Any of the plants known as mercury, especially the annual mercury or French mercury (Mercurialis annua).",
    },
    {
      id: 1,
      word: "mercurial",
      partOfSpeech: "noun",
      defText: "A person born under the influence of the planet Mercury; hence, a person having an animated, lively, quick-witted or volatile character.",
    },
    {
      id: 2,
      word: "mercurial",
      partOfSpeech: "noun",
      defText: "A chemical compound containing mercury.",
    },
    {
      id: 3,
      word: "mercurial",
      partOfSpeech: "noun",
      defText: "A preparation of mercury, especially as a treatment for syphilis.",
    },
    {
      id: 4,
      word: "mercurial",
      partOfSpeech: "adjective",
      defText: "Having a lively or volatile character; animated, changeable, quick-witted.",
    },
    {
      id: 5,
      word: "mercurial",
      partOfSpeech: "adjective",
      defText: "Pertaining to the astrological influence of the planet Mercury; having the characteristics of a person under such influence (see adjective sense 1).",
    },
    {
      id: 6,
      word: "mercurial",
      partOfSpeech: "adjective",
      defText: "Pertaining to the planet Mercury.",
    },
    {
      id: 7,
      word: "mercurial",
      partOfSpeech: "adjective",
      defText: "Of or pertaining to the element mercury or quicksilver; containing mercury.",
    },
    {
      id: 8,
      word: "mercurial",
      partOfSpeech: "adjective",
      defText: "Caused by the action of mercury or a mercury compound.",
    },
    {
      id: 9,
      word: "mercurial",
      partOfSpeech: "adjective",
      defText: "Pertaining to Mercury, the Roman god of, among other things, commerce, financial gain, communication, and thieves and trickery; hence , money-making; crafty.",
    },
  ]);
</script>

<template>
  <!-- Implement table using grid system -->
  <div id="grid-system">
    <div class="container">
      <div class="row" v-for="wordEntry in wordList" :key="wordEntry.id">
        <!-- Contains columns of increasing size. -->
        <div class="col-2">
          {{wordEntry.word}}
        </div>
        <div class="col-3">
          {{wordEntry.partOfSpeech}}
        </div>
        <div class="col-5">
          {{wordEntry.defText}}
        </div>
      </div>
    </div>
  </div>
</template>
