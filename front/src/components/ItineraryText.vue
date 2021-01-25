<template>
  <div class="itinerary">
    <TextView :normalmap="false"/>
  </div>
</template>

<script>
import TextView from "./TextView";

export default {
  name: "ItineraryText",
  components: {
    TextView
  },
};
</script>