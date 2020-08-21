import Vue from 'vue';
import Router from 'vue-router';
import NotFound from './components/NotFound.vue';
import Cars from './components/Cars.vue'

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Cars',
      component: Cars,
    },
    {
      path: '*',
      name: 'NotFount',
      component: NotFound,
    }
  ],
});
