<template>
  <div class="card-container">
    <div
      class="p-d-flex p-jc-center p-ai-center"
      style="height: 100vh; width: 100vh"
    >
      <div class="p-shadow-2 p-p-6 p-col-10 p-md-4 p-lg-4">
        <h2 class="titre p-text-center">Bienvenue</h2>
        <p>Veuillez vous inscrire ou vous connecter</p>
        <div class="btns">
          <div class="p-col-12 p-mb-3 p-p-md-0">
            <button
              class="p-button p-button-rounded p-button-outlined p-button-lg p-button-success p-text-center"
              @click="login"
            >
              Connexion
            </button>
          </div>
          <div class="p-col-12 p-p-md-0">
            <button
              class="p-button p-button-rounded p-button-lg p-button-primary p-text-center"
              @click="register"
            >
              Inscription
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    login() {
      this.$router.push("/login");
    },
    register() {
      // Appeler la fonction d'inscription
    },
  },
};
</script>

<style scoped>
.titre,
p {
  display: flex;
  justify-content: center;
}
.btns {
  display: flex;
  justify-content: center;
}
.card-container {
  align-items: center;
  display: flex;
  height: 100vh;
  margin-left: 25%;
}
.p-shadow-2 {
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 2px 10px 0 rgba(0, 0, 0, 0.12) !important;
}
.p-button-success {
  background-color: #3f51b5 !important;
  color: #fff !important;
}
.p-button-primary {
  background-color: #3f51b5 !important;
  color: #fff !important;
}
</style>
