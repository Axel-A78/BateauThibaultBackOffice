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
        <button @click="addStock" style="margin-right: 10px; margin-top: 10px">
          Ajouter article(s)
        </button>
        <button @click="removeStock" style="margin-top: 10px">
          Supprimer article(s)
        </button>
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
      <p>Quantité en stock: {{ selectedProduct.quantityInStock }}</p>
      <p>Nombre d'articles vendus: {{ selectedProduct.sold_count }}</p>
      <p>Commentaires: {{ selectedProduct.comments }}</p>
      <div>
        <label for="sale-percentage"
          >Modifier le pourcentage de promotion :</label
        >
        <input
          type="number"
          id="sale-percentage"
          v-model.number="salePercentage"
        />
        %
        <button
          @click="updateSalePercentage"
          style="margin-right: 10px; margin-top: 10px"
        >
          Mettre à jour promotion
        </button>
        <div v-if="errorMessage">{{ errorMessage }}</div>
      </div>
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
import { defineComponent, ref, watch } from "vue";
import { useStore } from "vuex";

interface Product {
  id: number;
  name: string;
  price: number;
  price_on_sale?: number;
  promotion_percentage?: number;
  quantityInStock: number;
  sold_count: number;
  comments: string;
}

export default defineComponent({
  name: "ProductDetails",
  setup() {
    const store = useStore();
    const selectedProduct = ref<Product | null>(null);
    const products = ref<Product[]>([]);
    const salePercentage = ref<number>(0);
    const stockChange = ref<number>(0);
    const errorMessage = ref<string>("");

    store.dispatch("fetchProducts");

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
      const parsedStockChange = parseInt(stockChange.value.toString());
      const product = selectedProduct.value;
      if (isNaN(parsedStockChange) || parsedStockChange < 1) {
        errorMessage.value = "Veuillez entrer un nombre positif.";
      } else if (product.quantityInStock + parsedStockChange > 1000) {
        errorMessage.value = "Le stock maximal est atteint.";
      } else {
        // Appelez l'action Vuex pour ajouter des articles au stock
        store.dispatch("updateQuantityInStock", {
          productId: product.id,
          stockChange: parsedStockChange,
        });
        product.quantityInStock = Math.min(
          product.quantityInStock + parsedStockChange,
          1000
        );
        selectedProduct.value = { ...product }; // mise à jour de l'objet réactif
        errorMessage.value = "";
      }
    }

    function removeStock() {
      if (!selectedProduct.value) return;
      const parsedStockChange = -parseInt(stockChange.value.toString());
      const product = selectedProduct.value;
      if (isNaN(parsedStockChange) || parsedStockChange > 1) {
        errorMessage.value = "Veuillez entrer un nombre negatif.";
      } else if (product.quantityInStock + parsedStockChange < 0) {
        errorMessage.value = "Le stock minimal est 0.";
      } else {
        // Appelez l'action Vuex pour ajouter des articles au stock
        store.dispatch("updateQuantityInStock", {
          productId: product.id,
          stockChange: parsedStockChange,
        });
        product.quantityInStock = Math.min(
          product.quantityInStock + parsedStockChange
        );
        selectedProduct.value = { ...product }; // mise à jour de l'objet réactif
        errorMessage.value = "";
      }
    }
    function updateSalePercentage() {
      if (!selectedProduct.value) return;
      const parsedSalePercentage = parseInt(salePercentage.value.toString());
      if (
        isNaN(parsedSalePercentage) ||
        parsedSalePercentage < 0 ||
        parsedSalePercentage > 100
      ) {
        errorMessage.value = "Veuillez entrer un pourcentage entre 0 et 100.";
      } else {
        // Appelez l'action Vuex pour mettre à jour le pourcentage de promotion
        store.dispatch("updateSalePercentage", {
          productId: selectedProduct.value.id,
          salePercentage: parsedSalePercentage,
        });
        errorMessage.value = "";
      }
    }

    return {
      products,
      selectedProduct,
      displaySelectedProduct,
      stockChange,
      salePercentage,
      updateSalePercentage,
      errorMessage,
      addStock,
      removeStock,
    };
  },
});
</script>
