import Vue from 'vue'
import VueRouter from 'vue-router'
import MapText from '../components/MapText.vue'
import ItineraryLocations from '../components/ItineraryLocations.vue'
import MapLocations from '../components/MapLocations.vue'
import ItineraryText from '../components/ItineraryText.vue'
import Upload_file from '../components/Upload_file.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MapText',
    component: MapText
  },
  {
    path: '/maptext',
    name: 'MapText',
    component: MapText
  },
  {
    path: '/maplocations',
    name: 'MapLocations',
    component: MapLocations
  },
  {
    path: '/itinerarytext',
    name: 'ItineraryText',
    component: ItineraryText
  },
  {
    path: '/itinerarylocations',
    name: 'ItineraryLocations',
    component: ItineraryLocations
  },
  {
    path: '/upload',
    name: 'upload',
    component: Upload_file
  },
]

const router = new VueRouter({
  routes
})

export default router
