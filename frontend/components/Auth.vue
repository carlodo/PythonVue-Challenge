<template>
  <div>
    <h2>{{$t('auth.loginTtl')}}</h2>
    <form @submit.prevent="Login">
      <div>
        <label for="email">{{$t('auth.email')}}</label>
        <input type="email" v-model="email" name="email" required/>
      </div>
      <div>
        <label for="password">{{$t('auth.password')}}</label>
        <input type="password" v-model="password" name="password" required/>
      </div>
      <div class="controls">
        <button>{{$t('auth.loginBut')}}</button>
        <p v-if="message">{{$t(message)}}</p>
      </div>
    </form>
    <p>
      {{$t('auth.register1')}}
      <router-link to="/signup" v-text="$t('auth.register2')"/>
    </p>
  </div>
</template>

<script>
import store from '../store.js'
import router from '../router.js'
import sha256 from 'js-sha256'

export const authSalt = 'code energy pepper'

export default {
  name: 'Login',
  data: () => ({
    email: '',
    password: '',
    message: ''
  }),
  created () {
    this.$store.dispatch('auth/logout')
  },

  methods: {
    Login () {
      this.message = 'auth.loginSub'
      const credentials = {
        email: this.email,
        password: sha256(authSalt + this.password)
      }
      const opts = {
        method: 'POST',
        headers: { 'Content-Type': 'application.json' },
        body: JSON.stringify(credentials)
      }
      fetch('/api/auth/', opts)
        .then(resp => {
          if (resp.status === 401) this.message = 'auth.err.badCredentials'
          return resp.json()
        })
        .then(resp => {
          if (resp.error) throw resp.error
          const authData = { email: this.email, token: resp.token }
          this.$store.dispatch('auth/login', authData)
          this.$router.push('/dashboard')
        })
        .catch(err => console.log(err))
    }
  }
}

export const AuthStore = {
  namespaced: true,
  state: { authenticated: false, token: null, email: null },

  mutations: {
    login (state, { token, email }) {
      state.authenticated = true
      state.token = token
      state.email = email
    },
    logout (state) {
      state.authenticated = false
      state.token = ''
      state.email = ''
    }
  },

  actions: {
    login ({ dispatch, commit }, authData) {
      commit('login', authData)
    },
    logout ({ dispatch, commit }) {
      commit('logout')
    }
  }
}

export function authFetch (url, options = {}) {
  const token = store.state.auth.token
  options.headers = options.headers || {}
  if (token) options.headers.Authorization = 'Bearer ' + token
  return fetch(url, options)
    .then(resp => {
      if ([401, 403].includes(resp.status)) router.push('/login')
      return resp
    })
}
</script>
