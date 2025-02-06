<template>
  <v-dialog v-model="showAnalytics" max-width="800px">
    <v-card elevation="4">
      <v-card-title>
        <span class="text-h5 font-weight-bold">Inventory Analytics</span>
      </v-card-title>

      <v-card-text>
        <!-- Insights Table -->
        <div class="insights">
          <h3 class="text-xl font-semibold">Key Insights</h3>
          <table>
            <tr>
              <th>Metric</th>
              <th>Item</th>
              <th>Value</th>
            </tr>
            <tr>
              <td>Item with max Stock</td>
              <td>{{ insights?.max_stock?.item_name }}</td>
              <td>{{ insights?.max_stock?.stock_quantity }}</td>
            </tr>
            <tr>
              <td>Item with min Stock</td>
              <td>{{ insights?.min_stock?.item_name }}</td>
              <td>{{ insights?.min_stock?.stock_quantity }}</td>
            </tr>
            <tr>
              <td>Item with max Price</td>
              <td>{{ insights?.max_price?.item_name }}</td>
              <td>{{ insights?.max_price?.price }}</td>
            </tr>
            <tr>
              <td>Item with min Price</td>
              <td>{{ insights?.min_price?.item_name }}</td>
              <td>{{ insights?.min_price?.price }}</td>
            </tr>
          </table>
        </div>

        <!-- Loading state -->
        <v-progress-circular v-if="isLoading" indeterminate color="primary"></v-progress-circular>

        <!-- Charts -->
        <div class="chart-container">
          <BarChart :chartData="barChartData" :chartOptions="barChartOptions" />
          <PieChart :chartData="pieChartData" :chartOptions="pieChartOptions" />
        </div>
      </v-card-text>

      <v-card-actions>
        <v-btn @click="showAnalytics = false" color="primary">Close</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { useInventoryStore } from '@/stores/InventoryStore'; // Import Pinia store
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ArcElement } from "chart.js";
import { storeToRefs } from "pinia";
import BarChart from '@/components/BarChart.vue'; // Import the BarChart component
import PieChart from '@/components/PieChart.vue'; // Import the PieChart component

// Register Chart.js components
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ArcElement);

export default {
  name: "Analytics-Page",
  components: {
    BarChart,
    PieChart,
  },
  setup() {
    const inventoryStore = useInventoryStore(); // Use Pinia store
    const { showAnalytics, categoryStockData, valueData, insights } = storeToRefs(inventoryStore);

    // Fetch stats and handle loading state
    inventoryStore.fetchStats();

    return { showAnalytics, categoryStockData, valueData, insights }; // Bind store data to the component
  },
  computed: {
    // Bar chart data
    barChartData() {
      return {
        labels: this.categoryStockData.map(item => item.category),
        datasets: [
          {
            label: 'Stock Quantity',
            data: this.categoryStockData.map(item => item.stock_quantity),
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
        text: 'Total Stocks per Category', // Title for Bar Chart
        font: {
          size: 18, // Font size of the title
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
        labels: this.valueData.map(item => item.category),
        datasets: [
          {
            label: 'Inventory Value',
            data: this.valueData.map(item => item.inventory_value),
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
        text: 'Total Value per Category', // Title for Pie Chart
        font: {
          size: 18, // Font size of the title
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

<style scoped>
.chart-container {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  margin-top: 20px;
}

.insights {
  margin-bottom: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f4f4f4;
}
</style>