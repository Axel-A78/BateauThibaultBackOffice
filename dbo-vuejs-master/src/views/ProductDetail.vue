<template>
  <div v-if="product">
    <h1>{{ product.name }}</h1>
    <p>{{ product.description }}</p>
    <p>Prix: {{ product.prix }} €</p>
    <!-- autres informations sur le produit... -->
  </div>
</template>

<script>
export default {
  props: ["id"],
  data() {
    return {
      product: null,
    };
  },
  async created() {
    // Récupération du produit avec l'API REST
    const response = await fetch(`http://localhost:8000/product/${this.id}`);
    this.product = await response.json();
    console.log(this.product);
    console.log(this.product.name);
  },
};
</script>
