<script setup>
  import { ref } from 'vue';
  const bookList = ref([
    {
      imgSrc: "/images/hp1.jpg",
      no: 1,
      title: "Philosopher's Stone",
      description: [
        `Harry Potter has never been the star of a Quidditch team, scoring points while riding a broom far above the ground. He knows no spells, has never helped to hatch a dragon, and has never worn a cloak of invisibility.`,
        `All he knows is a miserable life with the Dursleys, his horrible aunt and uncle, and their abominable son, Dudley - a great big swollen spoiled bully. Harry's room is a tiny closet at the foot of the stairs, and he hasn't had a birthday party in eleven years.`,
        `But all that is about to change when a mysterious letter arrives by owl messenger: a letter with an invitation to an incredible place that Harry - and anyone who reads about him - will find unforgettable.`,
      ],
      releaseDate: "1997-06-26",
    },
    {
      imgSrc: "/images/hp2.jpg",
      no: 2,
      title: "Chamber of Secrets",
      description: [
        `The Dursleys were so mean and hideous that summer that all Harry Potter wanted was to get back to the Hogwarts School for Witchcraft and Wizardry. But just as he's packing his bags, Harry receives a warning from a strange, impish creature named Dobby who says that if Harry Potter returns to Hogwarts, disaster will strike.`,
        `And strike it does. For in Harry's second year at Hogwarts, fresh torments and horrors arise, including an outrageously stuck-up new professor, Gilderoy Lockhart, a spirit named Moaning Myrtle who haunts the girls' bathroom, and the unwanted attentions of Ron Weasley's younger sister, Ginny.`,
      ],
      releaseDate: "1998-07-02",
    },
    {
      imgSrc: "/images/hp3.jpg",
      no: 3,
      title: "Prisoner of Azkaban",
      description: [
        `For twelve long years, the dread fortress of Azkaban held an infamous prisoner named Sirius Black. Convicted of killing thirteen people with a single curse, he was said to be the heir apparent to the Dark Lord, Voldemort.`,
        `Now he has escaped, leaving only two clues as to where he might be headed: Harry Potter's defeat of You-Know-Who was Black's downfall as well. And the Azkaban guards heard Black muttering in his sleep, "He's at Hogwarts... he's at Hogwarts."`,
        `Harry Potter isn't safe, not even within the walls of his magical school, surrounded by his friends. Because on top of it all, there may be a traitor in their midst.`,
      ],
      releaseDate: "1999-07-08",
    },
    {
      imgSrc: "/images/hp4.jpg",
      no: 4,
      title: "Goblet of Fire",
      description: [
        `Harry wants to get away from the pernicious Dursleys and go to the International Quidditch Cup with Hermione, Ron, and the Weasleys. He wants to dream about Cho Chang, his crush (and maybe do more than dream). He wants to find out about the mysterious event involving two other rival schools of magic, and a competition that hasn't happened for a hundred years. He wants to be a normal, fourteen-year-old wizard. Unfortunately for Harry Potter, he's not normal - even by wizarding standards.`,
        `And in this case, different can be deadly.`,
      ],
      releaseDate: "2000-07-08",
    },
    {
      imgSrc: "/images/hp5.jpg",
      no: 5,
      title: "Order of the Phoenix",
      description: [
        `There is a door at the end of a silent corridor. And it's haunting Harry Potter's dreams. Why else would he be waking in the middle of the night, screaming in terror?`,
        `It's not just the upcoming O.W.L. exams; a new teacher with a personality like poisoned honey; a venomous, disgruntled house-elf; or even the growing threat of He-Who-Must-Not-Be-Named. Now Harry Potter is faced with the unreliability of the very government of the magical world and the impotence of the authorities at Hogwarts.`,
        `Despite this (or perhaps because of it), he finds depth and strength in his friends, beyond what even he knew; boundless loyalty; and unbearable sacrifice.`,
      ],
      releaseDate: "2003-06-21",
    },
    {
      imgSrc: "/images/hp6.jpg",
      no: 6,
      title: "Half-Blood Prince",
      description: [
        `The war against Voldemort is not going well; even Muggle governments are noticing. Ron scans the obituary pages of the Daily Prophet, looking for familiar names. Dumbledore is absent from Hogwarts for long stretches of time, and the Order of the Phoenix has already suffered losses. And yet...`,
        `As in all wars, life goes on. Sixth-year students learn to Apparate - and lose a few eyebrows in the process. The Weasley twins expand their business. Teenagers flirt and fight and fall in love. Classes are never straightforward, though Harry receives some extraordinary help from the mysterious Half-Blood Prince.`,
      ],
      releaseDate: "2005-07-16",
    },
    {
      imgSrc: "/images/hp7.jpg",
      no: 7,
      title: "Deathly Hallows",
      description: ["We now present the seventh and final installment in the epic tale of Harry Potter."],
      releaseDate: "2007-07-21",
    },
  ]);
</script>

<template>
  <!-- Implement table using grid system -->
  <div id="grid-system">
    <div class="container">
      <!-- Header row -->
      <div id="grid-system-header-row" class="row">
        <div class="col-1">
          No.
        </div>
        <div class="col-2">
          Book
        </div>
        <div class="col-6">
          Description
        </div>
        <div class="col-2">
          Release Date
        </div>
      </div>
      <div class="row" v-for="book in bookList" :key="book.no">
        <!-- Contains columns of increasing size. -->
        <div class="col-1 cell">
          {{book.no}}
        </div>
        <div class="col-2 cell book-cover">
          <figure>
            <img width="100" :src="book.imgSrc" :alt="book.imgSrc" />
            <figcaption>Harry Potter and the {{book.title}}</figcaption>
          </figure>
        </div>
        <div class="col-6 cell">
          <p v-for="descLine in book.description" :key="descLine">{{descLine}}</p>
        </div>
        <div class="col-2 cell">
          {{book.releaseDate}}
        </div>
      </div>
    </div>
  </div>
</template>
