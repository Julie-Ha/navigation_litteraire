<template>
  <div class="home">
    {{ text }}
    <Map v-if="locations" :locations="locations" />
  </div>
</template>

<script>
import Map from "./Map.vue";
import axios from "axios";

export default {
  name: "Home",
  components: {
    Map,
  },
  data() {
    return {
      text: "Six mois se passèrent encore ; et, l’année d’après, Charles fut définitivement envoyé au collège de Rouen, où son père l’amena lui-même, vers la fin d’octobre, à l’époque de la foire Saint-Romain.",
      locations: "",
    };
  },
  async created() {
    await axios
      .get("http://127.0.0.1:5000/get-annotated-text?text=" + this.text)
      .then((response) => {
        this.locations = response.data;
      })
      .catch((e) => {
        this.errors.push(e);
      });
  },
};
</script>
