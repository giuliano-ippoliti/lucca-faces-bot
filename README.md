# lucca-faces-bot
Exécuter dans la console du navigateur (F12...) et démarrer le jeu (bouton "Go"). Le bot continue à jouer et apprend. Score maximal obtenu : 1517 (sans bot il est pratiquement impossible de dépasser les 1000 points).

Selon la qualité de la connexion réseau, des erreurs peuvent survenir.

## Pour la petite histoire :)
En jouant de façon "régulière", le score maximal que j'ai obtenu a été de 974.

Je me suis ensuite rendu compte que je pouvais jouer sur les probabilités avec GSAutoClicker, en configurant des rafales de clicks sur le premier nom : 1 chance sur 4 de devenir le premier nom, 1/16 de deviner les 2 premiers, 1/64 de deviner les 3 premiers... 1/1024 de deviner les 5 premiers. Avec ce petit trick j'ai dépassé les 1100 points (environ 150 (score avec GSAutoClicker) * 5 + 80 (score "manuel") * 5).

J'ai ensuite codé un bot en utilisant le module python PyAutoGUI, en utilisant comme "signature" d'une image les coordonnées RGB de 2 pixel pris au hasard. Cela m'a permis de dépasser les 1300 points, mais pas plus, car la prise de screenshot est relativement chronophage.

Pour finir, j'ai vu qu'il y avait déjà sur le net un ancien bot (chez https://gist.github.com/nicolas-goudry). J'ai retenu l'idée d'utiliser une IIFE (Immediately Invoked Function Expression), mais j'ai tout recodé from scratch pour le fun, avec un peu d'aide de ChatGPT :) Le bot réalise une correspondance entre les noms et la taille des images. Cela m'a permis de dépasser les 1500 points, et je pense que c'est compliqué de faire mieux.
