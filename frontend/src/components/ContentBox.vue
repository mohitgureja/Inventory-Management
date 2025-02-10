<template>
  <v-main>
    <!-- Fixed v-card positioned at the top center of the screen -->
    <v-card class="mx-auto mt-11 custom-card">
      <v-card-title class="title-background font-weight-black">

        <!-- Left Button (Show/Hide Analytics) -->
        <v-btn @click="inventoryStore.toggleAnalytics"> Analytics</v-btn>
        <Analytics v-if="inventoryStore.showAnalytics" />

        <!-- Static Title Centered -->
        <span class="title-text"> Dashboard</span>

        <!-- Right Button (Update Stock Price by Category) -->
        <v-btn @click="inventoryStore.toggleStockPriceUpdateDialog">
          Update Stock Price
        </v-btn>
        <UpdateStockPriceByCategory v-if="inventoryStore.isStockPriceFormVisible" />
      </v-card-title>

      <!-- Slot to inject content -->
      <slot></slot>
    </v-card>
  </v-main>
</template>

<script>
import { useInventoryStore } from "@/stores/InventoryStore";
import UpdateStockPriceByCategory from "@/components/UpdateStockPriceByCategory.vue";
import Analytics from "@/components/Analytics.vue";

export default {
  name: 'ContentBox',
  components: {
    UpdateStockPriceByCategory,
    Analytics,
  },
  setup() {
    const inventoryStore = useInventoryStore();

    return {
      inventoryStore,
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
  align-items: center;
}

.title-text {
  flex-grow: 1;
  text-align: center;
}

.custom-card {
  position: fixed;
  /* Fix the card in place */
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  /* Adjust the card's position to be perfectly centered */
  width: 100%;
}
</style>
