// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import ElementUI from 'element-ui'
import Vuex from 'vuex'
import 'element-ui/lib/theme-chalk/index.css'

Vue.config.productionTip = false
//绑定vue 调用方法
// this.$http.get(`url`).then(m => {
//    let data = eval(m.data)
//    _this.count = data.data.Count
//     _this.onlineCount = data.data.OnlineCount
//   })
Vue.prototype.$http = axios
//全局变量
//axios.defaults.baseURL = "http://localhost:58166/"
//使用elementui样式
Vue.use(ElementUI)
//使用vuex
Vue.use(Vuex)
const store = new Vuex.Store({
  state: {
    id: '123123',
    prices: []
  },
  mutations: {
    getPrice(state) {
      if (state.id == 1) {
        axios.get("../static/prices.json").then((data) => {
          state.prices=[];
          data.data.prices.forEach((item) => {
            if (item.date == '2017-1-1')
            state.prices.push(item);
          })
        });
      }
      else if (state.id == 2) {
        axios.get("../static/prices.json").then((data) => {
          state.prices=[];
          data.data.prices.forEach((item) => {
            if (item.date == '2017-1-2')
            state.prices.push(item);
          });
        });
      }
      else {
        axios.get("../static/prices.json").then((data) => {
          state.prices=[];
          data.data.prices.forEach((item) => {
            if (item.date != '2017-1-1' && item.date != '2017-1-2')
            state.prices.push(item);
          });
        });
      }
    },
    updateId(state,id){
      state.id=id
    }
  }
})
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
