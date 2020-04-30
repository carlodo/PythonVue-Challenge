<template>
  <div>
    <div>
      <p>{{message}}</p>
      <input v-model="motto" @keyup="update" placeholder="Your motto" />
    </div>
  </div>
</template>

<script>
import { authFetch } from './Auth.vue'

export default {
  name: 'Dashboard',
  data: () => ({ message: '', motto: '' }),
  created () { this.dashboard() },
  methods: {
    dashboard () {
      authFetch('/api/dashboard/')
        .then(resp => resp.json())
        .then(resp => {
          if (resp.error) {
            this.message = resp.error
          } else {
            this.message = resp.name
            this.motto = resp.motto
          }
        })
        .catch(err => console.log(err))
    },
    update () {
      const opts = {
        method: 'POST',
        headers: { 'Content-Type': 'application.json' },
        body: JSON.stringify({ motto: this.motto })
      }
      authFetch('/api/dashboard/', opts)
        .catch(err => console.log(err))
    }
  }
}
</script>
