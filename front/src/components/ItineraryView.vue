<template>
  <div class="home">
    <div class="row">
      <div class="col-sm-6">
        <div class="text" v-html="text">{{ text }}</div>
      </div>

      <div class="map col-sm-6 offset-sm-6 fixed-top">
        <ItineraryMap :locations="locations" />

        <label>N° de ligne </label>
        <input v-model="line" type="number" name="line" min="0" />
        <b-button type="submit" @click="loadText()" class="btnVal">OK</b-button>
        <div>{{ locations }}</div> -->
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
      textFile: "text",
      text: "text",
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
            this.textFile +
            "&line=" +
            this.line
        )
        .then((response) => {
          this.locations = response.data.locations;
          this.text = response.data.text;
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
