<template>
  <main class="detect-page">
    <section class="detect-panel">
      <div class="intro">
        <p class="eyebrow">Recognition Workspace</p>
        <h1>Upload an ISL gesture image</h1>
        <p>
          Choose a clear hand-sign image and send it to the recognition model. The result page will show the predicted label, confidence, and the annotated output image.
        </p>
      </div>

      <form enctype="multipart/form-data" class="upload-card">
        <label for="file" class="upload-label">Select image</label>
        <input
          id="file"
          type="file"
          class="form-control picker"
          name="file"
          ref="inputFile"
          accept=".png,.jpg,.jpeg,.gif"
        />
        <button type="submit" class="upload-btn" @click.prevent="uploadFile">Analyze Gesture</button>
      </form>
    </section>
  </main>
</template>

<script>
import router from "../router/index";

const API_BASE_URL = process.env.VUE_APP_API_BASE_URL || "http://127.0.0.1:5001";

export default {
  name: "Crop",
  methods: {
    async uploadFile(event) {
      event.preventDefault();
      const selectedFile = this.$refs.inputFile?.files?.[0];

      if (!selectedFile) {
        alert("Please choose an image first.");
        return;
      }

      const formData = new FormData();
      formData.append("file", selectedFile);

      try {
        const response = await fetch(`${API_BASE_URL}/upload`, {
          method: "POST",
          body: formData,
        });

        if (!response.ok) {
          const errorData = await response.json();
          alert(`Error: ${errorData.error_message || "Something went wrong"}`);
          return;
        }

        const data = await response.json();
        router.push({
          name: "Result",
          query: {
            class_label: data.class_label,
            confidence: data.confidence,
            total_spots: data.total_spots,
            annotated_image: data.annotated_image || "/result",
          },
        });
      } catch (error) {
        console.error("Error uploading file:", error);
        alert("Error uploading file. Please try again.");
      }
    },
  },
};
</script>

<style scoped>
.detect-page {
  max-width: 980px;
  margin: 0 auto;
  padding: 28px 24px 56px;
}

.detect-panel {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 22px;
}

.intro,
.upload-card {
  background: rgba(255, 255, 255, 0.84);
  border: 1px solid rgba(20, 54, 66, 0.08);
  box-shadow: 0 18px 40px rgba(20, 54, 66, 0.08);
  border-radius: 28px;
}

.intro {
  padding: 36px;
}

.eyebrow {
  margin: 0 0 10px;
  color: #2a9d8f;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  font-size: 0.76rem;
  font-weight: 700;
}

.intro h1 {
  margin: 0 0 14px;
  font-size: clamp(2rem, 3vw, 3rem);
}

.intro p:last-child {
  margin: 0;
  color: #355070;
  line-height: 1.8;
}

.upload-card {
  padding: 28px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 14px;
}

.upload-label {
  font-weight: 700;
  color: #143642;
}

.picker {
  min-height: 52px;
}

.upload-btn {
  min-height: 52px;
  border: none;
  border-radius: 999px;
  background: linear-gradient(135deg, #143642, #2a9d8f);
  color: #fff;
  font-weight: 700;
}

@media (max-width: 860px) {
  .detect-page {
    padding: 24px 14px 40px;
  }

  .detect-panel {
    grid-template-columns: 1fr;
  }
}
</style>
