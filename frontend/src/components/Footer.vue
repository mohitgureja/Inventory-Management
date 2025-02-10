<template>
  <v-footer app d-flex flex-column>
    <div class="px-4 py-2 bg-black w-100 mx-0">
      <strong>Copyright (c) {{ new Date().getFullYear() }}, statworx GmbH </strong>
    </div>
  </v-footer>
</template>


<script>
export default {
  name: "Footer-Page",
}
</script>

<style>
.v-footer {
  padding: 0% !important;
}
</style>
