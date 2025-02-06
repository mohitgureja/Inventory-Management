<template>
  <v-container class="scrollable-table-container">
    <v-data-table
      :items="items"
      :headers="headers"
      hide-default-footer
      dense
      class="custom-data-table"
      item-key="item_id"
      :items-per-page="200"
    >
      <!-- Customizing the "Stock Quantity" column using v-slot -->
      <template v-slot:[`item.stock_quantity`]="{ item }">
        <!-- Display Stock Quantity and the edit icon next to it -->
        <span>{{ item.stock_quantity }}</span>
        <v-icon @click="openEditDialog(item)" class="edit-icon">mdi-pencil</v-icon>
      </template>
    </v-data-table>
  </v-container>

  <!-- Dialog to edit stock quantity -->
  <v-dialog v-model="isDialogVisible" max-width="500px">
    <v-card>
      <v-card-title class="headline">Edit Stock Quantity</v-card-title>
      <v-card-text>
        <v-form>
          <v-text-field
            v-model="editedItem.stock_quantity"
            label="Stock Quantity"
            type="number"
            outlined
            required
          ></v-text-field>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-btn @click="closeDialog" color="grey" text>Cancel</v-btn>
        <v-btn @click="submitForm" color="primary">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { useInventoryStore } from "@/stores/InventoryStore";
import { computed, onMounted, ref } from "vue";

export default {
  name: "InventoryList",
  setup() {
    const inventoryStore = useInventoryStore();

    // Reactive state for managing dialog visibility
    const isDialogVisible = ref(false);

    // Reactive object for the form fields
    const editedItem = ref({
      stock_quantity: "",
      item_id: null, // To track which item is being edited
    });

    // Fetch items on mount
    onMounted(() => {
      inventoryStore.fetchItems();
    });

    // Table headers, including the "Actions" column for the edit icon
    const headers = [
      { title: "Item Id", key: "item_id" },
      { title: "Category", key: "category" },
      { title: "Item Name", key: "item_name" },
      { title: "Price", key: "price" },
      { title: "Stock Quantity", key: "stock_quantity" },
    ];

    const items = computed(() => inventoryStore.items);

    // Open the dialog and pre-fill the fields with the item data
    const openEditDialog = (item) => {
      editedItem.value.item_id = item.item_id;
      editedItem.value.stock_quantity = item.stock_quantity;
      isDialogVisible.value = true;
    };

    // Close the dialog
    const closeDialog = () => {
      isDialogVisible.value = false;
    };

    // Submit the form data to update stock quantity
    const submitForm = async () => {
      await inventoryStore.updateStockQuantity(editedItem.value.item_id, editedItem.value.stock_quantity);
      closeDialog(); // Close the dialog after updating
    };

    return {
      inventoryStore,
      headers,
      items,
      isDialogVisible,
      editedItem,
      openEditDialog,
      closeDialog,
      submitForm,
    };
  },
};
</script>

<style scoped>
/* Styling for the edit icon */
.edit-icon {
  cursor: pointer;
  font-size: 24px;
  color: #1976d2;
  transition: color 0.3s ease;
  margin-left: 8px;
}

.edit-icon:hover {
  color: #1565c0;
}

.custom-data-table {
  /* No changes needed for the table itself */
}

/* Make sure the header sticks at the top and has a background */
.v-data-table .custom-data-table thead th {
  position: sticky !important;
  top: 0 !important;
  background-color: blue !important;  /* Optional: adjust this color */
  z-index: 1 !important;
}

/* Table container to ensure scroll */
.scrollable-table-container {
  max-height: 400px;
  overflow-y: auto;
  display: block; /* Ensure the table can scroll */
}
</style>
