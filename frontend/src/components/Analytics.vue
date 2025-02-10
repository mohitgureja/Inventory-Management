<template>
  <v-dialog v-model="inventoryStore.showAnalytics" max-width="800px">
    <v-card>
      <v-card-title class="d-flex justify-center align-center">
        <span class="text-h5 font-weight-bold">Inventory Analytics</span>
      </v-card-title>

      <v-card-text>
        <!-- Insights Table -->
        <table>
          <thead>
            <tr>
              <th>Metric</th>
              <th>Item</th>
              <th>Value</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Item with Maximum Stock</td>
              <td>{{ inventoryStore.insights?.max_stock?.item_name }}</td>
              <td>{{ inventoryStore.insights?.max_stock?.stock_quantity }}</td>
            </tr>
            <tr>
              <td>Item with Minimum Stock</td>
              <td>{{ inventoryStore.insights?.min_stock?.item_name }}</td>
              <td>{{ inventoryStore.insights?.min_stock?.stock_quantity }}</td>
            </tr>
            <tr>
              <td>Item with Maximum Price</td>
              <td>{{ inventoryStore.insights?.max_price?.item_name }}</td>
              <td>{{ inventoryStore.insights?.max_price?.price }}</td>
            </tr>
            <tr>
              <td>Item with Minimum Price</td>
              <td>{{ inventoryStore.insights?.min_price?.item_name }}</td>
              <td>{{ inventoryStore.insights?.min_price?.price }}</td>
            </tr>
          </tbody>
        </table>

        <!-- Charts -->
        <div class="bar-chart-container">
          <Bar :data="barChartData" :options="barChartOptions" />
        </div>
        <div class="pie-chart-container">
          <Pie :data="pieChartData" :options="pieChartOptions" />
        </div>
      </v-card-text>

      <v-card-actions>
        <v-btn @click="inventoryStore.toggleAnalytics" color="primary">Close</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { useInventoryStore } from '@/stores/InventoryStore';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ArcElement } from "chart.js";
import { onMounted } from "vue";
import { Bar, Pie } from 'vue-chartjs';

// Register Chart.js components
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ArcElement);
ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale);

export default {
  name: "Analytics-Page",
  components: {
    Pie,
    Bar
  },
  setup() {
    const inventoryStore = useInventoryStore();

    // Fetch insights when the component mounts
    onMounted(async () => {
      await inventoryStore.fetchStats();
    });

    return { inventoryStore };
  },
  computed: {
    // Bar chart data
    barChartData() {
      return {
        labels: this.inventoryStore.categoryStockData.map(item => item.category),
        datasets: [
          {
            label: 'Stock Quantity',
            data: this.inventoryStore.categoryStockData.map(item => item.stock_quantity),
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1,
          },
        ],
      };
    },
    barChartOptions() {
      return {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true,
          },
        },
        plugins: {
          title: {
            display: true,
            text: 'Total Stocks per Category',
            font: {
              size: 18,
            },
            padding: {
              top: 10,
              bottom: 30,
            },
          },
        },
      };
    },

    // Pie chart data
    pieChartData() {
      return {
        labels: this.inventoryStore.valueData.map(item => item.category),
        datasets: [
          {
            label: 'Inventory Value',
            data: this.inventoryStore.valueData.map(item => item.inventory_value),
            backgroundColor: [
              'rgba(255, 99, 132, 0.2)',
              'rgba(54, 162, 235, 0.2)',
              'rgba(255, 206, 86, 0.2)',
              'rgba(75, 192, 192, 0.2)',
              'rgba(153, 102, 255, 0.2)',
              'rgba(255, 159, 64, 0.2)',
              'rgba(199, 199, 199, 0.2)',
            ],
            borderColor: [
              'rgba(255, 99, 132, 1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              'rgba(75, 192, 192, 1)',
              'rgba(153, 102, 255, 1)',
              'rgba(255, 159, 64, 1)',
              'rgba(199, 199, 199, 1)',
            ],
            borderWidth: 1,
          },
        ],
      };
    },
    pieChartOptions() {
      return {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          title: {
            display: true,
            text: 'Total Value per Category',
            font: {
              size: 18,
            },
            padding: {
              top: 10,
              bottom: 30,
            },
          },
        },
      };
    },
  },
};
</script>

<style>
table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f4f4f4;
}

.bar-chart-container {
  width: 90%;
  height: 400px; 
  margin-top: 40px;
  padding-left: 15%; 
}


.pie-chart-container {
  width: 90%;
  height: 400px;
  margin-top: 60px;
  padding-left: 15%; 
}
</style>