# Mémo sur les fonctions de Pygame

De manière générale nous utilisons des méthodes de la bibliothèque Pygame en écrivant `pygame.fonction`.

---

### Importer la bibliothèque Pygame

```python
import pygame
```
Importe tous les modules de `pygame`.  
On pourra ainsi utiliser toutes les classes et fonctions de la bibliothèque Pygame.

### Initialiser Pygame

```python
pygame.init()
```
Initialise tous les modules de la bibliothèque Pygame nécessaires.

### Définir une fenêtre

```python
ecran = pygame.display.set_mode((largeur,hauteur))
```
Défini le mode d’affichage et créé une fenêtre avec une largeur et une hauteur donnée. Cette méthode retourne une surface correspondante à ce qui est affichée dans la fenêtre. Dans cet exemple, celle-ci est stockée dans une variable nommée `ecran`.

### Définir un titre

```python
pygame.display.set_caption(‘le nom de la fenetre’)
```
Affiche une chaîne de caractères dans le titre de la fenêtre.

### Charger une image dans la mémoire

```python
image = pygame.image.load("nom_image.png").convert_alpha()
```
Charge une image (`image.load("nom_image.png")`) dans la mémoire et lui demande de la considérer comme une image avec fond transparent (méthode `convert_alpha()`).  
Stocke cette image dans la variable `image` que nous pourront utiliser par la suite.

### Ajouter une image à la surface d’affichage

```python
ecran.blit(image, (x,y))
```
A la base, un `blit` signifie coller une surface sur une autre, à une position donnée `(x,y)`. Ainsi, on change la couleur de certains pixels de la surface `ecran` par l’ajout de notre image.


### Afficher les images blitées dans la fenêtre

```python
pygame.display.update()
```

`display.update()` dessine sur la fenêtre du jeu tout ce que nous avons blité sur la surface.

### Écouter les événement et faire des actions
```python
listeEvenements = pygame.event.get()
for evenement in listeEvenements :
    if evenement.type == QUIT:
        pygame.quit()
        sys.exit()
```

La methode `event.get()` permet d'obtenir la liste des événements (appui sur une touche du clavier, muvement de la souris, ...) qui ont eu lieu depuis le dernier rafraichissement.

Grâce à une boucle `for`, on analyse chacun des événements qui ont eu lieu, afin d’exécuter des instructions pour certains d'entre eux.
Dans cet exemple, on lui demande de vérifier si l’utilisateur demande à fermer la fenêtre (évenement de type `QUIT`). Si c’est le cas, alors nous arrêtons le processus pygame pour libérer la mémoire vive utilisée, et nous mettons fin à l'éxécution du programme.

##### Les 3 `event.type` à retenir sont :

* `QUIT`
* `MOUSEMOTION` (événements de souris)
* `KEYDOWN` (événement de clavier)


##### `MOUSEMOTION`

```python
if event.type == MOUSEMOTION:
    # Change la position de l'image en stockant dans les variables
    # la position de la souris récupérée par event.pos x et y
    image_x = event.pos[0]
    image_y = event.pos[1]
```

`event.pos` récupère la position de la souris en pixel de la fenêtre. On accède à `x` avec l’index `0` et `y` avec l’index `1`.


##### `KEYDOWN`

```python
if event.type == KEYDOWN:
    # Change la position de l'image en modifiant la valeur des
    # variables de position de l’image suivant la touche enfoncée
    if event.key == pygame.K_RIGHT:
        image_x = image_x + 32
    if event.key == pygame.K_LEFT:
        image_x = image_x - 32
    if event.key == pygame.K_UP:
        image_y = image_y - 32
    if event.key == pygame.K_DOWN:
        image_y = image_y + 32
```
On compare ici `event.key` à des mots-clés renvoyant aux touches du clavier.  
Pour une liste détaillée des différents mot-clés vous pouvez aller voir la [documentation de pygame](http://www.pygame.org/docs/ref/key.html)
