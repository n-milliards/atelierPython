Initiation à la programmation et réalisation d'un jeu vidéo en Python - Atelier 1
=================================================================================

Exercice 1 - Écrire un programme et le lancer
---------------------------------------------

Tapez les lignes suivantes dans un nouveau fichier :

```python
nom = input("Entrez un nom : ")
message = "Bonjour " + nom + " !"

print(message)
```

Enregistrez le fichier sous le nom `programme.py`, et tapez `python programme.py` dans le terminal pour l'éxecuter.

Exercice 2 - Écrire une fonction
--------------------------------

Modifier le programme de l'exercice 1 pour qu'il devienne :

```python
def demanderUnNom() :
    nom = input("Entrez un nom :")
    return nom

print("Bonjour" + demanderUnNom() + "!")
```

Executez le programme

Exercice 3 - Utilisation des conditions
---------------------------------------

Modifiez le programme précédent en utilisant une condition pour afficher un message différent si le nom est "Bernard".

Exercice 4 - Mot de passe
-------------------------

Écrivez un programme qui demande un mot de passe jusqu'à ce qu'il donne le bon. (Indice : se servir d'une boucle `while`)

Exercice 5 - Somme d'une liste d'entiers
----------------------------------------

Écrivez un programme qui initialise une liste d'entiers, et calcule la somme de ses éléments

Exercice 6 - (Optionnel) Suite de Fibonnaci
-------------------------------------------

La suite de Fibonnaci est une suite particulière en mathématiques, qui a notamment un lien avec le nombre d'or.

Elle commence comme ceci :

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Chaque élément est défini comme la somme des deux précédents.

Écrivez un programme qui calcule la suite de Fibonnaci jusqu'au rang 20.

Exercice 7 - Premier programme avec Pygame
------------------------------------------

Récuperez le programme de base permettant d'ouvrir une fenêtre avec Pygame.

Exercice 8 - Couleur de fond
----------------------------

Modifiez le programme pour remplir la fenêtre avec une couleur de fond.

Exercice 9 - Utiliser une image
-------------------------------

Chargez une image en mémoire et dessinez là dans la fenêtre de jeu.

Exercice 10 - Bouger l'image avec la souris
-------------------------------------------

Utilisez l'événement `MOUSEMOTION` pour changer la position de l'image en fonction de la position de la souris.
