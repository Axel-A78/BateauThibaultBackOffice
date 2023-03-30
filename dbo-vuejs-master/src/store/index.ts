import { ActionContext, createStore } from "vuex";
import auth from "./auth";

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

interface RootState {
  products: Product[];
}

interface StockUpdatePayload {
  productId: number;
  stockChange: number;
}

interface SaleUpdatePayload {
  productId: number;
  salePercentage: number;
}

export default createStore<RootState>({
  modules: {
    auth,
  },
  state: {
    products: [] as Product[],
  },

  mutations: {
    setProducts(state, products) {
      state.products = products;
    },
    updateQuantityStock(state, { productId, newQuantityInStock }) {
      const product = state.products.find((p) => p.id === productId);
      if (product) {
        product.quantityInStock = newQuantityInStock;
      }
    },
    updateSalePercentage(
      state,
      payload: { productId: number; newSalePercentage: number }
    ) {
      const productIndex = state.products.findIndex(
        (p) => p.id === payload.productId
      );
      if (productIndex !== -1) {
        state.products[productIndex].promotion_percentage =
          payload.newSalePercentage;
        state.products[productIndex].price_on_sale =
          state.products[productIndex].price *
          (1 - payload.newSalePercentage / 100);
      }
    },
  },
  actions: {
    async updateQuantityInStock(
      context: ActionContext<RootState, RootState>,
      payload: StockUpdatePayload
    ) {
      const { commit, state, rootGetters } = context;
      const { productId, stockChange } = payload;
      const token = rootGetters["auth/getToken"];

      if (!token) {
        console.error("Accès refusé. Veuillez vous connecter.");
        return;
      }

      const product = state.products.find((p: Product) => p.id === productId);

      if (product) {
        const newQuantityInStock = product.quantityInStock + stockChange;
        console.log(
          "New quantity :",
          newQuantityInStock,
          "Produit de quantité dans la table : ",
          product.quantityInStock,
          "Stockchange:",
          stockChange
        );
        // Envoyer une requête PATCH au backend
        const response = await fetch(
          `http://127.0.0.1:8000/update_product_stock/${productId}/`,
          {
            method: "PATCH",
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${token}`,
            },

            body: JSON.stringify({ quantityInStock: newQuantityInStock }),
          }
        );

        if (response.ok) {
          const updatedProduct = await response.json();
          console.log("Produit msie à jour après requete : " + updatedProduct);
          commit("updateQuantityStock", {
            productId,
            newQuantityInStock: updatedProduct.quantityInStock,
          });
          product.quantityInStock = updatedProduct.quantityInStock;
        } else {
          const error = await response.json();
          console.error("Error updating product stock:", error);
        }
      }
    },

    async updateSalePercentage(
      context: ActionContext<RootState, RootState>,
      payload: SaleUpdatePayload
    ) {
      const { commit, state, rootGetters } = context;
      const { productId, salePercentage } = payload;
      const token = rootGetters["auth/getToken"];

      if (!token) {
        console.error("Accès refusé. Veuillez vous connecter.");
        return;
      }

      const product = state.products.find((p: Product) => p.id === productId);

      if (product) {
        const newSalePercentage = parseInt(salePercentage.toString());
        console.log(newSalePercentage);
        // Envoyer une requête PUT au backend
        const response = await fetch(
          `http://localhost:8000/update_sale_percentage/${productId}/`,
          {
            method: "PUT",
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${token}`,
            },
            body: JSON.stringify({
              sale: true,
              discount: newSalePercentage,
            }),
          }
        );

        if (response.ok) {
          const updatedProduct = await response.json();
          commit("updateSalePercentage", {
            productId,
            newSalePercentage: updatedProduct.sale_percentage,
          });
        } else {
          const error = await response.json();
          console.error("Error updating product sale percentage:", error);
        }
      }
    },

    async fetchProducts({ commit, rootGetters }) {
      console.log("token recup : ", rootGetters["auth/getToken"]);
      const response = await fetch("http://localhost:8000/infoproducts", {
        headers: {
          Authorization: `Bearer ${rootGetters["auth/getToken"]}`,
        },
      });

      if (response.ok) {
        const products = await response.json();
        commit("setProducts", products);
      } else {
        console.error("Erreur lors de la récupération des produits.");
      }
    },
  },
  getters: {
    getProducts(state) {
      return state.products;
    },
  },
});
