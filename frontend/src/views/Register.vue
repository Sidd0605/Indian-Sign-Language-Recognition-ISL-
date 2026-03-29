<template>
  <div class="register-page">
    <form class="register-card" @submit.prevent="submitForm">
      <p class="eyebrow">Stay Connected</p>
      <h1>Register for future ISL project updates</h1>

      <label for="fullName">Full Name</label>
      <input id="fullName" v-model.trim="form.fullName" type="text" required>

      <label for="email">Email Address</label>
      <input id="email" v-model.trim="form.email" type="email" required>

      <label for="phone">Phone Number</label>
      <input id="phone" v-model.trim="form.phone" type="tel" required>

      <button type="submit">Register</button>
      <p v-if="message" class="message">{{ message }}</p>
    </form>
  </div>
</template>

<script>
export default {
  name: "Register",
  data() {
    return {
      form: {
        fullName: "",
        email: "",
        phone: "",
      },
      message: "",
    };
  },
  methods: {
    submitForm() {
      this.message = "Registration details captured locally. You can connect this form to a database or email workflow later.";
      this.form = {
        fullName: "",
        email: "",
        phone: "",
      };
    },
  },
};
</script>

<style scoped>
.register-page {
  min-height: calc(100vh - 90px);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.register-card {
  width: min(100%, 440px);
  padding: 28px;
  border-radius: 22px;
  background: rgba(255, 255, 255, 0.9);
  box-shadow: 0 18px 40px rgba(20, 54, 66, 0.08);
  border: 1px solid rgba(20, 54, 66, 0.08);
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.eyebrow {
  margin: 0;
  color: #2a9d8f;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  font-size: 0.76rem;
  font-weight: 700;
}

h1 {
  margin: 0 0 6px;
  line-height: 1.1;
}

label {
  font-weight: 600;
}

input {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid #c9ced6;
  border-radius: 10px;
}

button {
  margin-top: 8px;
  padding: 12px;
  border: none;
  border-radius: 999px;
  background: #143642;
  color: #fff;
  font-weight: 700;
}

.message {
  margin: 0;
  color: #1d3557;
  line-height: 1.6;
}
</style>
