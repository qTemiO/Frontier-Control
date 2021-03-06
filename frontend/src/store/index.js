import { createStore } from 'vuex'
import axios from 'axios'

const SET_SEARCH_QUERY = 'SET_SEARCH_QUERY';
const SET_LOADING = 'SET_LOADING';
const SET_RESULT_RES = 'SET_RESULT_RES';
const RESET_SEARCH = 'RESET_SEARCH';
const SET_PROBITY_RES = 'SET_PROBILITY_RES';
const SET_COMPLEX_RES = 'SET_COMPLEX_RES';

export default createStore({
  state: {
    state: {
      searchQuery: '',
      loading: false,
      tnved: 'null',
      probility: 'null',
      complex: 'null'
    },
  },
  getters: {

  },
  mutations: {
    [SET_SEARCH_QUERY]: (state, searchQuery) => state.searchQuery = searchQuery,
    [SET_PROBITY_RES]: (state, probility) => state.probility = probility,
    [SET_COMPLEX_RES]: (state, complex) => state.complex = complex,
    [SET_RESULT_RES]: (state, tnved) => state.tnved = tnved,
    [SET_LOADING]: (state, loading) => state.loading = loading,
    [RESET_SEARCH]: state => state.tnved = null,
    [RESET_SEARCH]: state => state.probility = null,
    [RESET_SEARCH]: state => state.complex = null,
    

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
        let probs = await axios.get(`http://localhost:8000/classificator/classificatorUser/${state.searchQuery}/`);
        commit(SET_PROBITY_RES, probs);
        let compl = await axios.get(`http://localhost:8000/main/complex/${state.searchQuery}/`);
        commit(SET_COMPLEX_RES, compl);
        console.log(compl)
      } catch (e) {
        commit(RESET_SEARCH);
      }
      commit(SET_LOADING, false);
    
  }},
  modules: {

  }
})
