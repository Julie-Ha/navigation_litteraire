<template>
  <div class="home">
    <div class="row">
      <div class="col-sm-6">
        <div class="text" v-html="textContent">{{ textContent }}</div>
      </div>

      <div class="map col-sm-6 offset-sm-6 fixed-top">
        <select v-model="text" @change="loadText">
          <option v-for="text in textsList" :value="text.text" :key="text.value">
            {{ text.text }}
          </option>
        </select>

        <Map :locations="locations" />

        <label>N° de ligne </label>
        <input v-model="line" type="number" name="line" min="0" />
        <b-button type="submit" @click="loadText()" class="btnVal">OK</b-button>
        <div>{{ locations }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Map from "./Map";

export default {
  name: "Home",
  components: {
    Map,
  },
  data() {
    return {
      textsList: [],
      text: "bovary",
      textContent: "text",
      line: 0,
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
            "&line=" +
            this.line
        )
        .then((response) => {
          this.locations = response.data.locations;
          this.textContent = response.data.text;
        });

      await axios.get("http://127.0.0.1:5000/getList").then((response) => {
        this.textsList = response.data;
      });
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
