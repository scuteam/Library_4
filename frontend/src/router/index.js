import Vue from 'vue'
import Router from 'vue-router'
import Borrow from '@/components/views/Borrow'
import Login from '@/components/views/Login'
import Renew from '@/components/views/Renew'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Borrow',
      component: Borrow
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/renew',
      name: 'Renew',
      component: Renew
    }
  ]
})
