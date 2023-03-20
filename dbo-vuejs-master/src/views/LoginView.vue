<template>
  <div class="login-container">
    <div class="p-card login-card">
      <h2 class="p-text-center">Connexion</h2>
      <div class="p-fluid">
        <div class="p-field p-mt-4">
          <label for="username">Nom d'utilisateur</label>
          <input
            type="text"
            id="username"
            v-model="username"
            class="p-inputtext p-component p-filled"
          />
        </div>
        <div class="p-field p-mt-4">
          <label for="password">Mot de passe</label>
          <input
            type="password"
            id="password"
            v-model="password"
            class="p-inputtext p-component p-filled"
          />
        </div>
        <div class="p-d-flex p-jc-between p-mt-6">
          <div class="card flex justify-content-center">
            <Button
              type="button"
              label="Se connecter"
              icon="pi pi-user"
              @click="login"
            />
          </div>
          <div>
            <Button label="Effacer" @click="clear" text raised />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    login() {
      // const token = localStorage.getItem("token");
      const requestOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: this.username,
          password: this.password,
        }),
      };
      fetch("http://localhost:8000/api/token/", requestOptions)
        .then((response) => {
          if (!response.ok) {
            throw new Error("Nom d'utilisateur ou mot de passe incorrect.");
          }
          return response.json();
        })
        .then((data) => {
          // Stocker le jeton d'authentification dans le local storage pour une utilisation ultérieure
          localStorage.setItem("token", data.access);
          // Rediriger l'utilisateur vers la page d'accueil ou une autre page protégée
          this.$router.replace(this.$route.query.redirect || "/test");
        })
        .catch((error) => {
          console.log(error);
          alert(error.message);
        });
    },
    clear() {
      this.username = "";
      this.password = "";
    },
  },
};
</script>

<style scoped>
.login-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-card {
  width: 90%;
  max-width: 400px;
}
</style>
