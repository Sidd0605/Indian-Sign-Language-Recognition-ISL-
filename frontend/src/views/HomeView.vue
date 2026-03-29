<template>
  <main class="home-page">
    <section class="hero-section">
      <div class="hero-copy">
        <p class="eyebrow">Final Capstone Project</p>
        <h1>Indian Sign Language Recognition (ISL)</h1>
        <p class="hero-text">
          A deep-learning web application for recognizing Indian Sign Language gestures from uploaded images and presenting the results through a polished, easy-to-use interface.
        </p>
        <div class="hero-actions">
          <router-link class="primary-btn" :to="{ name: 'Dashboard' }">Start Recognition</router-link>
          <router-link class="secondary-btn" :to="{ name: 'ProjectDetails' }">Project Overview</router-link>
        </div>
      </div>

      <div class="hero-panel">
        <div class="panel-card top-card">
          <span>Goal</span>
          <strong>Use computer vision to support more accessible communication.</strong>
        </div>
        <div class="panel-card mid-card">
          <span>Flow</span>
          <strong>Upload a gesture image, run inference, and review the confidence-driven result.</strong>
        </div>
        <div class="panel-card bottom-card">
          <span>Stack</span>
          <strong>Vue frontend, Flask backend, and YOLO-powered image recognition.</strong>
        </div>
      </div>
    </section>

    <section class="info-grid">
      <article class="info-card">
        <h2>Aim and Mission</h2>
        <p>
          This project aims to reduce communication barriers by building a practical recognition system for Indian Sign Language gestures. It also helps highlight the role of ISL as an important communication medium.
        </p>
      </article>

      <article class="info-card">
        <h2>Why It Matters</h2>
        <p>
          Recognition tools can support learning, accessibility research, and prototype communication workflows. This capstone brings machine learning and interface design together in one focused application.
        </p>
      </article>

      <article class="info-card">
        <h2>What You Can Explore</h2>
        <p>
          Use the dashboard to upload gesture images, inspect prediction results, review the project structure, and explore the team and future directions behind the prototype.
        </p>
      </article>
    </section>
  </main>
</template>

<script>
export default {
  name: "HomeView",
};
</script>

<style scoped>
.home-page {
  max-width: 1180px;
  margin: 0 auto;
  padding: 28px 24px 56px;
}

.hero-section {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 28px;
}

.hero-copy,
.hero-panel,
.info-card {
  background: rgba(255, 255, 255, 0.84);
  border: 1px solid rgba(20, 54, 66, 0.08);
  box-shadow: 0 20px 50px rgba(20, 54, 66, 0.08);
}

.hero-copy {
  padding: 44px;
  border-radius: 28px;
}

.eyebrow {
  margin: 0 0 12px;
  color: #2a9d8f;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  font-size: 0.78rem;
}

h1 {
  margin: 0;
  font-size: clamp(2.4rem, 4vw, 4.1rem);
  line-height: 0.98;
}

.hero-text {
  margin: 22px 0 0;
  color: #355070;
  line-height: 1.8;
  max-width: 56ch;
}

.hero-actions {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  margin-top: 28px;
}

.primary-btn,
.secondary-btn {
  padding: 14px 20px;
  border-radius: 999px;
  font-weight: 700;
}

.primary-btn {
  background: #143642;
  color: #fff;
}

.secondary-btn {
  background: #ffd166;
  color: #143642;
}

.hero-panel {
  border-radius: 28px;
  padding: 20px;
  display: grid;
  gap: 16px;
}

.panel-card {
  min-height: 148px;
  border-radius: 22px;
  padding: 22px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  color: #fff;
}

.panel-card span {
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-size: 0.8rem;
  opacity: 0.86;
}

.panel-card strong {
  font-size: 1.15rem;
  line-height: 1.45;
}

.top-card {
  background: linear-gradient(135deg, #1d3557, #2a9d8f);
}

.mid-card {
  background: linear-gradient(135deg, #2a9d8f, #457b9d);
}

.bottom-card {
  background: linear-gradient(135deg, #e76f51, #f4a261);
}

.info-grid {
  margin-top: 28px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}

.info-card {
  border-radius: 24px;
  padding: 28px;
}

.info-card h2 {
  margin-top: 0;
  margin-bottom: 14px;
}

.info-card p {
  margin: 0;
  color: #355070;
  line-height: 1.75;
}

@media (max-width: 920px) {
  .hero-section,
  .info-grid {
    grid-template-columns: 1fr;
  }

  .hero-copy {
    padding: 30px;
  }
}

@media (max-width: 640px) {
  .home-page {
    padding: 22px 14px 40px;
  }
}
</style>
