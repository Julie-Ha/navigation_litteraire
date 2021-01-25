<template>
  <div class="home">
    <div class="row">
      <div class="col-sm-6 mt-2">
        <div class="locations">
          <b-list-group>
            <b-list-group-item v-for="location in locations" :key="location">
              <b-form-checkbox
                type="checkbox"
                class="text-left"
                :id="location"
                :value="location"
                v-model="selectedLocations"
                >{{ location }}</b-form-checkbox
              >
            </b-list-group-item>
          </b-list-group>
        </div>
      </div>

      <div class="map col-sm-6 offset-sm-6 fixed-top">
        <ItineraryMap v-if="normalmap == false" :locations="selectedLocations" />
        <Map v-if="normalmap == true" :locations="selectedLocations" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Map from "./Map";
import ItineraryMap from "./ItineraryMap";

export default {
  name: "Locations",
  components: {
    Map,
    ItineraryMap,
  },
  props: ["normalmap"],
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
.locations {
  margin: 1.25rem 2rem;
}

.map {
  margin-top: 4rem;
}
</style>
