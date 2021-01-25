<template>
  <div class="home">
    <div class="row">
      <div class="col-sm-6">
        <div class="text" v-html="textContent">{{ textContent }}</div>
      </div>

      <div class="map col-sm-6 offset-sm-6 fixed-top">
        <select class="textSelect" v-model="text" @change="loadText">
          <option
            v-for="text in textsList"
            :value="text.text"
            :key="text.value"
          >
            {{ text.text }}
          </option>
        </select>

        <ItineraryMap v-if="normalmap == false" :locations="locations" />
        <Map v-if="normalmap == true" :locations="locations" />

        <b-button style="background-color: #009879;" @click="previousPage()" class="btn"
          >Page précédente</b-button
        >
        <b-button style="background-color: #009879;" @click="nextPage()" class="btn">Page suivante</b-button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Map from "./Map";
import ItineraryMap from "./ItineraryMap";

export default {
  name: "TextView",
  components: {
    Map,
    ItineraryMap,
  },
  props: ["normalmap"],
  data() {
    return {
      textsList: [],
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

.textSelect {
    margin-top: 2rem;
}

.btn {
    margin: 1rem;
}
</style>
