<template>
  <main class="result-page">
    <section class="result-grid">
      <div class="summary-card">
        <p class="eyebrow">Prediction Output</p>
        <h1>Recognition Result</h1>

        <div class="metric-list">
          <div class="metric">
            <span>Predicted Label</span>
            <strong>{{ class_label || "No sign detected" }}</strong>
          </div>
          <div class="metric">
            <span>Detected Regions</span>
            <strong>{{ total_spots }}</strong>
          </div>
          <div class="metric">
            <span>Confidence</span>
            <strong>{{ formattedConfidence }}</strong>
          </div>
        </div>

        <router-link class="back-btn" :to="{ name: 'Crop', params: { crop_name: 'ISL' } }">
          Try Another Image
        </router-link>
      </div>

      <div class="preview-card">
        <img v-if="imgSrc" :src="imgSrc" alt="Annotated recognition output" class="centered-image" />
        <div v-else class="empty-state">Annotated result will appear here after inference.</div>
      </div>
    </section>
  </main>
</template>

<script>
const API_BASE_URL = process.env.VUE_APP_API_BASE_URL || "http://127.0.0.1:5001";

export default {
  name: "Result",
  data() {
    return {
      imgSrc: "",
      class_label: "",
      confidence: 0,
      total_spots: 0,
    };
  },
  computed: {
    formattedConfidence() {
      return `${(Number(this.confidence || 0) * 100).toFixed(2)}%`;
    },
  },
  mounted() {
    this.class_label = this.$route.query.class_label || "";
    this.confidence = Number(this.$route.query.confidence || 0);
    this.total_spots = Number(this.$route.query.total_spots || 0);

    const annotatedImage = this.$route.query.annotated_image || "/result";
    this.imgSrc = annotatedImage.startsWith("http")
      ? annotatedImage
      : `${API_BASE_URL}${annotatedImage}`;
  },
};
</script>

<style scoped>
.result-page {
  max-width: 1180px;
  margin: 0 auto;
  padding: 28px 24px 56px;
}

.result-grid {
  display: grid;
  grid-template-columns: 0.9fr 1.1fr;
  gap: 22px;
}

.summary-card,
.preview-card {
  background: rgba(255, 255, 255, 0.84);
  border: 1px solid rgba(20, 54, 66, 0.08);
  box-shadow: 0 18px 40px rgba(20, 54, 66, 0.08);
  border-radius: 28px;
}

.summary-card {
  padding: 32px;
}

.eyebrow {
  margin: 0 0 10px;
  color: #2a9d8f;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  font-size: 0.76rem;
  font-weight: 700;
}

.summary-card h1 {
  margin-top: 0;
  margin-bottom: 22px;
}

.metric-list {
  display: grid;
  gap: 12px;
}

.metric {
  padding: 16px;
  border-radius: 18px;
  background: #f4f7fb;
}

.metric span {
  display: block;
  color: #52796f;
  font-size: 0.86rem;
  margin-bottom: 6px;
}

.metric strong {
  font-size: 1.1rem;
}

.back-btn {
  display: inline-flex;
  margin-top: 22px;
  padding: 12px 18px;
  border-radius: 999px;
  background: #143642;
  color: #fff;
  font-weight: 700;
}

.preview-card {
  min-height: 460px;
  padding: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.centered-image {
  width: 100%;
  max-height: 640px;
  object-fit: contain;
  border-radius: 18px;
}

.empty-state {
  color: #52796f;
  text-align: center;
  max-width: 24ch;
}

@media (max-width: 900px) {
  .result-page {
    padding: 24px 14px 40px;
  }

  .result-grid {
    grid-template-columns: 1fr;
  }
}
</style>
