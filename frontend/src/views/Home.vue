<template>
  <ContentBox>

          <InventoryList />

  </ContentBox>
</template>

<script>
import ContentBox from "@/components/ContentBox.vue";
import InventoryList from "@/components/InventoryList.vue";

export default {
  name: "HomePage",
  components: {
    ContentBox,
    InventoryList
  }
}
</script>

<style scoped>
.scrollable-table-container {
  max-height: 500px; /* You can adjust this value */
  overflow-y: auto;  /* Allow vertical scrolling */
}
</style>
