import { createRouter, createWebHistory } from 'vue-router'
import HomePage from './pages/HomePage.vue';
import DownloadPage from './pages/DownloadPage.vue'
import GraphPage from './pages/GraphPage.vue'
import DiagramPage from './pages/DiagramPage.vue'
import HeatmapPage from './pages/HeatmapPage.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage,
  },
  {
    path: '/download',
    name: 'Download',
    component: DownloadPage
  },
  {
    path: '/graph',
    name: 'Graph',
    component: GraphPage
  },
  {
    path: '/diagram',
    name: 'Diagram',
    component: DiagramPage
  },
  {
    path: '/heatmap',
    name: 'Heatmap',
    component: HeatmapPage
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
