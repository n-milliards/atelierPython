Initiation à la programmation et réalisation d'un jeu vidéo en Python
---------------------------------------------------------------------

### **Atelier 2**



![Welcome back !](http://previews.123rf.com/images/gajus/gajus1406/gajus140600022/28879813-Old-rustic-signpost-with-the-phrase-Welcome-back-outdoors-in-sunny-woodland-with-a-faded-vintage-or--Stock-Photo.jpg)



* **des variables**, qui sont des cases mémoires pour stocker des informations
```
toto = 3.14
```
* **des fonctions**, qui sont des listes d'instructions avec un nom
```
def demanderUnNom(message) :
    return input(message)
```
* **des conditions**, pour executer des instructions selon les situations
```
if (nom == "Alex") :
    print("Oh, je ne savais pas que c'était toi !")
```
* **des listes**, pour stocker des séries d'information ensemble
```
bonLegumes = [ "patates", "tomates", "poivrons" ]
```
* **des boucles**, pour répéter des actions sur différents éléments ou en fonction d'une condition
```
for legume in bonLegumes :
    print("Les "+legume+" c'est bon !")
```



Aujourd'hui
-----------

![Moar code](http://image.slidesharecdn.com/dazzing-data-depiction-with-d3js-141109083710-conversion-gate02/95/dazzing-data-depiction-with-d3js-15-638.jpg)



Aujourd'hui
-----------

![](https://upload.wikimedia.org/wikipedia/en/b/be/SSBB_Gameplay.jpg)



Aujourd'hui
-----------

**Débuts avec Pygame**

* Ouvrir une fenêtre
* Afficher des trucs

**Encore du blabla**

* Les dictionnaires
* Les classes

**Le fun** (espérons :P)

* Elements de game building / design
* Principe du jeu que vous allez écrire
* Étapes de construction
* À vous !



Encore du blabla
----------------



Introduction à Pygame
=====================



Les librairies
--------------

Un ensemble de fonctions déjà pensées, écrites et packagées, qui servent un but particulier. Dans le cas de Pygame : écrire des jeux vidéos.

On importe les fonctions en utilisant :
```python
import someLibrary
```



Ce que permet Pygame
-------------------

* Afficher une fenêtre
* Dessiner des formes (lignes, rectangles, ...)
* Importer et afficher des images à des positions données
* Détecter les touches de clavier
* Détecter des collisions entre des objets
* ...



Premier programme avec Pygame
-----------------------------

```python
import pygame, sys
from pygame.locals import *

# Initialiser pygame
pygame.init()

# Initialiser une fenêtre / l’écran de jeu
ecran = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Mon jeu!')

# Boucle principale
while True:

    # Verifier si il y a des événement en attente
    for event in pygame.event.get():

        # Si l'utilisateur a déclenché la fermeture de la fenêtre
        if event.type == QUIT:
            # Désinitialiser pygame
            pygame.quit()
            # Sortir du programme
            sys.exit()
```



Changer la couleur de fond
--------------------------

En utilisant :
```python
    couleur = (0,0,255)
    ecran.fill(couleur)
```

Modification du programme :

```python
# [...]

# Boucle principale
while True:

    # Remplir l'écran avec une couleur
    ecran.fill((0,0,255))

    for event in pygame.event.get():
        # [...]
    
    # Rafraîchir l'écran
    pygame.display.update()
```



Les surfaces
------------

#### Charger une image
```python
monImage = pygame.image.load("chaton.png").convert_alpha()
```

#### **Blitter** : Coller une surface sur une auret
```python
surfaceDArrivee.blit(surface, (x,y))
```



Charger et utiliser des images
------------------------------

```python
# Charger des images
fond = pygame.image.load("fond.png").convert()
image = pygame.image.load("image.png").convert_alpha()

# Boucle principale
while True:

    for event ...
    #[...]

    # Coller l'image de fond
    ecran.blit(fond, (0,0))

    # Coller l'autre image
    ecran.blit(image, (50,50))

    # [...]
```



Les événements
--------------

Des événements sont générés en fonction des appuis des touches et des mouvements / clics de la souris.

Par exemple, appuyer sur une touche génère un événement `KEYDOWN`.




Déplacer une image avec le clavier
---------------------------------

```python
# [...]

# Définir la position initiale de l'image
image_x = 20
image_y = 20

# Boucle principale
while True:

    # Verifier si il y a des événement en attente
    for event in pygame.event.get():

        if event.type == QUIT:
            # [...]

        # Si l'utilisateur appuie sur une touche
        if event.type == KEYDOWN:
            # S’il appuie sur la touche gauche
            if event.key == K_LEFT :
                # Décrémente la valeur de de image_x
                image_x -= 10
            if event.key == K_RIGHT :
                image_x += 10
            if event.key == K_UP :
                image_y -= 10
            if event.key == K_DOWN :
                image_y += 10
    
    # [...]

    # Dessiner l'image à une certaine position
    # (qui change suivant la position de la souris)
    ecran.blit(image, (image_x,image_y))
```



Les dictionnaires
-----------------

Permet de stocker de l'information, indexées par des noms

Exemple : 
```python
age = {
   "alice"   : 20, 
   "bob"     : 18,
   "charlie" : 23
}

print(age["charlie"])
```

Autre exemple :
```python
regions = {
   "grand-est" : [ 08, 10, 51, 52, 54, 55, 57, 67, 68, 88 ],
   "bretagne"  : [ 22, 29, 35, 56 ]
}
```



Les dictionnaires
-----------------

```
age = {
   "alice"   : 20, 
   "bob"     : 18,
   "charlie" : 23
}

print(age)

print("L'age de Charlie est : " + str(age["charlie"]))

# Changer une valeur dans un dictionnaire :
age["bob"] = 19

# Ajouter une entrée dans un dictionnaire :
age["dianne"] = 32

print(age)

```


Les classes
-----------



Les classes : principe
-----------

Les classes peuvent être vues comme des structures comprenant :
- des **variables** (nommées **attributs**) décrivant l'état d'un objet
- des **fonctions** (nommées **méthodes**) décrivant le comportement d'un objet et les
  possibilités d'interaction avec lui



Les classes : exemple
-----------

![](assets/classe.png)



Les classes : vocabulaire
-----------

On apelle **classe** la "description générale" des attributs et des méthodes,
et **objets** des instances de cette classe.

Il s'agit de la même différences qu'entre « les voitures » (en général) et « ma voiture » (en particulier).



Les classes : syntaxe
-----------

Déclaration

```python
class Voiture() :

    def __init__(self, marque, couleur) :
        self.marque   = marque
        self.couleur  = couleur
        self.compteur = 0
    
    def rouler(distance) :

        self.compteur += distance
```

Utilisation

```
maVoiture = Voiture("citroen", "rouge")
maVoiture.rouler(30)
maVoiture.rouler(150)

print("Ma voiture est une "+maVoiture.marque+" "+maVoiture.couleur)
print("Elle a roulé"+maVoiture.compteur+"km.")
```



Les classes : syntaxe
-----------

Déclaration

```python
class Coffre() :

    def __init__(self, contenu) :

        self.contenu = contenu
        self.etat    = "verouille"

    def deverouiller(self, cle) :

        if (cle == "cle rouge") :
            self.etat = "ferme"
        else :
            print("Ce n'est pas la bonne cle !")
```

Utilisation

```
monCoffre = Coffre("Une super epee")

print("Mon coffre contient : " + monCoffre.contenu)
print("Mon coffre est : "      + monCoffre.etat)

monCoffre.deverouiller("cle verte")
```



Construction d'un jeu tile-based
================================



Elements de game building / design
----------------------------------

* **Afficher des choses** (écran, images, animations, texte)
* **Gérer les entrées** (clavier, souris, ...)
* Jouer des sons, de la musique
* **Penser l'architecture logicielle du jeu** (structures de données)
* **Penser la mécanique du jeu** (gameplay)
* Penser l'univers du jeu


Ref : http://lanyrd.com/2012/pycon/spbxc/



Jeux tile-based
---------------

![](http://www.emanueleferonato.com/wp-content/uploads/2010/05/rebuildc2.jpg)
![](https://www.pokebip.com/pages/jeuxvideo/rbvj/soluce_rb/screen_ig/screen047.png)



Format de la map
----------------

![](assets/textToMap.png)



Sprites
-------

![](assets/spriteExample.png)



Les grandes étapes
------------------

### Le héros

1. Charger le sprite en mémoire
2. Afficher le héros sur l'écran
3. Ajouter une méthode `look` pour faire regarder le héros à
   droite/gauche/haut/bas
4. Ajouter une méthode `move` qui déplace le héros d'une case
5. Mapper les touches du clavier sur `look` et `move`

### La map

1. Lire le fichier ascii de la map vers une liste
2. Afficher la map

### Les collisions

1. Vérifier dans `move` si la case de destination est libre