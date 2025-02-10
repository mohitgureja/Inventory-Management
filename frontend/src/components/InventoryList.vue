<template>
  <v-container class="scrollable-table-container">
    <v-data-table :items="inventoryStore.items" :headers="headers" fixed-header hide-default-footer dense item-key="item_id"
      :items-per-page="200" height="440px">

      <!-- Customizing the "Stock Quantity" column using v-slot -->
      <template v-slot:[`item.stock_quantity`]="{ item }">
        <span>{{ item.stock_quantity }}</span>
        <v-icon @click="openEditDialog(item)" class="edit-icon" color="black" size="18">
          mdi-pencil
        </v-icon>
      </template>
    </v-data-table>
  </v-container>

  <!-- Dialog to edit stock quantity -->
  <v-dialog v-model="inventoryStore.isUpdateStockQDialogVisible" max-width="500px">
    <v-card>
      <v-card-title class="headline">Edit Stock Quantity</v-card-title>
      <v-card-text>
        <v-form>
          <v-text-field v-model="editedItem.stock_quantity" label="Stock Quantity" type="number" outlined
            required></v-text-field>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-btn @click="inventoryStore.toggleUpdatetockQDialog" color="grey" text>Cancel</v-btn>
        <v-btn @click="updateForm" color="primary">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { useInventoryStore } from "@/stores/InventoryStore";
import { onMounted, ref } from "vue";

export default {
  name: "InventoryList",
  setup() {
    const inventoryStore = useInventoryStore();

    // Reactive object for the form fields
    const editedItem = ref({
      stock_quantity: "",
      item_id: null,
    });

    // Fetch items on mount
    onMounted(() => {
      inventoryStore.fetchItems();
    });

    const headers = [
      { title: "Item Id", key: "item_id" },
      { title: "Category", key: "category" },
      { title: "Item Name", key: "item_name" },
      { title: "Price", key: "price" },
      { title: "Stock Quantity", key: "stock_quantity" },
    ];

    // Open the dialog and pre-fill the fields with the item data
    const openEditDialog = (item) => {
      editedItem.value.item_id = item.item_id;
      editedItem.value.stock_quantity = item.stock_quantity;
      inventoryStore.isUpdateStockQDialogVisible = true;
    };

    // Submit the form data to update stock quantity
    const updateForm = async () => {
      await inventoryStore.updateStockQuantity(editedItem.value.item_id, editedItem.value.stock_quantity);
      inventoryStore.isUpdateStockQDialogVisible = false
    };

    return {
      inventoryStore,
      headers,
      editedItem,
      openEditDialog,
      updateForm,
    };
  },
};
</script>

<style>
.edit-icon {
  margin-left: 10px;
  cursor: pointer;
}


</style>
