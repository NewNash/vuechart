import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    count:0,
    chartType:''
  },
  mutations: {
    increment(state){
      state.count++
    },
    test(state){
      state.chartType='test'
    },

  },
  actions: {
  },
  modules: {
  }
})
