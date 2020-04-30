import Vue from 'vue'
import 'normalize.css'

import App from './App.vue'
import router from './router.js' // XXX: router must be imported before store
import store from './store.js'
import i18n from './i18n.js'

const vm = new Vue({
  i18n,
  store,
  router,
  render: h => h(App)
})
vm.$mount('#vue-main')
