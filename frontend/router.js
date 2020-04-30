import Vue from 'vue'
import Router from 'vue-router'

import store from './store.js'

import Home from './components/Home.vue'
import Auth from './components/Auth.vue'
import Signup from './components/Signup.vue'
import Dashboard from './components/Dashboard.vue'

Vue.use(Router)

const router = new Router({
  routes: [
    { path: '/', component: Home },
    { path: '/login', component: Auth },
    { path: '/signup', component: Signup },
    { path: '/dashboard', component: Dashboard }
  ]
})

export default router

router.beforeEach((to, from, next) => {
  // Redirect to login if not logged in and trying to access a restricted page.
  const publicPages = ['/', '/login', '/signup']
  const authRequired = !publicPages.includes(to.path)

  if (authRequired && !store.state.auth.authenticated) return next('/login')
  next()
})
