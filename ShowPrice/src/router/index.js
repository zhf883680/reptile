import Vue from 'vue'
import Router from 'vue-router'
import search from '@/components/search'
import login from '@/components/login'
import chart from '@/components/chart'
import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/search',
      name: 'search',
      component: search
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/chart',
      name: 'chart',
      component: chart
    }
  ]
})
