<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <div id="app">
    <p>{{ message }}</p>
    <ul>
      <li v-for="item in data" :key="item">{{ item }}</li>
    </ul>
  </div>
  <HelloWorld msg="Vue.js + FastAPI"/>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  data() {
    return {
      message: "",
      data: [],
    };
  },
  async created() {
    // Fetch data from FastAPI
    const response = await fetch("http://0.0.0.0:8000/api/data");
    const result = await response.json();
    this.message = "Data from FastAPI:";
    this.data = result.data;
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
