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
import { useStore } from "vuex";
import { ref } from "vue";
import { useRouter, useRoute } from "vue-router";

export default {
  setup() {
    const store = useStore();
    const router = useRouter();
    const route = useRoute();
    const username = ref("");
    const password = ref("");

    const login = async () => {
      const requestOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: username.value,
          password: password.value,
        }),
      };
      try {
        const response = await fetch(
          "http://localhost:8000/api/token/",
          requestOptions
        );
        if (!response.ok) {
          throw new Error("Nom d'utilisateur ou mot de passe incorrect.");
        }
        const data = await response.json();
        // Utilisez la mutation 'setToken' du module 'auth' pour stocker le token
        store.commit("auth/setToken", data.access);
        // Rediriger l'utilisateur vers la page d'accueil ou une autre page protégée
        router.replace(route.query.redirect || "/");
      } catch (error) {
        console.log(error);
        alert(error.message);
      }
    };

    const clear = () => {
      username.value = "";
      password.value = "";
    };

    return {
      username,
      password,
      login,
      clear,
    };
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
