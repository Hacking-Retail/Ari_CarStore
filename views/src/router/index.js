import { createRouter, createWebHistory } from 'vue-router';
import Index from '../views/index.vue';
import all from '../views/all.vue'

const routes = [
  {
    path: '/',
    name: 'Index',
    component: Index,
  },
  {
    path: '/all',
    name: 'all',

    component: () => import( '../views/all.vue'),
  },
  {
    path: '/filter',
    name:'filter'
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
