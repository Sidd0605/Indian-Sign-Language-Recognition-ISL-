<template>
  <main class="details-page">
    <section class="hero-card">
      <p class="eyebrow">Project Overview</p>
      <h1>How the ISL recognition system is structured</h1>
      <p>
        This capstone combines a web interface and an object-detection model to create a usable prototype for recognizing Indian Sign Language gestures from uploaded images.
      </p>
    </section>

    <section class="details-grid">
      <article class="detail-card">
        <h2>Problem Focus</h2>
        <p>
          The project explores how computer vision can support accessible communication by interpreting hand-sign imagery and mapping it to meaningful ISL output.
        </p>
      </article>

      <article class="detail-card">
        <h2>Technical Stack</h2>
        <p>
          The frontend is built with Vue, the backend uses Flask, and gesture recognition is handled through a YOLO-based inference pipeline with annotated result output.
        </p>
      </article>

      <article class="detail-card">
        <h2>Workflow</h2>
        <p>
          A user uploads an image, the backend processes it through the trained model, and the UI presents the recognized class label, confidence, and highlighted output image.
        </p>
      </article>

      <article class="detail-card">
        <h2>Scope</h2>
        <p>
          The current version is a working academic prototype designed for demonstration, experimentation, and future extension into broader accessibility or learning use cases.
        </p>
      </article>
    </section>
  </main>
</template>

<script>
export default {
  name: "ProjectDetails",
};
</script>

<style scoped>
.details-page {
  max-width: 1080px;
  margin: 0 auto;
  padding: 28px 24px 56px;
}

.hero-card,
.detail-card {
  background: rgba(255, 255, 255, 0.84);
  border: 1px solid rgba(20, 54, 66, 0.08);
  box-shadow: 0 18px 40px rgba(20, 54, 66, 0.08);
}

.hero-card {
  border-radius: 28px;
  padding: 32px;
  margin-bottom: 20px;
}

.eyebrow {
  margin: 0 0 10px;
  color: #2a9d8f;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  font-size: 0.76rem;
  font-weight: 700;
}

.hero-card h1 {
  margin: 0 0 10px;
}

.hero-card p:last-child {
  margin: 0;
  color: #355070;
  line-height: 1.8;
}

.details-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 18px;
}

.detail-card {
  padding: 26px;
  border-radius: 24px;
}

.detail-card h2 {
  margin-top: 0;
}

.detail-card p {
  margin-bottom: 0;
  color: #355070;
  line-height: 1.8;
}

@media (max-width: 760px) {
  .details-page {
    padding: 24px 14px 40px;
  }

  .details-grid {
    grid-template-columns: 1fr;
  }
}
</style>
