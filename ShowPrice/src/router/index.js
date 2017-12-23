import Vue from 'vue'
import Router from 'vue-router'
import login from '@/components/login'
import topNav from '@/components/topNav'
import leftNav from '@/components/leftNav'
import busShow from '@/components/busShow'


Vue.use(Router)

export default new Router({
  routes: [
   
    {
      path: '/busShow',
      name: 'busShow',
      component: busShow
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/topNav',
      name: 'topNav',
      component: topNav
    },{
      path: '/leftNav',
      name: 'leftNav',
      component: leftNav
    }
  ]
})
