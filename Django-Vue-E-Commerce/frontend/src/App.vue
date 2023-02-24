<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">Home</router-link>

        <a
          class="navbar-burger"
          aria-label="menu"
          aria-expanded="false"
          data-target="navbar-menu"
          @click="showMobileMenu = !showMobileMenu"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div
        class="navbar-menu"
        id="navbar-menu"
        v-bind:class="{ 'is-active': showMobileMenu }"
      >
        <div class="navbar-start">
          <div class="navbar-item">
            <form method="get" action="/search">
              <div class="field has-addons">
                <div class="control">
                  <input
                    type="text"
                    class="input"
                    placeholder="What are you looking for?"
                    name="query"
                  />
                </div>

                <div class="control">
                  <button class="button is-success">
                    <span class="icon">
                      <i class="fas fa-search"></i>
                    </span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>

        <div class="navbar-end">
          <router-link to="/summer" class="navbar-item">Summer</router-link>
          <router-link to="/winter" class="navbar-item">Winter</router-link>

          <div class="navbar-item">
            <div class="buttons">
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/my-account" class="button is-light"
                  >My account</router-link
                >
              </template>

              <template v-else>
                <router-link to="/log-in" class="button is-light"
                  >Log in</router-link
                >
              </template>

              <router-link to="/cart" class="button is-success">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart ({{ cartTotalLength }})</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <div v-if="$store.state.isLoading" class="center">
      <div
        class="loading-box"
        v-bind:class="{ 'is-loading': $store.state.isLoading }"
      >
        <div class="loader"></div>
      </div>
    </div>

    <section class="section">
      <router-view />
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2021</p>
    </footer>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: [],
      },
      isAuthenticated: false,
    };
  },
  beforeCreate() {
    this.$store.commit("initializeStore");

    const token = this.$store.state.token;

    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
  mounted() {
    this.cart = this.$store.state.cart;
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0;

      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity;
      }

      return totalLength;
    },
  },
};
</script>

<style lang="scss">
@import "../node_modules/bulma";

.loader {
  left: -100%;
  animation: load 3s linear infinite;
}

@keyframes load {
  0% {
    left: -100%;
  }
  100% {
    left: 100%;
  }
}
.loading-box {
  width: 400px;
  height: 50px;
  border-radius: 50px;
  border: 2px solid #ededed;
  overflow: hidden;
}

.loader {
  width: 100%;
  height: 100%;
  border-radius: 50px;
  background: linear-gradient(45deg, #b6b5ff, #ff9797);
  left: 0%;
}

.center {
  display: flex;
  justify-content: center;
  margin-top: 15%;
  margin-bottom: 15%;
}

@media (max-width: 420px) {
  .center {
    display: flex;
    justify-content: center;
    margin-top: 20%;
    margin-bottom: 30%;
  }
}
</style>
