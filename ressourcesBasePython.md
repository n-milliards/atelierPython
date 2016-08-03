Mémo sur les principes de base de la programmation
===================================================

Les variables
---------------

On peut stocker dans des variables tout un tas d’informations. Pour ce faire, on leur affecte des valeurs avec l’opérateur `=`.

```python
age = 99
pi = 3.14
punchline = "zdedededex"
chemin_vers_mon_fichier = "images/image2.png"
beaucoup_info = (1, 2, 3)
est_ce_vrai = True
```
> on voit aussi ici les différents types de données  
> `99` est un entier (`int`)  
> `3.14` est un nombre à virgule (`float`)  
> `"zdedededex"` est une chaine de caractère (`str`)
> `(1, 2, 3)` est un tuple, une série d’information non modifiable  
> `True` est un booléen (`bool`) ne prenant pour valeur que `True` ou `False`

Il est possible d'effectuer des calculs avec :

```python
petunias = 6
serviettes = 7
reponse_a_la_vie = petunias * serviettes
```

Dans les programmes avec un minimum de complexité, on obtient rapidement des variables dont la valeur n'est plus connue d'avance : par exemple, du texte entré par l'utilisateur, les coordonnées de la souris, etc ... Nommer correctement ses variables est crucial pour s’y retrouver au milieu de toutes les informations que l'on manipule !

Les opérateurs
--------------

Pour effectuer des opérations et des comparaisons, nous avons besoin de symboles nommés **opérateurs**.

Il en existe différends types :


### Les opérateurs mathématiques
| Opérateur      | Effet         | Exemple |
| -------------- | ------------- | ------- |
| +  | addition | 3 + 7 == 10 |
| -  | soustraction | 7 - 6 == 1 |
| *  | multiplication | 3 * 7 == 21 |
| /  | division | 7 / 2 == 3.5 |
| %  | modulo (reste de la division entière) | 7 % 2 == 1 |


### Les opérateurs de comparaisons

| Opérateur      | Signification |
| -------------- | ------------- |
| a `<` b  | *a* est `strictement inférieur` à *b* |
| a `>` b  | *a* est `strictement supérieur` à *b* |
| a `<=` b  | *a* est `inférieur ou égal` à *b* |
| a `>=` b  | *a* est `supérieur ou égal` à *b* |
| a `==` b  | *a* est `strictement égal` à *b* |
| a `!=` b  | *a* est `différend` de *b* |
 
### Les opérateurs logiques

| Opérateur      | Utilisation | Signification |
| -------------- | ----------- | ------------- |
| `or`  | if (a > 0) `or` (b > 0) | (a > 0) OU (b > 0) |
| `and`  | if (a > 0) `and` (b > 0) | (a > 0) ET (b > 0) |
| `not` | if `not` (False) | opposé de la condition |


## Les fonctions

On défini une fonction en commençant la ligne par `def` puis le nom qu’on lui donne suivi de parenthèses. Enfin on termine la ligne par `:` qui suppose une suite d’instructions à exécuter lorsqu’on appelle notre fonction.  
Ces instructions doivent être indentées d'une tabulation ou de quelques espaces.

```python
def demanderUnNom() :
	nom = input("Entrez un nom :")
	return nom
```

On exécute une fonction en l’appellant dans notre code :

```python
# Cette instruction propose à l’utilisateur d’écrire un nom dans 
# l’invite de commande et imprime par la suite sur l’écran ce même nom.
print(demanderUnNom())
```

Une fonction peut dépendre de **paramètres**, c’est-à-dire une ou plusieurs informations importantes dont la fonction doit avoir connaissance pour réaliser ses instructions. On les spécifie entre parenthèses et on les sépare par des virgules.

```python
def demanderUnNom(parametre1, parametre2) :
	nom = input(parametre1)
	message = parametre2 + nom + " !"
	return message
	
demande = "Entrez un nom :"
formule = "Bonjour "

# On exécute la fonction demanderUnNom avec pour parametre1 le contenu de 
# la variable ‘demande’ et parametre2 ‘formule’ définis juste avant.
print(demanderUnNom(demande, formule))
```
> Entrez un nom :  
> => *leNomQueVousDonnez*  
> Bonjour *leNomQueVousAvezDonné* !


## Les conditions

L'instruction `if` permet de vérifier si une condition est remplie. Si elle l’est, le code indenté suivant sera exécuté. Avec `else` on indique ce qu’il doit être exécuté dans le cas contraire. Si plusieurs conditions sont possibles on peut utiliser `elif`

Syntaxe générale :

```python
# Défini la variable ‘condition’ comme ‘vrai’
condition = True

# SI ‘condition’ est ‘vrai’
if (condition) : 
    # Imprime à l’écran le texte suivant
    print("La variable condition vaut True !")

# SINON SI
elif (condition != True and condition != False):
    print("il se passe un truc chelou")

# SINON    
else :
    # Imprime celui-ci
    print("La variable condition vaut False !")

print("Ce message s'affiche quoi qu'il arrive")
```

Exemples avec différents opérateurs :

```python
# Egalité (par exemple d'une chaine de caractère)
if (variable == "plop")
# Comparaison de valeur numérique
if (variable > 3.14)
# Negation de la precedente condition
if not (variable > 3.14)
# Condition 1 ET condition 2
if (variable1 == "plop") and (variable2 > 3.14)
# Condition 1 OU condition 2
if (variable1 == "plop") or (variable2 > 3.14) 
```


## Les listes

Les listes permettent de contenir des séries d’éléments, énoncés entre crochets `[ ]` :

```python
todoAtelier = [ "slides", "exercices", "images", "ressources"]
```

On peut accéder à un élément via sa position (**index**). Attention, en programmation, les index commencent systématiquement par 0. Pour accéder au premier élément d’une liste, il faut donc demander l’index numéro 0.

Pour afficher par exemple le 3ème élément de notre liste il faut écrire :

```python
print("Voici la 3ème chose à faire :")
print(todoAtelier[2])
```
> Voici la 3ème chose à faire :  
> images

Suivant le même principe, il est possible de modifier une valeur dans la liste :
```python
todoAtelier[2] = "sprites"
```

Il est également possible d'ajouter des éléments dans une liste après son initialisation, avec la méthode `append()` :

```python
# Ajoute un élément à la fin de la liste ‘todoAtelier’ 
todoAtelier.append("n milliards d’autres trucs")
```



## Les boucles

### Boucle `for`

La boucle `for` permet d'effectuer un ensemble d'instructions pour chaque élément d'une liste


```python
print("Voilà ce que tu dois faire :")

# Pour chaque element dans L
for tache in todoAtelier :
  # Afficher l'element
  print(tache)
```
> Voilà ce que tu dois faire :  
> slides  
> exercices  
> images  
> ressources  


### Boucle `while`

La boucle `while` permet d’exécuter en boucle des instructions tant qu'une condition est vraie.

```python
# Tant que je ne suis pas le meilleur dresseur
while (bestPokemonTrainer != me) :
    # Capturer plus de pokemons
    captureMorePokemon()
```

Autre exemple :

```python
# Défini continuer comme variable globale avec pour valeur "oui"
continuer = "oui"

# Tant que ‘continue’ est strictement égal à ‘oui’
while (continuer == "oui") :
    # Demande à l’utilisateur s’il souhaite continuer à exécuter la boucle et 
    # stocke le résultat dans la variable ‘continuer’
    continuer = input("Écrit ‘oui’ si tu est persévérant\n")

# Imprime un message d’encouragement si l’utilisateur provoque la fin de la boucle    
print("noob")
```
> Ce programme demandera à l’utilisateur constamment s’il est persévérant jusqu’à ce que celui-ci craque et écrive autre chose que ‘oui’

## Les dictionnaires

Les dictionnaires sont un peu comme les listes sauf que chaque *élément* possède une clé et une valeur. C’est donc via leur clé que nous pourrons accéder à leur valeur. De plus ils n’ont pas d’ordres particulier (une boucle `for` affichera par exemple la 3ème clé avant la 2ème).    

Cela permet par exemple de donner un nom à un chemin de fichier, et de récupérer ceux-ci grâce à leur nom. 


```python
imgDict = {
    "perso" : "img/perso.png",
    "mur" : "img/mur.png",
    "sol" : "img/solVersion3.png",
}

# Récupérer le chemin de l'image du personnage :
print(imgDict["perso"])
```
> imgs/perso.png

On peut parcourir un dictionnaire et imprimer ses clés avec une boucle `for` :

```python
# on utilise la méthode keys() pour récuperer les clé
for nom_image in imgDict.keys():
    print(nom_image)
```
> mur  
> perso  
> sol

Pour le faire avec les valeurs on fait :

```python
# on utilise la méthode values() pour récuperer les valeurs
for chemin_image in imgDict.values():
    print(chemin_image)
```
> img/solVersion3.png  
> img/mur.png  
> img/perso.png 

Et pour récupérer à la fois les clés et les valeurs, c’est ainsi :

```python
# on utilise la méthode items() pour récuperer les clés et les valeurs
for nom_image, chemin_image in imgDict.items():
    print(nom_image + " se trouve dans " + chemin_image)
```
> perso se trouve dans img/perso.png  
> sol se trouve dans img/solVersion3.png  
> mur se trouve dans img/mur.png


## Ouvrir et lire un fichier

Il est commun de vouloir ouvrir un fichier pour lire ou écrire de l'information qui est ou sera stockée en dehors du programme. La syntaxe suivante permet d'ouvrir le fichier et de le refermer automatiquement une fois que l'on a réalisé les opérations souhaitées :

```python
# Ouvre le fichier en mode lecture seule (r pour read) 
# et le stocke dans la variable monFichier
with open("nomDuFichier", r) as monFichier :
    # Opérations sur le fichier
``` 

Le contenu du fichier est alors accessible via `f.readlines()`

```python
# Déclare une liste vide
contenu = [ ]

with open("nomDuFichier", r) as monFichier :
    
    # On récupère le contenu du fichier avec readlines()
    contenu = monFichier.readlines()
    
print(contenu)
``` 
