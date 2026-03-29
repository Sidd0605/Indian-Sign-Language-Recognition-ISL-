import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Dashboard from "../views/Dashboard.vue"
import AboutUs from "../views/AboutUs.vue"
import ProjectDetails from "../views/ProjectDetails.vue"
import Crop from "../views/Crop.vue"
import Result from "../views/Result.vue"
import Register from "../views/Register.vue"

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path:'/dashboard',
    name: "Dashboard",
    component: Dashboard,
  },
  {
    path: '/aboutus',
    name: 'AboutUs',
    component: AboutUs,
  },
  {
    path:'/projectdetails',
    name: "ProjectDetails",
    component: ProjectDetails
  },
  {
    path: '/crop/:crop_name', // <-- Update the path
    name: "Crop",
    component: Crop
  },
  {
    path: '/result', // <-- Update the path
    name: "Result",
    component: Result
  },
  {
    path: '/register',
    name: "Register",
    component: Register
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
