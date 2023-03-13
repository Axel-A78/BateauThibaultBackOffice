<template>
  <ProductList />
</template>

<script lang="ts">
import { defineComponent } from "vue";
import ProductList from "@/components/ProductList.vue";

export default defineComponent({
  name: "HomeView",
  components: {
    ProductList,
  },
});
</script>

<style>
.home {
  background: #fafafa;
}
header {
  top: 0;
  position: sticky;
  min-height: 120px;
  background: #150f26;
}
h1 {
  margin: 0;
  font-size: 36px;
  color: white;
  padding: 24px;
}
main {
  overflow-y: hidden;
  font-size: 36px;
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  grid-gap: 20px;
  justify-items: center;
  align-items: center;
}

.product-card {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 300px;
  height: 150px;
  background: #5b686a;
  border: 2px solid navy;
  border-radius: 8px;
  box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
}

.product-name {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 8px;
}

.product-price {
  font-size: 18px;
}
</style>
