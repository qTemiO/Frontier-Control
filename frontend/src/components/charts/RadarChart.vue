<template>
  
  <div class="card shadow rounded me-auto">
                  <Radar :chart-data="chartData" />
                  <div class="card-body">
                    <h5 class="card-title">Radar chart</h5>
                    <p class="card-text">Воздуханский текст</p>
                  </div>
                  <ul class="list-group list-group-flush">
                    <li class="list-group-item">An item</li>
                  </ul>
                </div>
  
</template>

<script>
import { Radar } from 'vue-chartjs'
import { Chart as ChartJS, Title,  Tooltip,  Legend,  PointElement, RadialLinearScale,  LineElement,  Plugin} from 'chart.js'

ChartJS.register( Title, Tooltip,  Legend,  PointElement,  RadialLinearScale,  LineElement)

export default {
    name: 'RadarChart',
  components: {
    Radar
  },
  data(){
      return {
          chartData: {
      labels: ['Eating','Drinking','Sleeping','Designing','Coding', 'Cycling', 'Running'],
      datasets: [
        {
          label: 'My First dataset',
          backgroundColor: 'rgba(179,181,198,0.2)',
          borderColor: 'rgba(179,181,198,1)',
          pointBackgroundColor: 'rgba(179,181,198,1)',
          pointBorderColor: '#fff',
          pointHoverBackgroundColor: '#fff',
          pointHoverBorderColor: 'rgba(179,181,198,1)',
          data: [65, 59, 90, 81, 56, 55, 40]
        },
        {
          label: 'My Second dataset',
          backgroundColor: 'rgba(255,99,132,0.2)',
          borderColor: 'rgba(255,99,132,1)',
          pointBackgroundColor: 'rgba(255,99,132,1)',
          pointBorderColor: '#fff',
          pointHoverBackgroundColor: '#fff',
          pointHoverBorderColor: 'rgba(255,99,132,1)',
          data: [28, 48, 40, 19, 96, 27, 100]
        }
      ]
    },

    chartOptions : {
      responsive: true,
      maintainAspectRatio: false
    }

      }
  }
}
</script>

<style>

</style>