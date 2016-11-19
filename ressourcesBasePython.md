Mémo sur les principes de base de la programmation
===================================================

Les variables
---------------

### Définir des variables
On peut stocker dans des variables tout un tas d’informations. Pour ce faire, on leur affecte des valeurs avec l’opérateur d'affectation `=`.

```python
age = 99
pi = 3.14
punchline = "zdedededex"
chemin_vers_mon_fichier = "images/image2.png"
beaucoup_info = (1, 2, 3)
est_ce_vrai = True
```
On voit aussi ici les différents types de données :

> `99` est un entier (`int`)  
> `3.14` est un nombre à virgule (`float`)  
> `"zdedededex"` est une chaine de caractère (`str`)  
> `(1, 2, 3)` est un `tuple`, une série d’information non modifiable  
> `True` est un booléen (`bool`) ne prenant pour valeur que `True` ou `False`

On peut utiliser `type()`, décrite plus bas, pour connaître le type d’une variable ou d'une valeur

### Les opérateurs mathématiques

Pour effectuer des opérations nous avons besoin de symboles nommés **opérateurs**.

Il en existe différends types :


| Opérateur      | Effet         | Exemple |
| -------------- | ------------- | ------- |
| +  | addition | 3 + 7 == 10 |
| -  | soustraction | 7 - 6 == 1 |
| *  | multiplication | 3 * 7 == 21 |
| /  | division | 7 / 2 == 3.5 |
| %  | modulo (reste de la division entière) | 7 % 2 == 1 |

On peut ainsi effectuer des opérations entre variables :

```python
petunias = 6
serviettes = 7
reponse_a_la_vie = petunias * serviettes
```

Dans les programmes avec un minimum de complexité, on obtient rapidement des variables dont la valeur n'est plus connue d'avance : par exemple, du texte entré par l'utilisateur, les coordonnées de la souris, etc ... **Nommer correctement ses variables est crucial pour s’y retrouver au milieu de toutes les informations que l'on manipule !**

### Manipuler des chaînes de caractères

Pour construire et afficher des chaînes de caractères, il est possible de combiner plusieurs chaînes. Cette combinaison s’appelle la _concaténation_.

On peut utiliser l’opérateur `+` :

```python
mot = "world"
concatenation = "hello, " + mot + " !"

print(concatenation)
```

> hello, world !


On peut utiliser la virgule pour séparer les différents éléments en arguments d’un `print()`,la fonction print ajoutera automatiquement une espace entre chaque arguments :

```python
mot = "world"
print("hello,", mot, "!")
```
>hello, world !


On peut changer l’ajout automatique d’une espace par un autre caractère en ajoutant l’argument `sep=""`:

```python
mot = "world"
print("hello,", mot, "!", sep="/")
```
> hello,/world/!



Quelques fonctions de base
---------------

### print()
Afficher quelque chose dans le terminal

```python
print("réponse à la vie")
``` 
> réponse à la vie

```python
reponse_a_la_vie = 42
print(reponse_a_la_vie)
```
> 42

### type()
Pour connaître le type d’un objet on utilise la fonction `type()`

```python
chaine = "une chaine de caractères"
nombre = 3
booleen = True

print(type(chaine))
print(type(nombre))
print(type(booleen))
``` 
>\<class 'str'>  
>\<class 'int'>  
>\<class 'bool'>


### input()
Demander à l’utilisateur une information

```python
# Exécute la fonction ‘input()’, et stocke ce que 
# l’utilisateur a écrit dans cette variable
pokemon = input("Donne moi un pokemon : ")
print(pokemon + "est super !")
``` 
> Donne moi un pokemon :

on donne un pokemon comme « Reptincel », et le programme imprimera donc :
> Reptincel est super !


### len()
Donne le nombre de caractères d’une ‘string’, le nombre d’éléments dans une liste ou un dictionnaire

```python
chaine = "une chaîne de caractères un peu longue"
liste = [1, 2, 3, "quatre"]
dico = {"douze": "a", "neuf": "b", "sept": "c"}

print(len(chaine), len(liste), len(dico))
``` 
> 38 4 3
 

### int()
Transforme le type d’un objet en `int`.

```python
nombre = "1"
print(type(nombre))

nombre_int = int(nombre)
print(type(nombre_int))
```
> \<class 'str'>  
> \<class 'int'>

```python
# Par exemple un utilisateur entre un nombre à la suite d’un input()
nombre = input("Entrez un nombre :")
# input() retourne toujours une string donc si l’utilisateur à écrit 1
# il faut transformer la string ("1") en int (1) sinon une erreur apparaît
calcul = int(nombre) + 5 
print(calcul)
``` 
> 6

Si un utilisateur entre quelque chose comme "un", une erreur apparaitrait car on ne peut transformer du texte en int.


### str()
Transforme le type d’un objet en `string`.

```python
nombre = 3482
boleen = True
print(type(nombre), type(boleen))

nombre_str = str(nombre)
boleen_str = str(boleen)
print(type(nombre_str), type(boleen_str))
``` 
> \<class 'int'> <class 'bool'>  
> \<class 'str'> <class 'str'>



Les fonctions
---------------

On défini une fonction en commençant la ligne par `def` puis le nom qu’on lui donne suivi de parenthèses. Enfin on termine la ligne par `:` qui suppose une suite d’instructions à exécuter lorsqu’on appelle notre fonction.  
Ces instructions doivent être indentées de 4 espaces. Cette indentation n’est pas seulement esthétique contrairement à d’autres langages, c’est la manière dont on indique à l’interpréteur Python que ces instructions font partie de la fonction (idem pour les conditions et les boucles). 

```python
def demanderUnNom():
	nom = input("Entrez un nom :")
	return nom
```

On exécute une fonction en l’appelant dans notre code :

```python
# Cette instruction propose à l’utilisateur d’écrire un nom dans 
# l’invite de commande et imprime par la suite sur l’écran ce même nom.
print(demanderUnNom())
```

Une fonction peut dépendre d’**arguments**, c’est-à-dire une ou plusieurs informations importantes dont la fonction doit avoir connaissance pour réaliser ses instructions. On les spécifie entre parenthèses et on les sépare par des virgules.

```python
def demanderUnNom(argument1, argument2):
	nom = input(argument1)
	message = argument2 + nom + " !"
	return message
	
demande = "Entrez un nom :"
formule = "Bonjour "

# On exécute la fonction demanderUnNom avec pour argument1 le contenu de 
# la variable ‘demande’ et argument2 ‘formule’ définis juste avant.
print(demanderUnNom(demande, formule))
```
> Entrez un nom :  
> => *leNomQueVousDonnez*  
> Bonjour *leNomQueVousAvezDonné* !


### Les _variables globales_ versus les _variables locales_

Les variables peuvent être _locales_ (uniquement accessibles à l’intérieur d’une fonction ou d’une classe) ou _globales_, accessibles en tout temps car déclarées au premier niveau du flux d’instructions ou à l’intérieur d’une boucle ou d’une condition.

```python
a = 6
b = 10

def calculer(nombre1, nombre2):
    resultat = nombre1 + nombre2 / 2
    return resultat

# ‘a’ et ‘b’ sont des variables déclarées au premier niveau et sont donc accessibles
print(a, b)

# /!\ ‘resultat’ n’est pas accessible car elle est déclarée dans une fonction 
print(resultat)

# ‘resultat’ ne peut être récupérée qu’en appelant la fonction calculer()
# qui nous renvoit sa valeur avec ‘return'
print(calculer(a, b))
```

### Valeur de retour

Pour pouvoir exploiter le résultat d'une fonction depuis l'endroit où on l’appelle, on 'retourne' ou 'renvoie' cette information avec le mot-clé `return`. On peut ainsi stocker le résultat d'une fonction dans une variable pour l'utiliser par la suite. C'est ce qu'il se passe dans le programme suivant :

```
def demanderUnNom():
	nom = input("Entrez un nom :")
	return nom
	
nom_du_personnage = demanderUnNom()
```

Lorsque `return` est appelé, l’exécution de la fonction cesse, et le programme continue là où la fonction était appelée.


Les conditions
---------------

Il est possible de comparer des variables ou des valeurs entres elles avec différents opérateurs :

### Les opérateurs de comparaisons

| Opérateur      | Signification |
| -------------- | ------------- |
| a `==` b  | *a* est `strictement égal` à *b* |
| a `!=` b  | *a* est `différend` de *b* |
| a `<` b  | *a* est `strictement inférieur` à *b* |
| a `>` b  | *a* est `strictement supérieur` à *b* |
| a `<=` b  | *a* est `inférieur ou égal` à *b* |
| a `>=` b  | *a* est `supérieur ou égal` à *b* |

### Les opérateurs logiques

| Opérateur      | Utilisation | Signification |
| -------------- | ----------- | ------------- |
| `or`   | if(a > 0 `or` b > 0)  | a > 0 OU b > 0 |
| `and`  | if(a > 0 `and` b > 0) | a > 0 ET b > 0 |
| `not`  | if `not`(False)       | opposé de la condition |

### if / else

L'instruction `if` permet de vérifier si une condition est remplie. Si elle l’est, le code indenté suivant sera exécuté. Avec `else` on indique ce qu’il doit être exécuté dans le cas contraire. Si plusieurs conditions sont possibles on peut utiliser `elif`

Syntaxe générale :

```python
# Défini la variable ‘condition’ comme ‘vrai’
condition = True

# SI ‘condition’ est ‘vrai’
if(condition): 
    # Imprime à l’écran le texte suivant
    print("La variable condition vaut True !")

# SINON SI
elif(condition != True and condition != False):
    print("il se passe un truc chelou")

# SINON    
else:
    # Imprime celui-ci
    print("La variable condition vaut False !")

print("Ce message s'affiche quoi qu'il arrive")
```

Exemples avec différents opérateurs :

```python
# Egalité (par exemple d'une chaine de caractère)
if(variable == "plop"):
# Comparaison de valeur numérique
if(variable > 3.14):
# Négation de la précédente condition
if not(variable > 3.14):
# Condition 1 ET condition 2
if(variable1 == "plop") and (variable2 > 3.14):
# Condition 1 OU condition 2
if(variable1 == "plop") or (variable2 > 3.14):
```


Les listes
---------------

Les listes permettent de contenir des séries d’éléments, énoncés entre crochets `[ ]` :

```python
todoAtelier = ["slides", "exercices", "images", "ressources"]
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

### append()

Il est également possible d'ajouter des éléments dans une liste après son initialisation, avec la méthode `append()` :

```python
# Ajoute un élément à la fin de la liste ‘todoAtelier’ 
todoAtelier.append("n milliards d’autres trucs")
```

### range()

Créé une séquence de nombre que l’on utilisera essentiellement dans des boucles `for`.

```python
liste = range(10)
# On utilise ici list() pour convertir directement range() en liste afin de l’afficher
print(list(liste))
```
> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

On peut donner en argument de `range()` un nombre de départ, celui de fin et enfin l’étape. Quand on n’indique pas tous les arguments, le nombre par défaut de départ sera 0 et l’étape sera de 1 comme dans le 1er exemple.  

```python
# créé une séquence commençant par 2 et ajoutant 2 jusqu’à 10
liste = range(2, 10, 2)
print(list(liste))
```
> [2, 4, 6, 8]

/!\ Le nombre de départ et de fin sont des index, par conséquent [1] == 0, [2] == 1, ... 


Les boucles
---------------

### Boucle `for`

La boucle `for` permet d'effectuer un ensemble d'instructions pour chaque élément d'une liste


```python
print("Voilà ce que tu dois faire :")

# Pour chaque élément dans L
for tache in todoAtelier:
  # Afficher l’élément
  print(tache)
```
> Voilà ce que tu dois faire :  
> slides  
> exercices  
> images  
> ressources  

### enumerate(list)
Permet de récupérer à la fois l’`index` et la `valeur` d’un **itérable** (liste, string, fichier) lors d’une boucle `for`

```python
liste = ["zéro", "un", "deux", "trois"]
for index, valeur in enumerate(liste):
    print("l’index est :", str(index), "la valeur de celui-ci est :", valeur)
``` 

>l’index est : 0 la valeur de celui-ci est : zéro  
>l’index est : 1 la valeur de celui-ci est : un  
>l’index est : 2 la valeur de celui-ci est : deux  
>l’index est : 3 la valeur de celui-ci est : trois

### Boucle `while`

La boucle `while` permet d’exécuter en boucle des instructions tant qu'une condition est vraie.

```python
# Tant que je ne suis pas le meilleur dresseur
while (bestPokemonTrainer != me):
    # Capturer plus de pokemons
    captureMorePokemon()
```

Autre exemple :

```python
# Défini continuer comme variable globale avec pour valeur "oui"
continuer = "oui"

# Tant que ‘continue’ est strictement égal à ‘oui’
while(continuer == "oui"):
    # Demande à l’utilisateur s’il souhaite continuer à exécuter la boucle et 
    # stocke le résultat dans la variable ‘continuer’
    continuer = input("Écrit ‘oui’ si tu est persévérant\n")

# Imprime un message d’encouragement si l’utilisateur provoque la fin de la boucle    
print("noob")
```
> Ce programme demandera à l’utilisateur constamment s’il est persévérant jusqu’à ce que celui-ci craque et écrive autre chose que ‘oui’

Les dictionnaires
---------------

Les dictionnaires sont un peu comme les listes sauf que chaque *élément* possède une clé et une valeur. C’est donc via leur clé que nous pourrons accéder à leur valeur. De plus ils n’ont pas d’ordres particulier (une boucle `for` affichera par exemple la 3ème clé avant la 2ème).    

Cela permet par exemple de donner un nom à un chemin de fichier, et de récupérer ceux-ci grâce à leur nom. 


```python
imgDict = {
    "perso": "img/perso.png",
    "mur": "img/mur.png",
    "sol": "img/solVersion3.png",
}

# Récupérer le chemin de l'image du personnage :
print(imgDict["perso"])
```
> imgs/perso.png

On peut parcourir un dictionnaire et imprimer ses clés avec une boucle `for` :

```python
# on utilise la méthode keys() pour récupérer les clé
for nom_image in imgDict.keys():
    print(nom_image)
```
> mur  
> perso  
> sol

Pour le faire avec les valeurs on fait :

```python
# on utilise la méthode values() pour récupérer les valeurs
for chemin_image in imgDict.values():
    print(chemin_image)
```
> img/solVersion3.png  
> img/mur.png  
> img/perso.png 

Et pour récupérer à la fois les clés et les valeurs, c’est ainsi :

```python
# on utilise la méthode items() pour récupérer les clés et les valeurs
for nom_image, chemin_image in imgDict.items():
    print(nom_image + " se trouve dans " + chemin_image)
```
> perso se trouve dans img/perso.png  
> sol se trouve dans img/solVersion3.png  
> mur se trouve dans img/mur.png


Ouvrir et lire un fichier
---------------

Il est commun de vouloir ouvrir un fichier pour lire ou écrire de l'information qui est ou sera stockée en dehors du programme. La syntaxe suivante permet d'ouvrir le fichier et de le refermer automatiquement une fois que l'on a réalisé les opérations souhaitées :

```python
# Ouvre le fichier en mode lecture seule (r pour read) et le stocke 
# dans la variable monFichier (on nomme la variable comme on veut)
with open("nomDuFichier", r) as monFichier :
    # Opérations sur le fichier
``` 

Le contenu du fichier est alors accessible via `monFichier.readlines()`

```python
# Déclare une liste vide
contenu = [ ]

with open("nomDuFichier", r) as monFichier:
    
    # On récupère le contenu du fichier avec readlines()
    contenu = monFichier.readlines()
    
print(contenu)
``` 
























