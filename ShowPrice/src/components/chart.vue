<template>
	<div id="app">
		<el-row justify="center" type="flex">
			<el-col :span="24">
				<div id="main" style="width:100%;height:500px;"></div>
			</el-col>
		</el-row>
	</div>
</template>

<script>
export default {
  name: "app",
  data() {
    return {};
  },
  mounted() {
    this.$nextTick(function() {
      this.showChart();
      //let echarts = require("echarts");
      // 基于准备好的dom，初始化echarts实例
      // let myChart = echarts.init(document.getElementById("main"));
      // // 绘制图表
      // this.data.options.xAxis.data = Array.from(this.$store.state.prices, a => a.date);
      // //设置y轴
      // this.data.options.series[0].data = Array.from(
      //   this.$store.state.prices,
      //   a => a.price
      // );
      //显示图标
      // myChart.setOption(this.options);

      // this.$http.get("../static/prices.json").then((data) => {
      // 	//let dataJson=JSON.stringify(data.data);
      // 	options.title.text = data.data.name;//设置标题
      // 	//设置x轴
      // 	options.xAxis.data=Array.from(data.data.prices,a=>a.date)
      // 	//设置y轴
      // 	options.series[0].data=Array.from(data.data.prices,a=>a.price)
      // 	//显示图标
      //   myChart.setOption(options);
      // });
    });
  },
  computed: {
    options() {
      return {
        title: {
          text: "",
          subtext: "纯属虚构"
        },
        tooltip: {
          trigger: "axis"
        },
        legend: {
          data: ["最高价格", "最低价格"]
        },
        xAxis: {
          type: "category",
          boundaryGap: false,
          data: Array.from(this.$store.state.prices, a => a.date)
        },
        yAxis: {
          type: "value",
          axisLabel: {
            formatter: "{value}"
          }
        },
        series: [
          {
            name: "价格",
            type: "line",
            data: Array.from(this.$store.state.prices, a => a.price),
            markPoint: {
              data: [{ type: "max", name: "最大值" }, { type: "min", name: "最小值" }]
            }
          }
        ]
      };
    }
  },
  watch: {
    options(val) {
      this.showChart();
    }
  },
  // computed: {
  //   options: {
  //     get() {
  //       let options = {
  //         title: {
  //           text: "",
  //           subtext: "纯属虚构"
  //         },
  //         tooltip: {
  //           trigger: "axis"
  //         },
  //         legend: {
  //           data: ["最高价格", "最低价格"]
  //         },
  //         xAxis: {
  //           type: "category",
  //           boundaryGap: false,
  //           data: Array.from(this.$store.state.prices, a => a.date)
  //         },
  //         yAxis: {
  //           type: "value",
  //           axisLabel: {
  //             formatter: "{value}"
  //           }
  //         },
  //         series: [
  //           {
  //             name: "价格",
  //             type: "line",
  //             data: Array.from(this.$store.state.prices, a => a.price),
  //             markPoint: {
  //               data: [
  //                 { type: "max", name: "最大值" },
  //                 { type: "min", name: "最小值" }
  //               ]
  //             }
  //           }
  //         ]
  //       };
  //       return options;
  // 		},
  // 		set(){
  // 			alert('123');
  // 		}
  //   }
  // },
  methods: {
    showChart() {
      let echarts = require("echarts");
      let myChart = echarts.init(document.getElementById("main"));

      myChart.setOption(this.options);
    }
  }
};
</script>

<style>

</style>
