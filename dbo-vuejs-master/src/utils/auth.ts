export function loggedIn(): boolean {
  const accessToken = localStorage.getItem("access_token");
  if (accessToken) {
    // Si un jeton d'accès est présent dans le local storage, vérifiez s'il est expiré
    const { exp } = JSON.parse(atob(accessToken.split(".")[1]));
    return Date.now() < exp * 1000;
  }
  return false;
}
