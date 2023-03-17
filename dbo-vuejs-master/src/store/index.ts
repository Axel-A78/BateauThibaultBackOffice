import { createStore } from "vuex";

export default createStore({
  state: {
    products: [],
  },
  mutations: {
    setProducts(state, products) {
      state.products = products;
    },
  },
  actions: {
    async fetchProducts({ commit }) {
      const response = await fetch("http://localhost:8000/products");
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
