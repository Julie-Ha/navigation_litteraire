import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import LocationsList from '../components/LocationsList.vue'

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
]

const router = new VueRouter({
  routes
})

export default router
