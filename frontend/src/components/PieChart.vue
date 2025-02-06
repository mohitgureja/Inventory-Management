<template>
  <div class="pie-chart-container">
    <Pie :data="chartData" :options="chartOptions" />
  </div>
</template>

<script>
import { Pie } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement, CategoryScale } from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale);

export default {
  name: 'PieChart',
  components: { Pie },
  props: {
    chartData: {
      type: Object,
      required: true,
    },
    chartOptions: {
      type: Object,
      default: () => ({}),
    },
  },
};
</script>
<style>
.pie-chart-container {
  width: 80%; /* You can set the percentage or px value depending on the size you want */
  height: 400px; /* Adjust this to control the height of the chart */
  padding-top: 55px;
}
</style>