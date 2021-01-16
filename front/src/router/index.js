import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import LocationsList from '../components/LocationsList.vue'
import ItineraryView from '../components/ItineraryView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
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
]

const router = new VueRouter({
  routes
})

export default router
