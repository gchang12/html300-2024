<script setup>
  import { ref } from 'vue';
  const definitions = ref([
    {
      word: "mercurial",
      cardHeader: "headingOne",
      ariaControls: "collapseOne",
      dataToggle: "#collapseOne",
      definitions: [
        ["noun", "Any of the plants known as mercury, especially the annual mercury or French mercury (Mercurialis annua)."],
        ["noun", "A person born under the influence of the planet Mercury; hence, a person having an animated, lively, quick-witted or volatile character."],
        ["noun", "A chemical compound containing mercury."],
        ["noun", "A preparation of mercury, especially as a treatment for syphilis."],
        ["adjective", "Having a lively or volatile character; animated, changeable, quick-witted."],
        ["adjective", "Pertaining to the astrological influence of the planet Mercury; having the characteristics of a person under such influence (see adjective sense 1)."],
        ["adjective", "Pertaining to the planet Mercury."],
        ["adjective", "Of or pertaining to the element mercury or quicksilver; containing mercury."],
        ["adjective", "Caused by the action of mercury or a mercury compound."],
        ["adjective", "Pertaining to Mercury, the Roman god of, among other things, commerce, financial gain, communication, and thieves and trickery; hence , money-making; crafty."],
      ],
    },
    {
      word: "verisimilitude",
      cardHeader: "headingTwo",
      ariaControls: "collapseTwo",
      dataToggle: "#collapseTwo",
      definitions: [
        ["noun", "The property of seeming true, of resembling reality; resemblance to reality, realism."],
        ["noun", "A statement which merely appears to be true."],
        ["noun", "Faithfulness to its own rules; internal cohesion."],
      ],
    },
    {
      word: "reminisce",
      cardHeader: "headingThree",
      ariaControls: "collapseThree",
      dataToggle: "#collapseThree",
      definitions: [
        ["noun", "An act of reminiscence."],
        ["verb", "To recall the past in a private moment, often fondly or nostalgically."],
        ["verb", "To talk or write about memories of the past, especially pleasant memories."],
        ["verb", "To remember fondly; to reminisce about."],
      ],
    }
  ]);
  const activeWord = ref("mercurial");
  function changeActiveWord(e) {
    activeWord.value = e.currentTarget.dataset.word;
  }
</script>

<template>
  <div id="accordion">
    <!-- Implemented accordion content structure here. -->
    <div class="card" v-for="definition in definitions" :key="definition.word">
      <div class="card-header" :id="definition.cardHeader">
        <!-- NOTE: Added tooltip here! -->
        <h5 class="mb-0" data-toggle="tooltip" title="Click me for a definition!">
          <!-- Press to activate accordion -->
          <button v-on:click="changeActiveWord" class="btn btn-link" data-toggle="collapse" :data-target="definition.dataToggle" :data-word="definition.word" aria-expanded="true" :aria-controls="definition.ariaControls">
            {{ definition.word }}
          </button>
        </h5>
      </div>
      <!-- Conditionally renders -->
      <div v-if="activeWord === definition.word" :id="definition.cardHeader" class="collapse show" :aria-labelledby="definition.cardHeader" data-parent="#accordion">
        <div class="card-body">
          <dl v-for="([partOfSpeech, defText]) in definition.definitions" :key="defText">
            <dt>{{partOfSpeech}}</dt>
            <dd>{{defText}}</dd>
          </dl>
        </div>
      </div>
      <div v-else class="card-body">
        (Press word-text to view definitions)
      </div>
    </div>
  </div>
</template>
