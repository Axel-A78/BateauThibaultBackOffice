import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ProductDetail from "../views/ProductDetail.vue";
import LoginView from "../views/LoginView.vue";
import TestView from "../views/TestView.vue";
import { loggedIn } from "@/utils/auth";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },

  {
    path: "/product/:id",
    name: "ProductDetail",
    component: ProductDetail,
    props: true,
  },

  {
    path: "/login",
    name: "login",
    component: LoginView,
  },

  {
    path: "/test",
    name: "test",
    component: TestView,
    meta: {
      requiresAuth: true,
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// Ajoutez un guard de route pour la vérification de l'authentification
router.beforeEach((to, from, next) => {
  // Vérifiez si la route nécessite une authentification
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    // Vérifiez si l'utilisateur est connecté
    if (!loggedIn()) {
      // Si l'utilisateur n'est pas connecté, redirigez-le vers la page de connexion
      console.log("User n'est pas connecté. Redirection à la page login.");
      next({
        path: "/login",
        query: { redirect: to.fullPath },
      });
    } else {
      // Si l'utilisateur est connecté, laissez-le accéder à la route
      console.log("User est connecté. Accès autorisé.");
      next();
    }
  } else {
    // Si la route n'a pas besoin d'authentification, laissez l'utilisateur y accéder
    console.log("Authentification non requise. Accès autorisé.");
    next();
  }
});

export default router;
