<template>
  <div class="home">
    <div v-html="text">{{ text }}</div>
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
      text: "text",
      locations: "",
    };
  },
  async created() {
    await axios
      .get("http://127.0.0.1:5000/get-annotated-text?text=" + this.text)
      .then((response) => {
        console.log(response.data)
        this.locations = response.data.locations;
        this.text = response.data.text;
      })
      .catch((e) => {
        this.errors.push(e);
      });
  },
};
</script>
<style>
.loc {
  color: red;
  font-weight: bold;
}
</style>