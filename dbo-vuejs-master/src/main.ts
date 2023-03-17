import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import PrimeVue from "primevue/config";

//theme
import "primevue/resources/themes/md-light-indigo/theme.css";

//core
import "primevue/resources/primevue.min.css";

//icons
import "primeicons/primeicons.css";

createApp(App).use(store).use(router).use(PrimeVue).mount("#app");
