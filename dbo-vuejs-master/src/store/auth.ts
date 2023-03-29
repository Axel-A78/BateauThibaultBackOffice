// auth.ts
interface AuthState {
  token: string | null;
}

const state: AuthState = {
  token: null,
};

const mutations = {
  setToken(state: AuthState, token: string) {
    state.token = token;
  },
};

const actions = {
  // Les actions pour la connexion, la déconnexion, etc.
};

const getters = {
  isAuthenticated(state: AuthState) {
    return !!state.token;
  },
  getToken(state: AuthState) {
    return state.token;
  },
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
};

export function loggedIn(): boolean {
  const accessToken = localStorage.getItem("token");
  if (accessToken) {
    // Si un jeton d'accès est présent dans le local storage, vérifiez s'il est expiré
    const { exp } = JSON.parse(atob(accessToken.split(".")[1]));
    return Date.now() < exp * 1000;
  }
  return false;
}
