import Vue from 'vue'
import VueRouter from 'vue-router'
import MapView from '../components/MapView.vue'
import LocationsList from '../components/LocationsList.vue'
import ItineraryView from '../components/ItineraryView.vue'
import Upload_file from '../components/Upload_file.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MapView',
    component: MapView
  },
  {
    path: '/locations',
    name: 'LocationsList',
    component: LocationsList
  },
  {
    path: '/itinerary',
    name: 'ItineraryView',
    component: ItineraryView
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
