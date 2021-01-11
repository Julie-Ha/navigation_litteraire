<template>
  <div class="home">
    <div class="row">
      <div class="col-sm-6">
        <div v-html="text">{{ text }}</div>
      </div>
      <div class="col-sm-6 offset-sm-6 fixed-top">
        <Map v-if="locations" :locations="locations" />
      </div>
    </div>
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
        console.log(response.data);
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
