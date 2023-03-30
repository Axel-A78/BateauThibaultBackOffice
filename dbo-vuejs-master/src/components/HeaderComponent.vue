<template>
  <div class="card relative z-2">
    <Menubar :model="items">
      <template #start>
        <a href="http://localhost:8080/">
          <img
            alt="logo"
            src="https://i.postimg.cc/jqP7JhJf/image.png"
            height="40"
            class="mr-2"
        /></a>
      </template>
      <template #end>
        <InputText placeholder="Search" type="text" />
      </template>
    </Menubar>
  </div>
</template>

<script>
import Menubar from "primevue/menubar";
export default {
  name: "HeaderComponent",
  components: {
    Menubar,
  },
  data() {
    return {
      items: [
        {
          label: "Liste des produits",
          icon: "pi pi-fw pi-file",
          command: () => {
            this.$emit("navigate", "ProductList");
          },
        },
        {
          label: "Modification de produit",
          icon: "pi pi-fw pi-info-circle",
          command: () => {
            this.$emit("navigate", "ProductDetails");
          },
        },
        {
          label: "Rapport financier",
          icon: "pi pi-fw pi-pencil",
        },
        {
          label: "Users",
          icon: "pi pi-fw pi-user",
          items: [
            {
              label: "New",
              icon: "pi pi-fw pi-user-plus",
            },
            {
              label: "Delete",
              icon: "pi pi-fw pi-user-minus",
            },
            {
              label: "Search",
              icon: "pi pi-fw pi-users",
              items: [
                {
                  label: "Filter",
                  icon: "pi pi-fw pi-filter",
                  items: [
                    {
                      label: "Print",
                      icon: "pi pi-fw pi-print",
                    },
                  ],
                },
                {
                  icon: "pi pi-fw pi-bars",
                  label: "List",
                },
              ],
            },
          ],
        },
        {
          label: "Categorie",
          icon: "pi pi-fw pi-calendar",
          items: [
            {
              label: "Crustace",
              icon: "pi pi-fw pi-pencil",
            },
            {
              label: "Poissons",
              icon: "pi pi-fw pi-calendar-times",
            },
            {
              label: "Fruits de mer",
              icon: "pi pi-fw pi-pencil",
            },
          ],
        },
        {
          label: "Quit",
          icon: "pi pi-fw pi-power-off",
        },
      ],
    };
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
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.card {
  background: var(--surface-card);
  border-radius: 10px;
  margin-bottom: 1rem;
}
</style>
