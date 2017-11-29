import Vue from 'vue'
import Router from 'vue-router'
import Borrow from '@/components/views/Borrow'
import Login from '@/components/views/Login'
import Renew from '@/components/views/Renew'
import BookManage from '@/components/views/BookManage'
import Operator from '@/components/views/operator/Operator'
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
      path: '/operator',
      name: 'Operator',
      component: Operator
    },
    {
      path: '/renew/:account',
      name: 'Renew',
      component: Renew
    },
    {
      path: '/book_manage/:account',
      name: 'BookManage',
      component: BookManage
    }
  ]
})
