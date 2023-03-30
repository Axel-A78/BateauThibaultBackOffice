<template>
  <div>
    <h1>Liste des produits</h1>
    <ul class="productGrid">
      <li v-for="product in products" :key="product.id">
        <Card class="cardProduct" style="width: 25em">
          <template #header>
            <img alt="user header" src="/images/usercard.png" />
          </template>
          <template #title> {{ product.name }} </template>
          <template #subtitle> {{ product.price }} € </template>
          <template #content>
            <p>
              {{ product.description }}
            </p>
          </template>
          <template #footer>
            <Button icon="pi pi-shopping-cart" rounded />
          </template>
        </Card>
      </li>
    </ul>
  </div>
</template>

<script>
import store from "../store";
import Card from "primevue/card";

export default {
  name: "ProductList",
  components: {
    Card,
  },
  computed: {
    products() {
      return store.getters.getProducts;
    },
  },
  mounted() {
    store.dispatch("fetchProducts");
  },
};
</script>

<style>
html {
  font-size: 14px;
}

body {
  font-family: var(--font-family);
  font-weight: normal;
  background: var(--surface-ground);
  color: var(--text-color);
  padding: 1rem;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.cardProduct {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 1rem;
  background: var(--surface-card);
  padding: 2rem;
  border-radius: 10px;
  margin-bottom: 1rem;
}

.productGrid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 1rem;
  list-style-type: none;
  padding: 0;
  margin: 0;
}
</style>
