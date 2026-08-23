<script setup>

  import defineProps from 'vue';

  defineProps({
    //searchResults: Array,
    //seriesTitle: String,
    seriesName: String,
    collapseKey: String,
  });

</script>

<template>
  <div class="accordion">
    <div class="accordion-item">
      <h3 class="accordion-header">
        <!-- Bootstrap: 'd-flex', 'justify-content-between' to separate series title and result-count.-->
        <!-- Bootstrap: 'btn-block' so that it spans entire width of container.-->
        <b-button v-b-toggle="'collapse-' + collapseKey" :data-series="seriesName" class="ShowResults d-flex justify-content-between btn btn-lg btn-block accordion-button" aria-expanded="true" :aria-controls="'collapse-' + collapseKey">
          <slot name="header">
          </slot>
        </b-button>
      </h3>
      <b-collapse :id="'collapse-' + collapseKey" :aria-labelledby="'heading-' + collapseKey">
        <b-card class="SearchResults accordion-body">
          <!-- Bootstrap: 'table-striped' for line visibility. -->
          <slot name="body">
          </slot>
        </b-card>
      </b-collapse>
    </div>
  </div>
</template>

