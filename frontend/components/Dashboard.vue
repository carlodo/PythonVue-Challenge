<template>
  <div>
    <div>
      <p>{{message}}</p>
    </div>
  </div>
</template>

<script>
import { authFetch } from './Auth.vue'

export default {
  name: 'Dashboard',
  data: () => ({ message: '' }),
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
          }
        })
        .catch(err => console.log(err))
    }
  }
}
</script>
