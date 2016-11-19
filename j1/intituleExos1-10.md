# Construction d'un jeu vidéo text-based

#### Exercice 1 : un premier programme

Taper et lancer le programme suivant :

```python
message = "Je connais la réponse à la vie et l'univers !"
reponse = 6 * 7

print("Salut !")
print(message)
print(reponse)
```

#### Exercice 2 : les variables

Taper et lancer le programme suivant :

```python
message = "Je connais la réponse à la vie et l'univers !"
reponse = 6 * 7

print("Salut !")
print(message)
print(reponse)
```

#### Exercice 3 : Interactivité

Taper et lancer le programme suivant :

```python
nom = input("Entrez un nom : ")
message = "-- Tut tut tut... Réveillez-vous " + nom + " !"

print(message)
```

#### Exercice 4 : Les fonctions

Taper et lancer le programme suivant :

```python
def demander_nom():
    reponse = input("Entrez un nom : ")
    return reponse


message = "-- Tut tut tut... Réveillez-vous " + demander_nom() + " !"

print(message)
```

#### Exercice 5 : Les conditions

Ajouter à la fonction `demander_nom()` : si le nom fait moins de 6 caractères, afficher un message, sinon affiche un autre message.

Vous pouvez utiliser `len(chaine)` pour connaître la longueur d'une chaîne de caractère

#### Exercice 6 : Arguments des fonctions

Modifier la fonction `demander_nom()` pour que la taille du nom soit donnée en argument

#### Exercice 7 : Les boucles `while`

Définir une fonction `reveil_relou()` qui, en boucle :
- affiche "Tut tut tut"
- demande un mot de passe à l'utilisateur
Tant qu'il n'a pas donné le bon mot de passe.

#### Exercice 8 : Les boucles `for`

Ajoutez à la fonction un compteur qui s'incrémentera à chaque mauvais mot de passe, et une boucle `for` qui affichera autant de "Tut tut tut..." que le compteur.

#### Exercice 9 : Les listes

Déclarer dans le programme une liste contenant les pièces de la maison et l'afficher après que le réveil ait fini de sonner !

On peut prendre les pièces : chambre, cuisine et salle de bain.

#### Exercice 10 : Les dictionnaires

Créer un dictionnaire avec l'état du personnage après son réveil :
- propre, habillé·e, affamé·e, reveillé·e
- utiliser des booléens (`True`/`False`)

Faire une boucle qui affiche l'état du personnage.