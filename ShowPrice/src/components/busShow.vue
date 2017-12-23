<template>
    <div id="app">
        <el-row justify="center" type="flex">
            <el-col :span="12">
                <el-input placeholder="请输入苏州公交的线路号" v-model="line" clearable>
                </el-input>
            </el-col>
            <el-col :span="1"></el-col>
            <el-col :span="6">
                <el-button v-on:click="search">查询</el-button>
            </el-col>

        </el-row>
        <el-row justify="center" type="flex">
            <el-col :span="24">
                <div id="main" style="width:100%;height:500px;"></div>
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
      line: "",
      options: {
        title: {
          text: "",
          subtext: "纯属虚构"
        },
        tooltip: {
          trigger: "axis"
        },
        legend: {
          data: ["最晚时间", "最早时间"]
        },
        xAxis: {
          type: "category",
          boundaryGap: false,
          data: []
        },
        yAxis: {
          type: "value",
          axisLabel: {
            formatter: function(value) {
              var strVal = value + "";
              if (strVal.indexOf(".") == -1) {
                return strVal + ":00";
              } else {
                var arr = strVal.split(".");
                if (arr[1].length == 2) {
                  return strVal.replace(".", ":");
                } else {
                  return strVal.replace(".", ":") + "0";
                }
              }
            }
          }
        },
        series: [
          {
            name: "时间",
            type: "line",
            data: [],
            label: {
              normal: {
                formatter: function(params) {return params.value.replace(".", ":")},
                show:true
              }
            }
          }
        ]
      }
    };
  },

  methods: {
    search() {
      console.log(this.line);
      //设置options
      this.$http.get("../static/bus.json").then(data => {
        this.options.title.text = data.data.name;
        this.options.xAxis.data = [];
        this.options.series[0].data = [];
        data.data.times.forEach(item => {
          this.options.xAxis.data.push(item.date);
          this.options.series[0].data.push(item.time);
        });
        //加载数据
         this.showChart();
      });
      
     
    },
    showChart() {
      let echarts = require("echarts");
      let myChart = echarts.init(document.getElementById("main"));
      myChart.setOption(this.options);
    }
  },
  mounted() {
    this.$nextTick(function() {
      this.showChart();
    });
  }
};
</script>

<style>

</style>
