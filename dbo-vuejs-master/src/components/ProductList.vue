<template>
  <div class="home">
    <header>
      <h1>Le poisson de Thibault</h1>
    </header>
    <main>
      Le projet fonctionne
      <div>{{ products.length }} products</div>
      <div class="product-grid">
        <div class="product-card" v-for="product in products" :key="product.id">
          <div class="product-name">{{ product.name }}</div>
          <div class="product-price">{{ product.price }}€</div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "ProductList",
  setup() {
    const products = ref([]);

    const getproducts = () => {
      return new Promise((resolve, reject) => {
        fetch("http://127.0.0.1:8000/products/")
          .then((response) => {
            if (response.ok) {
              resolve(response.json());
            } else {
              reject(new Error("Failed to fetch products"));
            }
          })
          .catch((error) => {
            reject(error);
          });
      });
    };

    getproducts().then((data) => {
      products.value = data;
    });

    return {
      products,
    };
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
