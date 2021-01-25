<template>
  <div class="itinerary">
    <Locations :normalmap="false"/>
  </div>
</template>

<script>
import Locations from "./Locations";

export default {
  name: "ItineraryText",
  components: {
    Locations
  },
};
</script>