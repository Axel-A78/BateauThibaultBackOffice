<template>
  <HeaderComponent />
  <ProductList />
</template>

<script lang="ts">
import { defineComponent } from "vue";
import HeaderComponent from "@/components/HeaderComponent.vue";
import ProductList from "@/components/ProductList.vue";

export default defineComponent({
  name: "HomeView",
  components: {
    ProductList,
    HeaderComponent,
  },
});
</script>
