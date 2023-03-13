# TME 2 Frontend

Le but de ce TME est de gérer l'authentification dans le projet.
Pour ce projet on utilisera des <a href="https://jwt.io/">JWT</a>.

Le projet backend doit nous fournir des routes REST permettant de récupérer deux types de token :

- access token
- refresh token

Si vous avez finis le TME de sécurité en backend vous devez avoir des routes "sécurisées", qui ne permettent pas d'accèder sans headers authorizations. (renvoie une erreur 401 ou 403)

## Exercice 1

Créer une page de login permettant de récupérer les tokens.

Si vous avez une route de création d'utilisateur créez également une page pour créer un compte.

Stocker ces tokens dans le store (et le localstorage).

Gérer le routeur pour que quand un token valide est présent la route par défaut arrive sur le home sinon directement sur la page login.

## Exercice 2

Modifier vos fonctions qui appellent l'API pour qu'elles utilisent un token.

Vérifier que vous arrivez bien à afficher les données comme au TME précédent.

Rappel:

Vous devez ajouter un header `authorization` qui "bear" le token :

```typescript
fetch(URL, {
  headers: { authorization: `Bearer ${token}` },
})
```
