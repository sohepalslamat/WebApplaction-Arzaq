import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueCookies from 'vue-cookies'
import VueRouter from 'vue-router'
import routes from './routes'
import store from './store/store'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import { ModalPlugin } from 'bootstrap-vue'

Vue.use(BootstrapVue)
Vue.use(ModalPlugin)

window.$ = window.jQuery = require('jquery');
Vue.use({
  install: function(Vue){
      Vue.prototype.$jQuery = require('jquery'); // you'll have this.$jQuery anywhere in your vue project
}});
Vue.config.productionTip = false

Vue.use(VueCookies)
VueCookies.config('7d')

Vue.use(VueRouter)
const router = new VueRouter({
  mode:'history',
  routes: routes

});
var base1 = axios.create({
  baseURL: 'http://127.0.0.1:8000/',
      
})
var base = axios.create({
  baseURL: 'http://127.0.0.1:8000/',
      
})
base.interceptors.request.use((config) => {
  config.headers = {'Authorization':'Token '+ window.$cookies.get('user').Authorization};
  return config;
 });

Vue.prototype.$http = base
Vue.prototype.$https = base1


new Vue({
  render: h => h(App),
  router,
  store
}).$mount('#app')
