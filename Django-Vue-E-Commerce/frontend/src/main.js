import { createApp } from "vue";
import router from "./router";
import App from "./App.vue";
import store from "./store";
import axios from "axios";

axios.defaults.baseURL = "https://django-vuejs-e-com.onrender.com";

createApp(App).use(store).use(router, axios).mount("#app");
