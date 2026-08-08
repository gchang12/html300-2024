<script>
</script>

<template>
  <div id="accordion">
    <!-- Implemented accordion content structure here. -->
    <div class="card">
      <div class="card-header" id="headingOne">
        <!-- NOTE: Added tooltip here! -->
        <h5 class="mb-0" data-toggle="tooltip" title="Click me for a definition!">
          <!-- Press to activate accordion -->
          <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            mercurial
          </button>
        </h5>
      </div>
      <!-- Conditionally renders -->
      <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
        <div class="card-body">
          <dl>
            <dt>noun</dt>
            <dd>Any of the plants known as mercury, especially the annual mercury or French mercury (Mercurialis annua).</dd>
            <dt>noun</dt>
            <dd>A person born under the influence of the planet Mercury; hence, a person having an animated, lively, quick-witted or volatile character.</dd>
            <dt>noun</dt>
            <dd>A chemical compound containing mercury.</dd>
            <dt>noun</dt>
            <dd>A preparation of mercury, especially as a treatment for syphilis.</dd>
            <dt>adjective</dt>
            <dd>Having a lively or volatile character; animated, changeable, quick-witted.</dd>
            <dt>adjective</dt>
            <dd>Pertaining to the astrological influence of the planet Mercury; having the characteristics of a person under such influence (see adjective sense 1).</dd>
            <dt>adjective</dt>
            <dd>Pertaining to the planet Mercury.</dd>
            <dt>adjective</dt>
            <dd>Of or pertaining to the element mercury or quicksilver; containing mercury.</dd>
            <dt>adjective</dt>
            <dd>Caused by the action of mercury or a mercury compound.</dd>
            <dt>adjective</dt>
            <dd>Pertaining to Mercury, the Roman god of, among other things, commerce, financial gain, communication, and thieves and trickery; hence , money-making; crafty.</dd>
          </dl>
        </div>
      </div>
    </div>
    <div class="card">
      <div class="card-header" id="headingTwo">
        <!-- NOTE: Added tooltip here! -->
        <h5 class="mb-0" data-toggle="tooltip" title="Click me for a definition!">
          <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            verisimilitude
          </button>
        </h5>
      </div>
      <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
        <div class="card-body">
          <dl>
            <dt>noun</dt>
            <dd>The property of seeming true, of resembling reality; resemblance to reality, realism.</dd>
            <dt>noun</dt>
            <dd>A statement which merely appears to be true.</dd>
            <dt>noun</dt>
            <dd>Faithfulness to its own rules; internal cohesion.</dd>
          </dl>
        </div>
      </div>
    </div>
    <div class="card">
      <div class="card-header" id="headingThree">
        <!-- NOTE: Added tooltip here! -->
        <h5 class="mb-0" data-toggle="tooltip" title="Click me for a definition!">
          <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
            reminisce
          </button>
        </h5>
      </div>
      <div id="collapseThree" class="collapse" aria-labelledby="headingThree" data-parent="#accordion">
        <div class="card-body">
          <dl>
            <dt>noun</dt>
            <dd>An act of reminiscence.</dd>
            <dt>verb</dt>
            <dd>To recall the past in a private moment, often fondly or nostalgically.</dd>
            <dt>verb</dt>
            <dd>To talk or write about memories of the past, especially pleasant memories.</dd>
            <dt>verb</dt>
            <dd>To remember fondly; to reminisce about.</dd>
          </dl>
        </div>
      </div>
    </div>
  </div>
</template>
