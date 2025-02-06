<template>
  <v-main>
    <!-- Fixed v-card positioned at the top center of the screen -->
    <v-card class="mx-auto mt-11 custom-card" elevation="16" max-width="1150">
      <v-card-title class="title-background font-weight-black">
        <!-- Left Button (Show/Hide Analytics) -->
        <v-btn @click="toggleAnalytics">
          {{ showAnalytics ? "Hide Analytics" : "Analytics" }}
        </v-btn>

        <!-- Load Inventory Chart on Button Click -->
        <Analytics v-if="showAnalytics"/>

        <!-- Static Title Centered -->
        <span class="title-text"> Dashboard</span>

        <!-- Right Button (Update Stock Price by Category) -->
        <v-btn
            class="ml-4"
            @click="openStockPriceForm"
            outlined
        >
          Update Stock Price
        </v-btn>
      </v-card-title>

      <!-- Slot to inject content like the table -->
      <slot></slot>

      <!-- Conditionally render the UpdateStockPriceByCategory component -->
      <UpdateStockPriceByCategory v-if="isStockPriceFormVisible"/>
    </v-card>
  </v-main>
</template>

<script>
import {useInventoryStore} from "@/stores/InventoryStore"; // Import Pinia store
import UpdateStockPriceByCategory from "@/components/UpdateStockPriceByCategory.vue"; // Import the new component
import Analytics from "@/components/Analytics.vue";
import {ref} from "vue";
import {storeToRefs} from "pinia"; // Add this import

export default {
  name: 'ContentBox',
  components: {
    UpdateStockPriceByCategory, // Register the new component
    Analytics, // Register InventoryChart component
  },
  setup() {
    const inventoryStore = useInventoryStore(); // Access Pinia store

    // State for controlling visibility of UpdateStockPriceByCategory
    const isStockPriceFormVisible = ref(false);

    const {showAnalytics} = storeToRefs(inventoryStore); // Reactive state for showAnalytics

    // Function to toggle analytics visibility
    const toggleAnalytics = () => {
      inventoryStore.toggleAnalytics(); // Toggle the showAnalytics state
    };

    const openStockPriceForm = () => {
      isStockPriceFormVisible.value = true; // Show the update stock price form
      inventoryStore.openStockPriceForm("Electronics"); // Example: passing a category (optional)
    };

    return {
      openStockPriceForm,
      isStockPriceFormVisible, // Expose to template
      showAnalytics,
      toggleAnalytics, // Expose the toggle function to template
    };
  }
}
</script>

<style scoped>
.title-background {
  background-color: black;
  color: white;
  font-size: 24px;
  padding: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}

.title-text {
  flex-grow: 1;
  text-align: center;
}

.ml-4 {
  margin-left: 16px;
}

.custom-card {
  position: fixed; /* Fix the card in place */
  top: 20px; /* Set the distance from the top */
  left: 50%; /* Center it horizontally */
  transform: translateX(-50%); /* Adjust the card's position to be perfectly centered */
  z-index: 1000; /* Ensure it is on top of other elements */
  width: 100%; /* Adjust width if necessary */
  height: 100%
}

.v-main {
  margin-top: 160px; /* Provide space for the fixed card, so the content doesn't overlap */
}
</style>
