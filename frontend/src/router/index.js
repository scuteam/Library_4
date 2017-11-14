import Vue from 'vue'
import Router from 'vue-router'
import Borrow from '@/components/views/Borrow'
import Login from '@/components/views/Login'
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
    }
  ]
})
