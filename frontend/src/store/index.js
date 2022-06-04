import { createStore } from 'vuex'
import axios from 'axios'

const SET_SEARCH_QUERY = 'SET_SEARCH_QUERY';
const SET_LOADING = 'SET_LOADING';
const SET_RESULT_RES = 'SET_RESULT_RES';
const RESET_SEARCH = 'RESET_SEARCH';
const SET_PROBITY_RES = 'SET_PROBILITY_RES';

export default createStore({
  state: {
    state: {
      searchQuery: '',
      loading: false,
      tnved: 'null',
      probility: 'null'
    },
  },
  getters: {

  },
  mutations: {
    [SET_SEARCH_QUERY]: (state, searchQuery) => state.searchQuery = searchQuery,
    [SET_LOADING]: (state, loading) => state.loading = loading,
    [SET_RESULT_RES]: (state, tnved) => state.tnved = tnved,
    [RESET_SEARCH]: state => state.tnved = null,
    [SET_PROBITY_RES]: (state, prop) => state.probility = prop
  },
  actions: {
    setSearchQuery({commit}, searchQuery) {
      commit(SET_SEARCH_QUERY, searchQuery);
    },
    async search({commit, state}) {
      commit(SET_LOADING, true);
      try {
        const {data} = await axios.get(`http://localhost:8000/filter/recommendUser/${state.searchQuery}/`);
        commit(SET_RESULT_RES, data);
        let props = await axios.get(`http://localhost:8000/classificator/classificatorUser/${state.searchQuery}/`);
        commit(SET_PROBITY_RES, props);
        console.log(props)
      } catch (e) {
        commit(RESET_SEARCH);
      }
      commit(SET_LOADING, false);
    
  }},
  modules: {

  }
})
