<template>
  <div class="home">
    <div class="row">
      <div class="col-sm-6">
        <div class="text" v-html="text">{{ text }}</div>
      </div>
      <div class="map col-sm-6 offset-sm-6 fixed-top">
        <div>
          <div>
            <span v-if="loading">Loading...</span>
            <br />
          </div>
          <l-map
            :zoom="zoom"
            :center="center"
            style="height: 500px; width: 100%"
          >
            <l-tile-layer :url="url" :attribution="attribution" />
            <l-geo-json
              v-if="show"
              :geojson="geojson"
              :options="options"
              :options-style="styleFunction"
            />
          </l-map>
          <label>N° de ligne </label>
          <input v-model="line" type="number" name="line" min="0" />
          <b-button type="submit" @click="loadText()" class="btnVal"
            >OK</b-button
          >
          <div>{{ locations }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { LMap, LTileLayer, LGeoJson } from "vue2-leaflet";

export default {
  name: "Home",
  components: {
    LMap,
    LTileLayer,
    LGeoJson,
  },
  data() {
    return {
      textFile: "text",
      text: "text",
      line: 0,
      locations: [],
      loaded: false,
      loading: false,
      show: true,
      enableTooltip: true,
      zoom: 6,
      center: [48, -1.219482],
      geojson: null,
      fillColor: "#e4ce7f",
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
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

      this.loading = true;

      let json = [];
      this.locations.forEach(async (location) => {
        const response = await fetch(
          "https://api-adresse.data.gouv.fr/search/?q=" + location
        );

        let j = await response.json();

        if (j.features.length > 0) {
          json.push(j.features[0]);
        }
      });

      this.geojson = json;
      this.loading = false;

      setTimeout(() => {
        this.loaded = true;
      }, 1000);
    },
  },
  computed: {
    options() {
      return {
        onEachFeature: this.onEachFeatureFunction,
      };
    },
    styleFunction() {
      const fillColor = this.fillColor;
      return () => {
        return {
          weight: 2,
          color: "#ECEFF1",
          opacity: 1,
          fillColor: fillColor,
          fillOpacity: 1,
        };
      };
    },
    onEachFeatureFunction() {
      if (!this.enableTooltip) {
        return () => {};
      }
      return (feature, layer) => {
        layer.bindTooltip(
          "<div>total:" +
            feature.properties.total +
            "</div><div>nom: " +
            feature.properties.name +
            "</div>",
          { permanent: false, sticky: true }
        );
      };
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
