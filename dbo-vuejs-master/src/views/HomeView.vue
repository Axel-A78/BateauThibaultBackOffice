<template>
  <HeaderComponent @navigate="navigateTo" />

  <div class="home">
    <div class="home-card">
      <h2>Bienvenue sur l'interface d'administration du marchand de poisson</h2>
      <p>
        Cette interface vous permet de gérer les stocks de produits de notre
        magasin. Vous pouvez ajouter ou retirer des produits en stock, modifier
        les prix et les promotions, voir le chiffre d'affaires, et d'autres
        fonctionnalités importantes. Utilisez les onglets de navigation en haut
        de la page pour accéder aux différentes fonctionnalités.
      </p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import ProductList from "@/components/ProductList.vue";

export default defineComponent({
  name: "HomeView",
  components: {},
  methods: {
    navigateTo(routeName: any) {
      this.$router.push({ name: routeName });
    },
  },
});
</script>

<style scoped>
.home {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  background-color: #f2f2f2;
}

.home-card {
  width: 50%;
  background-color: #0c2340;
  color: #fff;
  text-align: center;
  border-radius: 8px;
  padding: 2rem;
  margin-bottom: 20rem;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}

.home-card h2 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.home-card p {
  font-size: 1rem;
  line-height: 1.5;
  margin-bottom: 0;
}
</style>
