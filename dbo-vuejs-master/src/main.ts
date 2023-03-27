import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import PrimeVue from "primevue/config";
import InputText from "primevue/inputtext";
import Card from "primevue/card";
import Button from "primevue/button";
import AutoComplete from "primevue/autocomplete";
import InputNumber from "primevue/inputnumber";
import Image from "primevue/image";

//theme
import "primevue/resources/themes/md-light-indigo/theme.css";

//core
import "primevue/resources/primevue.min.css";

//icons
import "primeicons/primeicons.css";

createApp(App)
  .use(store)
  .use(router)
  .use(PrimeVue)
  .component("InputText", InputText)
  .component("Button", Button)
  .component("Card", Card)
  .component("AutoComplete", AutoComplete)
  .component("InputNumber", InputNumber)
  .component("Image", Image)
  .mount("#app");
