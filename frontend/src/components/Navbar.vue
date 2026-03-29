<template>
  <header class="nav-shell">
    <nav class="nav-bar">
      <router-link class="brand" :to="{ name: 'Home' }">
        <span class="brand-mark">ISL</span>
        <span class="brand-copy">
          <strong>Indian Sign Language Recognition</strong>
          <small>Accessible gesture recognition prototype</small>
        </span>
      </router-link>

      <div class="nav-links">
        <router-link class="nav-link" :to="{ name: 'Home' }">Home</router-link>
        <router-link class="nav-link" :to="{ name: 'Dashboard' }">Explore</router-link>
        <router-link class="nav-link" :to="{ name: 'ProjectDetails' }">Project</router-link>
        <router-link class="nav-link" :to="{ name: 'AboutUs' }">Team</router-link>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: "Navbar",
};
</script>

<style scoped>
.nav-shell {
  position: sticky;
  top: 0;
  z-index: 20;
  padding: 18px 24px 0;
}

.nav-bar {
  max-width: 1180px;
  margin: 0 auto;
  padding: 14px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
  border-radius: 22px;
  background: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(20, 54, 66, 0.08);
  box-shadow: 0 18px 40px rgba(20, 54, 66, 0.08);
  backdrop-filter: blur(12px);
}

.brand {
  display: flex;
  align-items: center;
  gap: 12px;
  color: #143642;
}

.brand-mark {
  width: 48px;
  height: 48px;
  border-radius: 14px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #143642, #2a9d8f);
  color: #fff;
  font-weight: 800;
  letter-spacing: 0.08em;
}

.brand-copy {
  display: flex;
  flex-direction: column;
}

.brand-copy strong {
  font-size: 1rem;
}

.brand-copy small {
  color: #52796f;
}

.nav-links {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.nav-link {
  padding: 10px 14px;
  border-radius: 999px;
  color: #143642;
  font-weight: 700;
  transition: background 0.2s ease, color 0.2s ease;
}

.nav-link:hover,
.router-link-active.nav-link {
  background: #143642;
  color: #fff;
}

@media (max-width: 820px) {
  .nav-shell {
    padding: 14px 14px 0;
  }

  .nav-bar {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>
