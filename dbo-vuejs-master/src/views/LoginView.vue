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
        <div>
          <div class="login-card flex justify-content-center">
            <Button
              type="button"
              label="Se connecter"
              icon="pi pi-user"
              @click="login"
            />
          </div>
          <div class="clear-card flex justify-content-center">
            <Button class="clearbtn" label="Effacer" @click="clear" link />
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
  justify-content: center;
}
h2 {
  width: 400px;
  display: inline-block;
  padding-left: 150px;
}
label {
  margin-left: 12.5%;
}
input {
  max-width: 75%;
  margin-left: 12.5%;
  margin-top: 10px;
  margin-bottom: 10px;
}
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

.p-button.p-component {
  width: 400px;
  max-width: 100%;
  border-radius: 10px;
}

.p-button.p-component.p-button-raised.p-button-text {
  border-radius: 10px;
}

.p-button.p-component.p-button-link.clearbtn {
  max-width: fit-content;
}

.login-card.flex.justify-content-center {
  width: 50%;
  margin-top: 5%;
  margin-left: 25%;
}

.clear-card.flex.justify-content-center {
  width: 50%;
  margin-bottom: 1%;
  margin-top: 5%;
  margin-left: 40%;
}
</style>
