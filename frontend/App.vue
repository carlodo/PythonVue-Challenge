<template>
  <div id="app">
    <h1 id="logo">{{ $t('Moti') }}</h1>
    <main>
      <nav>
        <router-link to="/dashboard" v-if="email" v-text="$t('nav.dash')"/>
        <router-link to="/login" v-if="this.$route.path !== '/login'"
          v-text="email?$t('nav.logout'):$t('nav.login')"/>
        <select v-model="$i18n.locale">
          <option v-for="(lang, i) in langs" :key="`Lang${i}`" :value="lang">
            {{ lang }}
          </option>
        </select>
      </nav>
      <div v-if="email">{{$t('nav.loginMsg', {name: email})}}</div>
      <section>
        <router-view/>
      </section>
    </main>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: () => ({
    langs: ['en', 'fr', 'pt']
  }),

  computed: {
    email: function () { return this.$store.state.auth.email }
  }
}
</script>

<style>
body {
  background-color: #fcfcfc;
  color: #181818;
  width: 800px;
  margin: 26px auto 0;
  padding: 0 26px;
  font-family: Sans-Serif;
}
#logo {
  border: 2px dashed #d18d3d;
  margin: 0 10px 26px 0;
  padding: 1px 10px 5px;
  font-variant: small-caps;
  text-transform: lowercase;
  background-color: #ffdfba;
  color: #773608;
  letter-spacing: .05em;
  display: inline-block;
  float: left;
}
nav {
  margin-bottom: 5px;
}
nav a {
  font-variant: small-caps;
  text-transform: lowercase;
  text-decoration: none;
  margin-right: 10px;
  margin-bottom: 20px;
  font-size: 120%;
  line-height: 0;
}
nav a:hover {
  text-decoration: underline;
}
.router-link-exact-active {
  font-weight: bold;
}
section {
  clear: both;
}
button {
  padding: .5em 1em;
  background-color: #b55f15;
  color: white;
  border: none;
  border-radius: 2px;
}
input {
  padding: .5em .6em;
}
form > div {
  margin-bottom: .5em;
}
form > div > label {
  width: 10em;
  display: inline-block;
  text-align: right;
  margin: 0 1em 0 0;
}
form > .controls {
    margin: 1.5em 0 0 11em;
}
</style>
