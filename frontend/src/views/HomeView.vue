<template>
<div>
  <header id="maskText"> div</header>
  <NavbarVue></NavbarVue>
  <div class="background">
  <div class="container">
    <div class="row">
      <div class="col">
              <BarChart></BarChart>
      </div>
      <div class="col">
            <RadarChart></RadarChart>
      </div>
      <div class="col">
        <div class="row">
            <D3BarChart></D3BarChart>
        </div>
        <div class="row">
            <RadarChart></RadarChart>
        </div>
            
      </div>
      <div class="col"></div>
    </div>
  </div>
  </div>
  <footer>Яйца</footer>
  </div>
</template>

<script>

import D3BarChartVue from '@/components/charts/D3BarChart.vue'
import RadarChart from '../components/charts/RadarChart.vue'
import NavbarVue from '../components/Navbar.vue'
import BarChart from '../components/charts/BarChart.vue'
import D3BarChart from '@/components/charts/D3BarChart.vue'
export default {
components: { NavbarVue, BarChart, RadarChart, D3BarChartVue, D3BarChart }
}
</script>

<style>
.background{
  background-color: #adaaa9;
}
#maskText h1 {
    font-size: 56px;
    font-family: 'Lilita One', sans-serif;
    color: #ffe400;
    text-shadow: 7px 7px 0px #34495e;
    text-transform: uppercase;
    text-align: center;
    margin: 0;
    display: block;
    -webkit-mask-image: url('../assets/penis.png');
    -webkit-transition:all 2s ease;
    -moz-transition:all 2s ease;
    -o-transition:all 2s ease;
    transition:all 2s ease;
    background-color: brown;
}
    #maskText h1:hover{
    -webkit-mask-image: url('../assets/logo.png');
    cursor: pointer;
    color: #ffe400;
    background-color: brown;
}
</style>