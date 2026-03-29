<template>
  <main class="about-page">
    <section class="header-card">
      <p class="eyebrow">Team</p>
      <h1>Built by the ISL recognition capstone team</h1>
      <p>
        This project brings together model experimentation, web development, and interface design to create an approachable prototype for Indian Sign Language recognition.
      </p>
    </section>

    <section class="member-grid">
      <article v-for="(name, index) in names" :key="index" class="member-card">
        <div class="avatar">{{ initials(name) }}</div>
        <div class="info">
          <h2>{{ name }}</h2>
          <p>{{ descriptions[index] }}</p>
          <p class="role">{{ roles[index] }}</p>
        </div>
      </article>
    </section>
  </main>
</template>

<script>
export default {
  name: "AboutUs",
  data() {
    return {
      names: ["Soham Gada", "Archit Menghani", "Siddhanth Salian"],
      descriptions: [
        "Focused on structured execution, reliable teamwork, and turning project goals into clear implementation steps.",
        "Committed to disciplined problem-solving, consistent delivery, and maintaining momentum across the project lifecycle.",
        "Driven by practical development work, interface refinement, and improving how users experience the overall system.",
      ],
      roles: [
        "Research and planning",
        "Implementation and coordination",
        "Development and product experience",
      ],
    };
  },
  methods: {
    initials(name) {
      return name
        .split(" ")
        .map((part) => part[0])
        .join("")
        .slice(0, 2)
        .toUpperCase();
    },
  },
};
</script>

<style scoped>
.about-page {
  max-width: 1080px;
  margin: 0 auto;
  padding: 28px 24px 56px;
}

.header-card,
.member-card {
  background: rgba(255, 255, 255, 0.84);
  border: 1px solid rgba(20, 54, 66, 0.08);
  box-shadow: 0 18px 40px rgba(20, 54, 66, 0.08);
}

.header-card {
  padding: 32px;
  border-radius: 28px;
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

.header-card h1 {
  margin: 0 0 10px;
}

.header-card p:last-child {
  margin: 0;
  line-height: 1.8;
  color: #355070;
}

.member-grid {
  display: grid;
  gap: 18px;
}

.member-card {
  display: grid;
  grid-template-columns: 110px 1fr;
  gap: 20px;
  align-items: center;
  padding: 24px;
  border-radius: 24px;
}

.avatar {
  width: 86px;
  height: 86px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #143642, #2a9d8f);
  color: #fff;
  font-size: 1.4rem;
  font-weight: 800;
}

.info h2 {
  margin: 0 0 10px;
}

.info p {
  margin: 0 0 10px;
  line-height: 1.75;
  color: #355070;
}

.role {
  color: #2a9d8f;
  font-weight: 700;
}

@media (max-width: 720px) {
  .about-page {
    padding: 24px 14px 40px;
  }

  .member-card {
    grid-template-columns: 1fr;
  }
}
</style>
