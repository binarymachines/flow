<template>
  <div id="app">        
    <FlowForm/>
    
  </div>

</template>

<script>
import FlowForm from './components/FlowForm.vue'

export default {
  name: 'App',
  components: {
    FlowForm
  }
}
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
