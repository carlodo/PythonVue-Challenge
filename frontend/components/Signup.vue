<template>
  <div>
    <h2>{{$t('auth.signupTtl')}}</h2>
    <form @submit.prevent="Signup">
      <div>
        <label for="name">{{$t('auth.name')}}</label>
        <input type="text" v-model="name" name="name" required/>
      </div>
      <div>
        <label for="email">{{$t('auth.email')}}</label>
        <input type="email" v-model="email" name="email" required/>
      </div>
      <div>
        <label for="password">{{$t('auth.password')}}</label>
        <input type="password" v-model="password" name="password" required/>
      </div>
      <div>
        <label for="password">{{$t('auth.passcheck')}}</label>
        <input type="password" v-model="passcheck" name="passcheck" required/>
      </div>
      <div class="controls">
        <button>{{$t('auth.signupBut')}}</button>
        <p v-if="message">{{$t(message)}}</p>
      </div>
    </form>
  </div>
</template>

<script>
import sha256 from 'js-sha256'
import { authSalt } from './Auth.vue'

export default {
  name: 'Signup',
  data: () => ({
    name: '',
    email: '',
    password: '',
    passcheck: '',
    submitted: false,
    usernameTaken: false,
    passcheckFailed: false,
    message: ''
  }),
  created () {
    this.$store.dispatch('auth/logout')
  },
  methods: {
    Signup () {
      this.usernameTaken = false
      if (this.password !== this.passcheck) {
        this.message = 'auth.err.passcheckFailed'
      } else {
        this.message = 'auth.signupSub'
        const registration = {
          name: this.name,
          email: this.email,
          password: sha256(authSalt + this.password)
        }
        const opts = {
          method: 'POST',
          headers: { 'Content-Type': 'application.json' },
          body: JSON.stringify(registration)
        }
        fetch('/api/signup/', opts)
          .then(resp => {
            if (resp.status === 409) {
              this.message = 'auth.err.usernameTaken'
            } else {
              this.$router.push('/login')
            }
          })
      }
    }
  }
}
</script>
