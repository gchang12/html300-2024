<script setup>

  import defineProps from 'vue';

  defineProps({
    searchResults: Array,
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
          <table class="table table-primary table-light table-striped">
            <thead>
              <tr>
                <th>Speaker</th>
                <th>Line</th>
                <th>Episode</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="result in searchResults" :key="result.id">
                <th>
                  {{ result.line.speaker }}
                </th>
                <td>
                  {{ result.line.dialogue }}
                </td>
                <td>
                  – S{{ result.seasonNo }} E{{ result.episodeNo }} –<br />
                  <i>{{result.title}}</i>
                </td>
              </tr>
            </tbody>
          </table>
        </b-card>
      </b-collapse>
    </div>
  </div>
</template>

