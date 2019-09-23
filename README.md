# Chariot Party

## Pré requis
  -> Vous aurez besoin de python en version 3

## Description
  -> Le but du projet chariot party est de créer un jeu similaire à un celebre jeux de la marque Japonaise avec sa celebre mascotte moustachu; où les joueurs, ici des chariots, se déplace sur un plateau généré aléatoirement.
  Le but est de récolter le plus de lingots d'or, qui sobtiennent en échangeant des charbons, qui eux meme se recoltent sur les cases du plateau de jeu.
	
### Déroulement du jeu :	
 1. le premier joueur lance le dé
 2. il se deplace en fonction du nombre donné par le dé
 3. selon la case sur laquelle le joueur tombe, soit il gagne du charbon (les cases vertes) soit il en pert (les cases rouge) soit rien ne se passe.
 4. si pendant son deplacement, il tombe sur la case correspondant au lingot d'or, il peut acheter cet OR si et seulement si il a réussi a récupérer au moins 10 hcarbons.

## How to play  
 - il suffit de lancer le script python avec la commande python : ‘python3 'leScript'.py‘  
 - pour toutes les étapes, on lance le script, et le jeu se lance avec une fenetre de jeu.  
 - à partir de l'étape 2, le teminal/invite de commande, demande a l'utilisateur :  
  * le nombre de joueurs voulus : un nombre entre 1 et 4  
  * le nombre de tour de jeu : au moins 1 tour.  
  * et le nombre de case pour le plateau : 4, 8, 12, 16 ou 20  
 - à partir de l'étape 3, le jeu joue tout seul, au tour par tour.  
    Il y a un affichage de ce qui se passe dans l'éxecution : 
    	- le tour X  
    	- le joueur X de jouer  
    	- le résultat du lancé de dé  
    	- et si le joueur passe sur une case avec un lingot  
    		+ affichage du nombre de charbon  
    		+ demande pour acheter un lingot. Si et seulement si le joueur en a assez pour en acheter (il faut 10 charbons)  
- à partir de l'étape 4, le jeu affiche les résultats et les exporte dans un fichier. si il y a une erreur lors de l'ouverture et/ou écriture du fichier, aucun fichier n'est créé.  
- à partir de l'étape 5 les changement sont avant tout interne : le code passe de l'impératif, a la programmation orienté objet  
- à l'étape 6, il y a un nouveau type de case : les case jaunes qui donne 10 charbons  
- à l'étape 7, les cases sont généré non plus totalement aléatoirement mais selon un calcul aléatoire en fonction d'un pourcentage d'apparition.  

## Découpage des échelons
- Chaque fichier correspond a un échelon:  
- le fichier stepOne.py correspond a l'échelon 1  
- le fichier stepTwo.py correspond a l'échelon 2  
- le fichier stepThree.py correspond a l'échelon 3  
- le fichier stepFour.py correspond a l'échelon 4  
- le fichier stepFive.py correspond a l'échelon 5  
- le fichier stepSix.py correspond a l'échelon 6  
- le fichier stepSeven.py correspond a l'échelon 7  

## Bonus
 Le jeu avec bonus se trouve dans le dossier eponyme : BONUS  
 Il s'execute comme ceci : python3 chariotsPartyBBR.py  
 Il contient :  
  - un mini jeu ou chaque tour les joueurs lance le dé, et celui qui fait le plus haut score, gagne 7 charbons  
  - et nous pouvons choisir la taille du dé en plus au debut de jeu (de 6 à 20 faces)

 Il contient aussi, en partie technique : une classe MiniGame, qui gere les mini jeux; une class Score: qui gere le score pour un mini jeu; une classe Dice : qui est en fait une classe spécifique pour le dé.
