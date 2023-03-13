# TME 1 Frontend

Le but de ce TME est de commencer le projet frontend du backoffice.
Ce projet utilisera Vuejs.

Les objectifs de la séance sont :

- lancer le projet en local
- afficher la liste de produits déjà présent dans le store du projet
- commencer la création des composants nécessaire au développement des pages du backoffice
- utiliser des données d'une API distante

## Exercice 1: Installation de l'environment

Clonez le repository github sur votre machine et lancez les commandes suivantes :

Pour installer les dépendances:

```sh
yarn #installez yarn et/ou node si ce n'est pas déjà le cas
```

Pour lancer le projet:

```sh
yarn serve
```

Vérifiez que le projet tourne bien sur le port 8080

http://localhost:8080

## Exercice 2: Première modifications

Si la couleur du header ne vous satisfait pas, changez la !

Dans le store de l'application se trouve les données renvoyé par le serveur vu en TME backend.
(Pour le moment nous nous satisferont de données statiques).

Utilisez ces données pour afficher une liste de produits de la mer avec leur description.

Vous pouvez trouver des inspirations de designs dans le dossier `design-inspirations`.

## Exercice 3 récupérer des données du backend

On veut maintenant pouvoir récupérer les informations initialement contenu dans le store directement du backend.

Créez un fichier et un dossier api dans lequel vous écrirez le code utilisant l'API distante.

Créez une fonction renvoyant une <a href="https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Promise">promesse</a> du résultat.

(Pour faire un appel http[s] utilisez de préférence <a href="https://developer.mozilla.org/en-US/docs/Web/API/fetch">fetch</a>)
