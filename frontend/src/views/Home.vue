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
