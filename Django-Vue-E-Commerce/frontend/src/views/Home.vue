<template>
  <div class="home">
    <div class="columns is-multiline">
      <ProductBox
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ProductBox from "@/components/ProductBox.vue";

export default {
  name: "Home",
  components: {
    ProductBox,
  },
  data() {
    return { latestProducts: [] };
  },
  mounted() {
    this.getLatestProducts();
    document.title = "Homepage";
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit("setIsLoading", true);

      await axios
        .get("/api/v1/latest-products/")
        .then((resp) => (this.latestProducts = resp.data))
        .catch((err) => console.log(err));

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
