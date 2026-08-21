<script setup>

  import defineProps from 'vue';

  // NOTE: On second thought, this may belong in the parent component.
  import useBorder from '../mixins/useBorder.js';

  /* TODO:
    (X) For the image page, convert the image markup into a separate component in its own file, be sure to import it into the corresponding 'page' component
    (X) The image component should have props for at least the image src, alt, & title attributes, use prop validation.
    ( ) Creation and use of slot for header component
    (X) Create a mixin for the image component that should toggle on/off a border around the image on click, apply the mixin to the image component.
    (X) Don't forget to add comments to your code explaining Bootstrap classes you added and your VUE code.
  */

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
