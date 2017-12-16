<template>
  <div id="app">
    <el-row justify="center" type="flex">
      <el-col :span="12">
        <el-input placeholder="请输入京东链接,如:https://item.jd.com/15806736305.html" v-model="jdurl" clearable>
        </el-input>
      </el-col>
      <el-col :span="1"></el-col>
      <el-col :span="6">
        <el-button v-on:click="search">查询</el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
//import axios from "axios";
export default {
  name: "app",
  data() {
    return {
    };
  },
  methods: {
    search: function(event) {
      // `this` 在方法里指向当前 Vue 实例
      // this.$http
      //   .post("GetAPI.ashx", "action=get&id=" + this.jdurl)
      //   .then(data => alert(data.data));
      this.$store.commit("getPrice");
    }
  },
  computed: {
    jdurl: {
      get() {
        return this.$store.state.id
      },
      set(value) {
        this.$store.commit("updateId", value);
      }
    }
  }
};
</script>

<style>

</style>
