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
