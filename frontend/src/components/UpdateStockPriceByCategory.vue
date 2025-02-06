<template>
  <v-card class="price-update-card" elevation="2" v-if="isFormVisible">
    <v-card-title class="headline">
      Update Stock Price by Category
    </v-card-title>

    <v-card-text>
      <v-form>
        <!-- Dropdown for selecting category -->
        <v-select
          v-model="categoryPriceForm.category"
          :items="categories"
          label="Select Category"
          outlined
          required
        ></v-select>

        <!-- Input for new price -->
        <v-text-field
          v-model="categoryPriceForm.new_price"
          label="New Price"
          type="number"
          outlined
          required
        ></v-text-field>
      </v-form>
    </v-card-text>

    <v-card-actions>
      <v-btn @click="updateStockPriceByCategory" color="primary">Save</v-btn>
      <v-btn @click="cancelForm" color="secondary">Cancel</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { useInventoryStore } from "@/stores/InventoryStore";
import { ref, computed, onMounted } from "vue";

export default {
  name: "UpdateStockPriceByCategory",
  setup() {
    const inventoryStore = useInventoryStore();

    // Reactive form data
    const categoryPriceForm = ref({
      category: "",
      new_price: null,
    });

    // Fetch categories when the component mounts
    onMounted(async () => {
      await inventoryStore.fetchCategories();  // Fetch categories from the API
    });

    // Computed property to access form visibility from the store
    const isFormVisible = computed(() => inventoryStore.isStockPriceFormVisible);

    // Access categories from the store
    const categories = computed(() => inventoryStore.categories);

    // Update stock price by category
    const updateStockPriceByCategory = async () => {
      if (categoryPriceForm.value.category && categoryPriceForm.value.new_price !== null) {
        await inventoryStore.updateStockPriceByCategory(
          categoryPriceForm.value.category,
          categoryPriceForm.value.new_price
        );
        categoryPriceForm.value.category = ""; // Reset form
        categoryPriceForm.value.new_price = null;
        inventoryStore.closeStockPriceForm(); // Close the form after saving
      } else {
        alert("Please fill in both fields!");
      }
    };

    // Cancel form (close it)
    const cancelForm = () => {
      inventoryStore.closeStockPriceForm(); // Close the form
    };

    return {
      categoryPriceForm,
      updateStockPriceByCategory,
      cancelForm,
      isFormVisible,
      categories,
    };
  },
};
</script>

<style scoped>
/* Styling for the card at the center */
.price-update-card {
  position: fixed;
  top: 50%;            /* Position it in the vertical center */
  left: 50%;           /* Position it in the horizontal center */
  transform: translate(-50%, -50%); /* Adjust for true center alignment */
  width: 400px;        /* Set a fixed width */
  padding: 16px;
  z-index: 1000;       /* Ensure it appears above other content */
}
</style>
