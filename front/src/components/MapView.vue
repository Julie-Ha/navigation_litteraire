<template>
  <div class="itinerary">
    <TextView :normalmap="true"/>
  </div>
</template>

<script>
import TextView from "./TextView";

export default {
  name: "Home",
  components: {
    TextView
  },
};
</script>