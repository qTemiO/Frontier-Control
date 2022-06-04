import { createRouter, createWebHashHistory } from 'vue-router'
import CodeSearchHelper from '../views/CodeSearchHelper.vue'
import Documentation from '../views/Documentation.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    
    component: () => import(/* webpackChunkName: "about" */ '../views/MainPage.vue')
  },
  {
    path: '/tnved_classification/',
    name: 'main',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: CodeSearchHelper
  },
  {
    path: '/documentation/',
    name: 'documentation',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: Documentation
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
