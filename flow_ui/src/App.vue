<template>
  <div id="app">        
    <Table/>
    <div>
      <b-button-toolbar aria-label="Toolbar">
        <b-button-group class="mx-1">
          <b-col lg="4" class="pb-2"><b-button variant="success">New</b-button></b-col>
          <b-col lg="4" class="pb-2"><b-button>Submit</b-button></b-col>
        </b-button-group>
      </b-button-toolbar>
    </div>
  </div>
  

</template>

<script>
import Table from './components/Table.vue'

export default {
  name: 'App',
  components: {
    Table
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
