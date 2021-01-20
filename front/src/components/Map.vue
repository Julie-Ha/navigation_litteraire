<template>
  <div>
    <div>
      <span v-if="loading">Loading...</span>
      <br />
    </div>
    <l-map :zoom="zoom" :center="center" style="height: 500px; width: 100%">
      <l-tile-layer :url="url" :attribution="attribution" />
      <l-geo-json
        v-if="show"
        :geojson="geojson"
        :options="options"
        :options-style="styleFunction"
      />
    </l-map>
  </div>
</template>

<script>
import { LMap, LTileLayer, LGeoJson } from "vue2-leaflet";

export default {
  name: "Map",
  props: ["locations"],
  components: {
    LMap,
    LTileLayer,
    LGeoJson,
  },
  data() {
    return {
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
  watch: {
    locations: function() {
        this.loadMap();
    },
  },
  methods: {
    async loadMap() {
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
      console.log(json);
      this.geojson = json;
      this.loading = false;
    },
  },
  computed: {
    options() {
      return {
        onEachFeature: this.onEachFeatureFunction,
      };
    },
    styleFunction() {
      const fillColor = this.fillColor; // important! need touch fillColor in computed for re-calculate when change fillColor
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
          "<div>" +
            feature.properties.name +
            "</div>",
          { permanent: false, sticky: true }
        );
      };
    },
  },
  async created() {
    setTimeout(() => {
      this.loadMap();
    }, 1000);
  },
};
</script>
