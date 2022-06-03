<template>
<div class="row">
    <div class="col">
        <div class="input-group mx-auto" style="width: 700px;">
            <input v-model="query" @input="debouncedSearch"
            type="search" class="form-control rounded"
            placeholder="Введите описание товара"
            aria-label="Search" aria-describedby="search-addon"
            />
            <button type="button" class="btn btn-outline-success">Поиск</button>
        </div>
    </div>


</div>
</template>

<script>
import {mapActions, mapState} from 'vuex';
import debounce from 'lodash/debounce';

export default {
  name: 'search',
  computed: {
    ...mapState(['searchQuery']),
    query: {
      get() {
        return this.searchQuery;
      },
      set(val) {
        return this.setSearchQuery(val);
      }
    }
  },
  methods: {
    ...mapActions(['setSearchQuery', 'search']),
    debouncedSearch: debounce(function () {
      this.search();
    }, 500)
  }
};
</script>

<style>

</style>