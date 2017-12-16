//引入vue及vuex
import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
Vue.use(Vuex)

//需要维护的状态
const state = {
    /*
        notes:存储note项
        activeNote:当前正在编辑的note项
    */
    id:0,
    shopPrice:{}
}

const mutations = {
    //添加笔记
    Get_Price(state,shopId){
			
    }
}

const actions = {
    /*
        actions处理函数接受一个 context 对象
        {
          state,     // 等同于 store.state, 若在模块中则为局部状态
          rootState, // 等同于 store.state, 只存在于模块中
          commit,    // 等同于 store.commit
          dispatch,  // 等同于 store.dispatch
          getters    // 等同于 store.getters
        }
    */
    addNote({commit}){
        commit('ADD_NOTE')
    }
}
const getters = {
    /*
        Getters 接受 state 作为其第一个参数
        state => state.notes为箭头函数等价于：
        function (state){
            return state.notes
        }
    */
  notes: state => state.notes,
  activeNote: state => state.activeNote
}

export default new Vuex.Store({
    state,
    mutations,
    actions,
    getters
})