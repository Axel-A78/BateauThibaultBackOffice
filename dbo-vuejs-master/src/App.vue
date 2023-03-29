<template>
  <link rel="stylesheet" href="https://unpkg.com/primeflex@^3/primeflex.css" />
  <HeaderComponent @navigate="navigateTo" />
  <router-view />
</template>

<style>
body {
  height: 100vh;
  margin: 0;
  padding: 0;
  font-family: helvetica;
}
#app {
  height: 100%;
}
</style>

<script lang="ts">
import { defineComponent } from "vue";
import HeaderComponent from "@/components/HeaderComponent.vue"; // Importez HeaderComponent

export default defineComponent({
  name: "App",
  components: {
    HeaderComponent, // Ajoutez HeaderComponent à la liste des composants
  },
  methods: {
    navigateTo(routeName: any) {
      this.$router.push({ name: routeName });
    },
  },
});
</script>
