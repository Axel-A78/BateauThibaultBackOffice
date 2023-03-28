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
  },
  actions: {
    async updateQuantityInStock(
      context: ActionContext<RootState, RootState>,
      payload: StockUpdatePayload
    ) {
      const { commit, state, rootGetters } = context;
      const { productId, stockChange } = payload;
      if (!rootGetters.isAuthenticated) {
        console.error("Accès refusé. Veuillez vous connecter.");
        return;
      }

      const product = state.products.find((p: Product) => p.id === productId);

      if (product) {
        const newQuantityInStock = product.quantityInStock + stockChange;

        // Envoyer une requête PATCH au backend
        const response = await fetch(
          `http://127.0.0.1:8000/update_product_stock/${productId}/`,
          {
            method: "PATCH",
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${rootGetters.getToken}`,
            },
            body: JSON.stringify({ quantityInStock: stockChange }),
          }
        );

        if (response.ok) {
          const updatedProduct = await response.json();
          commit("updateQuantityStock", {
            productId,
            newQuantityInStock: updatedProduct.quantityInStock,
          });
        } else {
          const error = await response.json();
          console.error("Error updating product stock:", error);
        }
      }
    },
    async fetchProducts({ commit, rootGetters }) {
      const response = await fetch("http://localhost:8000/infoproducts", {
        headers: {
          Authorization: `Bearer ${rootGetters.getToken}`,
        },
      });
      const products = await response.json();
      commit("setProducts", products);
    },
  },
  getters: {
    getProducts(state) {
      return state.products;
    },
  },
});
