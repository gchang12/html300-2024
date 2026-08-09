<script setup>
  //import { ref, defineProps } from "vue"
  import { ref, } from "vue"
  //defineProps(['images']);
  const images = ref([
    {
      src: "/images/polar-night.jpg",
      alt: "Dusk at the dawn of the polar night",
    },
    {
      src: "/images/antarctica.jpg",
      alt: "Antarctica sky and ice",
    }
  ]);
</script>

<template>
  <div id="image-gallery">
    <figure v-for="image in images" :key="image.src">
      <!-- img-fluid class is added to ensure that image is responsive -->
      <img class="img-fluid" :src="image.src" :alt="image.alt" />
      <figcaption>{{image.alt}}
      <!-- Image attribution here, within figure caption. -->
      </figcaption>
    </figure>
    <!-- https://openverse.org/image/a139ef61-0ef7-480c-a07f-441129b209a7?q=polar+night&p=8 -->
    <p class="attribution">"<a rel="noopener noreferrer" href="https://www.flickr.com/photos/38144390@N04/4395753165">Dusk at the dawn of the polar night</a>" by <a rel="noopener noreferrer" href="https://www.flickr.com/photos/38144390@N04">Bernt Sønvisen</a> is licensed under <a rel="noopener noreferrer" href="https://creativecommons.org/licenses/by/2.0/?ref=openverse">CC BY 2.0 <img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" style="height: 1em; margin-right: 0.125em; display: inline;" /><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" style="height: 1em; margin-right: 0.125em; display: inline;" /></a>.</p>
    <!-- https://openverse.org/image/62203ec4-9155-4089-9d2c-a008c8ea092b?q=antarctica&p=21 -->
    <p class="attribution">"<a rel="noopener noreferrer" href="https://www.flickr.com/photos/10978010@N07/12434752073">Antarctica sky and ice</a>" by <a rel="noopener noreferrer" href="https://www.flickr.com/photos/10978010@N07">londoncyclist</a> is licensed under <a rel="noopener noreferrer" href="https://creativecommons.org/licenses/by/2.0/?ref=openverse">CC BY 2.0 <img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" style="height: 1em; margin-right: 0.125em; display: inline;" /><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" style="height: 1em; margin-right: 0.125em; display: inline;" /></a>.</p>
  </div>
</template>
