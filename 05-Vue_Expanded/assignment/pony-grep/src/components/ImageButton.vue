<script setup>

  import defineProps from 'vue';

  // NOTE: On second thought, this may belong in the parent component.
  import useBorder from '../mixins/useBorder.js';

  const props = defineProps({
    src: String,
    alt: String,
    title: {
      type: String,
      required: false,
    },
    dataSeason: Number,
    onClick: Function,
    captionText: {
      type: String,
      required: true,
    },
  });

  const { toggleBorder } = useBorder();

  function onClickAndToggleBorder(e) {
    props.onClick(e);
    toggleBorder(e);
  }

</script>

<template>
  <!-- Bootstrap: 'btn' to remove default button styling and especially for zero-opacity -->
  <b-button v-b-tooltip.hover :title="title" class="btn" :data-season="dataSeason" @click="onClickAndToggleBorder">
    <figure>
      <img :src="src" :alt="alt" class="img-thumbnail" />
      <figcaption>
        <a class="nav-link" role="button">
          <!-- NOTE: Dropdown not working. Temporary fix. -->
          <!-- Bootstrap: 'btn-block' to make button width span container width -->
          <button class="btn btn-block btn-primary">
            {{ captionText }}
          </button>
        </a>
      </figcaption>
    </figure>
  </b-button>
</template>
