<template>
  <div>
    <div>
      <br />
    </div>
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
      setTimeout(() => {
        this.loadCoords();
      }, 1000);
      setTimeout(() => {
        this.initialiseMap();
        this.loadMap();
      }, 2000);
    },
  },
  methods: {
    async initialiseMap() {
      if(this.map) {
        this.map.remove();
      }
      
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
          maxZoom: 5,
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
          this.coords.push([
            j.features[0].geometry.coordinates[1],
            j.features[0].geometry.coordinates[0],
          ]);
        }
      });
    },
    async loadMap() {
      this.marker = null;
      if (this.coords.length > 1) {
        this.map.fitBounds(this.coords);
        this.marker = L.Marker.movingMarker(this.coords, 9000, {
          autostart: true,
        }).addTo(this.map);
        L.polyline(this.coords, { color: "red" }).addTo(this.map);
      }
    },
  },
  async created() {
    setTimeout(() => {
      this.loadCoords();
    }, 1000);
    setTimeout(() => {
      this.initialiseMap();
      this.loadMap();
    }, 2000);
  },
};
</script>
<style>
#map {
  height: 500px;
  width: 100%;
}

/* .map {
  z-index: -1;
} */

section {
  height: 100%;
}
</style>