import Vue from 'vue'
import Router from 'vue-router'
import Borrow from '@/components/views/Borrow'
import Login from '@/components/views/Login'
import Renew from '@/components/views/Renew'
import BookManage from '@/components/views/BookManage'
import Admin from '@/components/views/Admin'
import InnerOperator from '@/components/views/InnerOperator'
import UserManage from '@/components/views/UserManage'
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
      path: '/renew/:account',
      name: 'Renew',
      component: Renew
    },
    {
      path: '/book_manage/:account',
      name: 'BookManage',
      component: BookManage
    },
    {
      path: '/book_manage/:account',
      name: 'BookManage',
      component: BookManage
    },
    {
      path: '/innerOperator',
      name: 'InnerOperator',
      component: InnerOperator
    },
    {
      path: '/userManage',
      name: 'UserManage',
      component: UserManage
    },
    {
      path: '/admin',
      name: 'Admin',
      component: Admin
    }
  ]
})
