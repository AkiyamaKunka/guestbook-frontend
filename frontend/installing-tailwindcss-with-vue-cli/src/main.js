import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './assets/tailwindcss.css'
import axios from 'axios'

axios.defaults.withCredentials = true
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
axios.defaults.xsrfCookieName = 'csrftoken'

Vue.config.productionTip = false
Vue.prototype.$http = axios.create({
  baseURL: 'http://localhost:8001/',
  timeout: 3000,
  // headers: {'X-Custom-Header': 'foobar'}
});

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
// here is some update test