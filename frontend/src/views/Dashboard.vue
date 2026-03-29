<template>
  <main class="dashboard-page">
    <section class="dashboard-hero">
      <div>
        <p class="eyebrow">Explore the platform</p>
        <h1>Choose how you want to interact with the ISL project.</h1>
      </div>
      <p class="hero-copy">
        Start recognition, continue learning through external ISL resources, or register your interest for future improvements and updates.
      </p>
    </section>

    <section class="card-grid">
      <article v-for="(item, index) in actions" :key="index" class="feature-card">
        <img :src="item.image" :alt="item.name" class="card-image" />
        <div class="card-copy">
          <p class="card-tag">{{ item.tag }}</p>
          <h2>{{ item.name }}</h2>
          <p>{{ item.description }}</p>
        </div>

        <div class="card-action">
          <router-link v-if="index === 0" :to="{ name: 'Crop', params: { crop_name: 'ISL' } }" class="action-btn primary-action">
            Detect Gesture
          </router-link>

          <a
            v-else-if="index === 1"
            href="https://indiansignlanguage.org/learn-with-signs/"
            target="_blank"
            rel="noreferrer"
            class="action-btn info-action"
          >
            Learn ISL
          </a>

          <router-link v-else :to="{ name: 'Register' }" class="action-btn success-action">
            Register Interest
          </router-link>
        </div>
      </article>
    </section>
  </main>
</template>

<script>
export default {
  name: "Dashboard",
  data() {
    return {
      actions: [
        {
          name: "Run Recognition",
          tag: "Recognition",
          image: require("@/assets/handimg.jpg"),
          description: "Upload an image of a hand sign and let the model analyze the gesture.",
        },
        {
          name: "Learn About ISL",
          tag: "Learning",
          image: require("@/assets/isl.jpg"),
          description: "Open an external resource to continue learning Indian Sign Language and related communication basics.",
        },
        {
          name: "Join Future Updates",
          tag: "Community",
          image: require("@/assets/signlate.jpg"),
          description: "Share your details if you want to follow future features, improvements, and project progress.",
        },
      ],
    };
  },
};
</script>

<style scoped>
.dashboard-page {
  max-width: 1180px;
  margin: 0 auto;
  padding: 28px 24px 56px;
}

.dashboard-hero {
  display: flex;
  justify-content: space-between;
  gap: 20px;
  align-items: flex-end;
  margin-bottom: 24px;
}

.eyebrow {
  margin: 0 0 8px;
  color: #2a9d8f;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  font-size: 0.76rem;
  font-weight: 700;
}

.dashboard-hero h1 {
  margin: 0;
  max-width: 12ch;
  font-size: clamp(2.1rem, 3.2vw, 3.4rem);
  line-height: 1;
}

.hero-copy {
  margin: 0;
  max-width: 40ch;
  color: #355070;
  line-height: 1.8;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}

.feature-card {
  display: flex;
  flex-direction: column;
  min-height: 470px;
  border-radius: 24px;
  overflow: hidden;
  background: rgba(255, 255, 255, 0.86);
  border: 1px solid rgba(20, 54, 66, 0.08);
  box-shadow: 0 18px 40px rgba(20, 54, 66, 0.08);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.feature-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 24px 46px rgba(20, 54, 66, 0.12);
}

.card-image {
  width: 100%;
  height: 230px;
  object-fit: cover;
}

.card-copy {
  flex: 1;
  padding: 24px 24px 16px;
}

.card-tag {
  margin: 0 0 8px;
  color: #2a9d8f;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  font-size: 0.74rem;
  font-weight: 700;
}

.card-copy h2 {
  margin: 0 0 12px;
}

.card-copy p:last-child {
  margin: 0;
  color: #355070;
  line-height: 1.75;
}

.card-action {
  padding: 0 24px 24px;
}

.action-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  min-height: 48px;
  border-radius: 999px;
  font-weight: 700;
  color: #fff;
}

.primary-action {
  background: #143642;
}

.info-action {
  background: #457b9d;
}

.success-action {
  background: #2a9d8f;
}

@media (max-width: 920px) {
  .dashboard-page {
    padding: 24px 14px 40px;
  }

  .dashboard-hero {
    display: grid;
    grid-template-columns: 1fr;
  }

  .dashboard-hero h1,
  .hero-copy {
    max-width: none;
  }

  .card-grid {
    grid-template-columns: 1fr;
  }
}
</style>
