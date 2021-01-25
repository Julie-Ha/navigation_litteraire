<template>
  <div class="itinerary">
    <Locations :normalmap="true"/>
  </div>
</template>

<script>
import Locations from "./Locations";

export default {
  name: "Home",
  components: {
    Locations
  },
};
</script>