<template>
  <div class="home">
    <div class="row">
      <div class="col-sm-6">
        <div class="text" v-html="textContent">{{ textContent }}</div>
      </div>

      <div class="map col-sm-6 offset-sm-6 fixed-top">
        <ItineraryMap :locations="locations" />

        <b-button @click="previousPage()" class="btnVal"
          >Page précédente</b-button
        >
        <b-button @click="nextPage()" class="btnVal">Page suivante</b-button>
        <div>{{ locations }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ItineraryMap from "./ItineraryMap";

export default {
  name: "Home",
  components: {
    ItineraryMap,
  },
  data() {
    return {
      text: "bovary",
      textContent: "text",
      startChar: 0,
      action: "",
      locations: [],
      loaded: false,
    };
  },
  methods: {
    async loadText() {
      this.locations = [];

      await axios
        .get(
          "http://127.0.0.1:5000/get-annotated-text?text=" +
            this.text +
            "&char=" +
            this.startChar +
            "&action=" +
            this.action
        )
        .then((response) => {
          this.locations = response.data.locations;
          this.textContent = response.data.text;
          this.startChar = response.data.char;
        });

      await axios.get("http://127.0.0.1:5000/getList").then((response) => {
        this.textsList = response.data;
      });
    },
    async nextPage() {
      this.action = "next";
      this.loadText();
    },
    async previousPage() {
      this.action = "previous";
      this.loadText();
    },
  },
  async created() {
    this.loadText();
  },
};
</script>
<style>
.loc {
  color: red;
  font-weight: bold;
}

.text {
  text-align: justify;
  margin: 1rem 2rem;
}

.map {
  margin-top: 4rem;
}
</style>
