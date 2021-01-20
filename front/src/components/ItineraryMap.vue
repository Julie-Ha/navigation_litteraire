<template>
  <div>
    <div>
      <br />
    </div>
    <!-- <l-map :zoom="zoom" :center="center" style="height: 500px; width: 100%">
      <l-tile-layer :url="url" :attribution="attribution" />
      <l-geo-json
        v-if="show"
        :geojson="geojson"
        :options="options"
        :options-style="styleFunction"
      />
    </l-map> -->
    <section>
      <div id="map"></div>
    </section>
  </div>
</template>

<script>
import "./lib/MovingMarker.js";
import L from "leaflet";

export default {
  name: "ItineraryMap",
  props: ["locations"],
  data() {
    return {
      map: null,
      marker: null,
      coord: [
        [41.385064, 2.173403],
        [42.698611, 2.895556],
        [43.3017, -0.3686],
        [44.837912, -0.579541],
        [43.296346, 5.369889],
        [43.738418, 7.424616],
      ],
      coords: [],
    };
  },
  watch: {
    locations: function() {
      this.loadMap();
    },
  },
  methods: {
    async initialiseMap() {
      // initialize the map on the "map" div with a given center and zoom
      this.map = new L.Map("map", {
        zoom: 6,
        minZoom: 3,
      });

      // create a new tile layer
      let tileUrl = "http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        layer = new L.TileLayer(tileUrl, {
          attribution:
            'Maps © <a href="www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
          maxZoom: 18,
        });

      // add the layer to the map
      this.map.addLayer(layer);
    },
    async loadCoords() {
      this.coords = [];
      this.locations.forEach(async (location) => {
        const response = await fetch(
          "https://api-adresse.data.gouv.fr/search/?q=" + location
        );
        let j = await response.json();
        if (j.features.length > 0) {
          this.coords.push(j.features[0].geometry.coordinates);
        }
      });
    },
    async loadMap() {
      await this.loadCoords();
      console.log(this.coords);

      this.map.fitBounds(this.coord);

      this.marker = L.Marker.movingMarker(this.coord, 9000, {
        autostart: true,
      }).addTo(this.map);
      L.polyline(this.coord, { color: "red" }).addTo(this.map);
    },
  },
  async mounted() {
    this.initialiseMap();
    this.loadMap();
  },
};
</script>
<style>
#map {
  height: 500px;
  width: 100%;
}
section {
  height: 100%;
}
</style>
