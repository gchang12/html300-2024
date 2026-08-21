<script setup>

  import defineProps from 'vue';

  import useBorder from '../mixins/useBorder.js';

  defineProps({
    title: {
      type: String,
      required: true,
    },
    captionText: {
      type: String,
      required: true,
    },
  });

  const { toggleBorder } = useBorder();

</script>

<template>
  <a class="EpisodeEntry" role="button">
    <!-- Bootstrap: 'btn-secondary' to indicate that episodes are secondary wrt seasons; also for the background color -->
    <b-button v-b-tooltip.hover.top @click="toggleBorder" :title="title" class="btn btn-secondary">{{ captionText }}</b-button>
  </a>
</template>
