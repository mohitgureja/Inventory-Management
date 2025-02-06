import {defineStore} from 'pinia';
import axios from 'axios';

const BACKEND_URL = 'http://localhost:8000';
export const useInventoryStore = defineStore('inventory', {
    state: () => ({
        items: [],
        categories: [], // Categories will be an array of strings
        isNameFormVisible: false,
        isStockPriceFormVisible: false,
        categoryForPriceUpdate: null, // Track the category for price update
        showAnalytics: false,
        categoryStockData: [],
        valueData: [],
        insights: {},
    }),
    actions: {
        async fetchItems() {
            const response = await axios.get(BACKEND_URL + '/items');
            this.items = response.data.items;
        },
        async fetchStats() {
            try {
                const response = await axios.get(BACKEND_URL + '/inventory_stats');
                const stats = response.data;

                // Map the fetched data into the store's state
                this.categoryStockData = stats.category_stock_data;
                this.valueData = stats.value_data;
                this.insights = stats.insights;
            } catch (error) {
                console.error("Error fetching inventory stats:", error);
            }
        },
        async fetchCategories() {
            try {
                const response = await axios.get(BACKEND_URL + '/inventory_category');
                this.categories = response.data; // Now categories is an array of strings
            } catch (error) {
                console.error("Error fetching categories", error);
            }
        },
        async updateStockQuantity(item_id, new_quantity) {
            await axios.put(BACKEND_URL + '/update_stock_quantity', {
                item_id,
                new_quantity,
            });
            await this.fetchItems(); // Automatically refresh the inventory after updating
        },
        async updateStockPriceByCategory(category, new_price) {
            await axios.put(BACKEND_URL + '/update_stock_price_by_category', {
                category,
                new_price,
            });
            await this.fetchItems(); // Automatically refresh the inventory after updating
        },

        // Actions to control the visibility of the forms
        openStockPriceForm(category) {
            this.categoryForPriceUpdate = category; // Store the category for price update
            this.isStockPriceFormVisible = true;
        },
        closeStockPriceForm() {
            this.isStockPriceFormVisible = false;
            this.categoryForPriceUpdate = null; // Clear the stored category after closing the form
        },
        toggleAnalytics() {
            this.showAnalytics = !this.showAnalytics;
        },
    },
});
