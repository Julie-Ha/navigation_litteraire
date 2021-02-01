<template>
  <div class="home">
    <div class="row">
      <div class="text-col col-sm-6">
        <div class="text" v-html="textContent">{{ textContent }}</div>
      </div>

      <div class="map col-sm-6 offset-sm-6 fixed-top">
        <b-form-select class="textSelect" v-model="text" @change="loadText">
          <option
            v-for="text in textsList"
            :value="text.text"
            :key="text.value"
          >
            {{ text.text }}
          </option>
        </b-form-select>

        <ItineraryMap v-if="normalmap == false" :locations="locations" />
        <Map
          v-if="normalmap == true"
          :locations="locations"
          @myEvent="scrollText"
        />

        <b-button
          style="background-color: #009879;"
          @click="previousPage()"
          class="btn"
          >Page précédente</b-button
        >
        <b-button
          style="background-color: #009879;"
          @click="nextPage()"
          class="btn"
          >Page suivante</b-button
        >
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
      text: "lys",
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
    async scrollText(loc) {
      const el = this.$el.getElementsByClassName(loc)[0];
      console.log(el);

      if (el) {
        // Use el.scrollIntoView() to instantly scroll to the element
        // el.scrollIntoView({ behavior: "smooth" });
        // window.scrollTo(0, el.offsetTop-50);
        window.scrollTo({
          top: el.offsetTop-50,
          behavior: "smooth",
        });
      }
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
  margin-top: 1rem;
}

.btn {
  margin: 1rem;
}
</style>
