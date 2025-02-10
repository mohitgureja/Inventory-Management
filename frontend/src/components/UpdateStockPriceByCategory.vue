<template>
  <v-dialog v-model="inventoryStore.isStockPriceFormVisible" max-width="450">
    <v-card>
      <v-card-title>
        Update Stock Price by Category
      </v-card-title>

      <v-card-text>
        <v-form>
          <!-- Dropdown for selecting category -->
          <v-select 
            v-model="inventoryStore.selectedCategory" 
            :items="inventoryStore.categories" 
            label="Select Category" 
            outlined 
            required
          ></v-select>

          <!-- Input for new price -->
          <v-text-field 
            v-model="inventoryStore.newStockPrice" 
            label="New Price" 
            type="number" 
            outlined 
            required
          ></v-text-field>
        </v-form>
      </v-card-text>

      <v-card-actions>
        <v-btn @click="inventoryStore.closeStockPriceForm" color="secondary">Cancel</v-btn>
        <v-btn @click="updateStockPriceByCategory" color="primary">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { useInventoryStore } from "@/stores/InventoryStore";
import { onMounted } from "vue";

export default {
  name: "UpdateStockPriceByCategory",
  setup() {
    const inventoryStore = useInventoryStore();

    // Fetch categories when the component mounts
    onMounted(async () => {
      await inventoryStore.fetchCategories();
    });

    // Update stock price by category
    const updateStockPriceByCategory = async () => {
      if (inventoryStore.selectedCategory && inventoryStore.newStockPrice !== null) {
        await inventoryStore.updateStockPriceByCategory(
          inventoryStore.selectedCategory,
          inventoryStore.newStockPrice
        );
        inventoryStore.closeStockPriceForm();
      } else {
        alert("Please fill in both fields!");
      }
    };

    return {
      updateStockPriceByCategory,
      inventoryStore
    };
  },
};
</script>
