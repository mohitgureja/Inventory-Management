import {defineStore} from 'pinia';
import axios from 'axios';

const BACKEND_URL = 'http://localhost:8000';
export const useInventoryStore = defineStore('inventory', {
    state: () => ({
        items: [],
        categories: [], 
        isStockPriceFormVisible: false,
        showAnalytics: false,
        categoryStockData: [],
        valueData: [],
        insights: {},
        isUpdateStockQDialogVisible: false,
        selectedCategory: null,
        newStockPrice: null
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
                this.categories = response.data;
            } catch (error) {
                console.error("Error fetching categories", error);
            }
        },
        async updateStockQuantity(item_id, new_quantity) {
            await axios.put(BACKEND_URL + '/update_stock_quantity', {
                item_id,
                new_quantity,
            });
            await this.fetchItems();
        },
        async updateStockPriceByCategory(category, new_price) {
            await axios.put(BACKEND_URL + '/update_stock_price_by_category', {
                category,
                new_price,
            });
            await this.fetchItems();
        },
        closeStockPriceForm() {
            this.isStockPriceFormVisible = false;
            this.selectedCategory = null;
            this.newStockPrice = null
        },
        toggleAnalytics() {
            this.showAnalytics = !this.showAnalytics;
        },
        toggleUpdatetockQDialog() {
            this.isUpdateStockQDialogVisible = !this.isUpdateStockQDialogVisible;
        },
        toggleStockPriceUpdateDialog() {
            this.isStockPriceFormVisible = !this.isStockPriceFormVisible
        }
    },
});
