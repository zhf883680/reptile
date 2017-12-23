<template>
  <div id="app">
    <el-container id='divContent'>
      <el-header>
        <topNav></topNav>
      </el-header>
      <el-container>
        <el-aside>
          <leftNav></leftNav>
        </el-aside>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>

    <!-- <jdSearch></jdSearch>
    <jdChart></jdChart> -->
  </div>
</template>

<script>
// import jdSearch from './components/jd-search.vue'
// import jdChart from './components/jd-chart.vue'
import topNav from "./components/topNav.vue"
import leftNav from "./components/leftNav.vue"
export default {
  components: {
    topNav,
    leftNav
  }
};
</script>

<style scoped>
@media only screen and (max-width: 1366px) {
  #divContent {
   margin-left:100px;
    margin-right:100px;
  }
}
@media only screen and (min-width: 1367px) {
  #divContent {
    margin-left:15%;
    margin-right:15%;
  }
}
</style>
