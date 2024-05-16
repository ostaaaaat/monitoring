import { createRouter, createWebHistory } from 'vue-router'
import DownloadPage from './pages/DownloadPage.vue'
import GraphPage from './pages/GraphPage.vue'
import DiagramPage from './pages/DiagramPage.vue'
import HeatmapPage from './pages/HeatmapPage.vue'
import StatisticsPage from './pages/StatisticsPage.vue'
import ReportPage from './pages/ReportPage.vue'

const routes = [
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
  {
    path: '/statistics',
    name: 'Statistics',
    component: StatisticsPage
  },
  {
    path: '/report',
    name: 'Report',
    component: ReportPage
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router