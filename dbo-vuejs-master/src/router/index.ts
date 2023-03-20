import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ProductDetail from "../views/ProductDetail.vue";
import LoginView from "../views/LoginView.vue";
import TestView from "../views/TestView.vue";

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
    // Vérifiez si l'utilisateur a un jeton d'accès valide
    const token = localStorage.getItem("token");
    if (!token) {
      // Si l'utilisateur n'a pas de jeton, redirigez-le vers la page de connexion
      next({
        path: "/login",
        query: { redirect: to.fullPath },
      });
    } else {
      // Si l'utilisateur a un jeton, laissez-le accéder à la route
      next();
    }
  } else {
    // Si la route n'a pas besoin d'authentification, laissez l'utilisateur y accéder
    next();
  }
});

export default router;
