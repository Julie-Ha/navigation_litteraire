<template>
  <div class="home">
    <div class="row">
      <div class="col-sm-6 mt-2">
        <div class="locations">{{ locations }}</div>
      </div>

      <div class="map col-sm-6 offset-sm-6 fixed-top">
        <Map :locations="selectedLocations" />
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
      textFile: "text",
      locations: [],
      selectedLocations: [],
      loaded: false,
    };
  },
  methods: {
    async loadLocations() {
      this.locations = [];

      await axios
        .get("http://127.0.0.1:5000/get-locations?text=" + this.textFile)
        .then((response) => {
          this.locations = response.data;
        });
    },
  },
  async created() {
    this.loadLocations();
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
