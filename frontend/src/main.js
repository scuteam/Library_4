// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import Axios from 'axios'
import 'element-ui/lib/theme-chalk/index.css'
Vue.config.productionTip = false
Axios.defaults.baseURL = 'http://127.0.0.1:8080'
Axios.defaults.withCredentials = true
Axios.headers = {'Access-Control-Allow-Origin': 'http://127.0.0.1:8080'}
Vue.prototype.$http = Axios
Vue.use(ElementUI)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
