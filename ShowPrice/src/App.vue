<template>
  <div id="app">
    <search></search>
    <chart></chart>
  </div>
</template>

<script>
//import axios from "axios";
import search from './components/search.vue'
import chart from './components/chart.vue'
export default {
  components:{
    search,
    chart
  }
};
</script>

<style>

</style>
