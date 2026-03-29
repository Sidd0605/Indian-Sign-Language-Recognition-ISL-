<template>
  <div class="app-shell">
    <Navbar />
    <router-view />
  </div>
</template>

<script>
import Navbar from "../src/components/Navbar.vue";

export default {
  name: "App",
  components: {
    Navbar,
  },
};
</script>

<style>
html, body, #app {
  min-height: 100%;
}

body {
  margin: 0;
  font-family: "Avenir Next", "Trebuchet MS", sans-serif;
  background:
    radial-gradient(circle at top left, rgba(255, 214, 102, 0.35), transparent 28%),
    radial-gradient(circle at top right, rgba(42, 157, 143, 0.28), transparent 26%),
    linear-gradient(180deg, #f7f4ea 0%, #eef7f2 44%, #f7fbff 100%);
  color: #143642;
}

* {
  box-sizing: border-box;
}

a {
  text-decoration: none;
}

.app-shell {
  min-height: 100vh;
}
</style>
