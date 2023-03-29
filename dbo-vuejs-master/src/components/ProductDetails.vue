<template>
  <div class="product-details">
    <div class="dropdown-wrapper">
      <Dropdown
        v-model="selectedProduct"
        :options="products"
        optionLabel="name"
        placeholder="Veuillez choisir un produit"
        @update:modelValue="displaySelectedProduct($event)"
      />
    </div>
    <div v-if="selectedProduct" class="product-info">
      <div>
        <label for="stock-change">Changer le stock :</label>
        <input type="number" id="stock-change" v-model.number="stockChange" />
        <button @click="addStock">Ajouter</button>
        <button @click="removeStock">Enlever</button>
        <p v-if="errorMessage">{{ errorMessage }}</p>
      </div>
      <h2>{{ selectedProduct.name }}</h2>
      <p>Prix: {{ selectedProduct.price }} €</p>
      <p v-if="selectedProduct.price_on_sale">
        Prix en promotion: {{ selectedProduct.price_on_sale }} €
      </p>
      <p v-if="selectedProduct.promotion_percentage">
        Pourcentage de promotion: {{ selectedProduct.promotion_percentage }}%
      </p>
      <p>Quantité en stock: {{ selectedProduct.stock }}</p>
      <p>Nombre d'articles vendus: {{ selectedProduct.sold_count }}</p>
      <p>Commentaires: {{ selectedProduct.comments }}</p>
    </div>
  </div>
</template>

<style scoped>
.product-details {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.dropdown-wrapper {
  margin-bottom: 2rem;
  width: 100%;
  max-width: 400px;
}

.product-info {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  background-color: #f5f5f5;
  padding: 1.5rem;
  border-radius: 0.5rem;
  box-shadow: 0 0.25rem 0.5rem rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
}

.product-info h2 {
  margin-bottom: 1rem;
  font-size: 1.5rem;
}

.product-info p {
  margin-bottom: 0.5rem;
}
</style>
<script lang="ts">
import { computed, defineComponent, ref, watch } from "vue";
import { useStore } from "vuex";
import { Product } from "@/types";

// interface Product {
//   id: number;
//   name: string;
//   price: number;
//   price_on_sale?: number;
//   promotion_percentage?: number;
//   stock: number;
//   sold_count: number;
//   comments: string;
// }

export default defineComponent({
  name: "ProductDetails",
  setup() {
    const store = useStore();
    const selectedProduct = ref<Product | null>(null);
    const products = ref<Product[]>([]);
    const stockChange = ref(0);
    const errorMessage = ref("");

    watch(
      () => store.getters["auth/isAuthenticated"],
      (isAuthenticated: boolean) => {
        if (isAuthenticated) {
          store.dispatch("fetchProducts");
        }
      }
    );

    watch(
      () => store.getters.getProducts,
      (newProducts: Product[]) => {
        products.value = newProducts;
      }
    );

    function displaySelectedProduct(product: Product) {
      selectedProduct.value = product;
    }

    function addStock() {
      if (!selectedProduct.value) return;
      if (stockChange.value < 1) {
        errorMessage.value = "Veuillez entrer un nombre positif.";
      } else {
        store.dispatch("updateQuantityInStock", {
          productId: selectedProduct.value.id,
          stockChange: stockChange.value,
        });
        errorMessage.value = "";
      }
    }

    function removeStock() {
      if (!selectedProduct.value) return;
      if (
        stockChange.value < 1 ||
        stockChange.value > selectedProduct.value.quantityInStock
      ) {
        errorMessage.value = "Veuillez entrer un nombre valide.";
      } else {
        store.dispatch("updateQuantityInStock", {
          productId: selectedProduct.value.id,
          stockChange: -stockChange.value,
        });
        errorMessage.value = "";
      }
    }

    return {
      products,
      selectedProduct,
      displaySelectedProduct,
      stockChange,
      errorMessage,
      addStock,
      removeStock,
    };
  },
});
</script>
