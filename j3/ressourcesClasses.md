# Mémo sur les classes en Python

## Vocabulaire

Les _classes_ peuvent être vues comme des structures comprenant :

- des **variables** propre à cette classe (nommées **attributs**) décrivant l’état d’un objet ;
- des **fonctions** propre à cette classe (nommées **méthodes**) décrivant le comportement (les différentes actions que l’on peut réaliser) d’un objet.

On appelle **classe** la _description générale_ des attributs et des méthodes. C’est une sorte de super recette qui permet de créer des **objets** complexes ayant des états et des comportements.

Ces **objets** sont donc des _instances_ de cette classe, c’est-à-dire un exemplaire créé à partir de la recette (modèle). On peut faire la différence entre classe et instance de classe en comparant « pièces » (la recette) et « chambre » (un exemple précis de pièce).

> Une pièce à des murs d’une certaine couleur, il y a une série de meubles dedans, elle à des portes qui mène à d’autres pièces, ... La chambre à des murs brun, il y a un lit, une armoire et une table de chevet, une porte mène au couloir et une seconde mène à la salle de bain, ...

## Déclaration d’une classe

```python
class Monstre() :
    # "Constructeur" - le machin qui initialise un objet
    def __init__(self, type):

        self.type = type

        if (type == "Troll"):
            self.hp = 50
            self.force = 6
        elif (type == "Gobelin"):
            self.hp = 10
            self.force = 2
        else: print("Type de monstre inconnu !")

    def attaquer(self, cible):

        cible.hp -= self.force
```
On défini une classe avec `class Monstre():` (par convention, on nomme la classe en commençant par une majuscule).
On défini à l’intérieur la classe notre première méthode (fonction propre à cette classe). Cette méthode `__init__` est un peu particulière, on l’appelle le **constructeur**, c’est la méthode qui sera automatiquement exécutée à l’instanciation de la classe (lorsque l’on va créer un objet à partir de cette classe), c’est une initialisation. On y définit les attributs (variables propres à cette classe) que doit avoir notre futur objet lors de sa création.
C’est aussi dans ce constructeur que l’on passe les arguments qui seront donnés à la création d’un objet, et non pas entre les parenthèses de la définition de la classe.

### Qu'est-ce que `self` ?

On peut se dire que `self` est un mot-clé qui, à la création d’un objet,  sera remplacé par le nom que l’on donnera à un objet nouvellement créé. `self` est l’objet en lui-même.

## Utilisation des classes et des objets

### Créer un objet à partir d'une classe

À l’instar des fonctions, une classe ne s’exécute pas d’elle-même. Il faut assigner une variable à un appel de classe (instanciation) pour créer un objet, la classe renverra alors un objet qui sera stocké dans la variable que l’on pourra manipuler.

```python
# Créer un troll
super_troll = Monstre("Troll")
```

On créé un exemplaire de Monstre nommé `super_troll`. Ce monstre sera de type `Troll` (donné en paramètre). Le paramètre est pris en compte par la méthode `\_\_init\_\_`. Les attributs (`hp` et `force`) sont initialisé en conséquence

### Créer plusieurs objets à partir d’une même classe

En utilisant la syntaxe précédente, il est tout à fait possible de créér plusieurs objets, en utilisant une boucle for par exemple :

```python
# Préparer une armée de gobelin
# On crée ici 4 monstre de type Gobelin (10 hp, 2 force)
armee_gobelins = []
for i in range(4) :
    gobelin = Monstre("Gobelin")
    armee_gobelins.append(gobelin)
```

### Accéder aux attributs d'un objet

On peut accéder aux attributs de l’instance `super_troll` en utilisant `super_troll.attribut` (ici, `hp`).

```python
print("Super Troll a " + str(super_troll.hp) + " hp !")
```
> Super Troll a 50 hp !

### Utiliser les méthodes d'un objet

```python
# le troll attaque le 3ème gobelin de l’armée
super_troll.attaquer(armee_gobelins[2])
# chaque gobelins attaque le troll
for gobelin in armee_gobelins :
    gobelin.attaquer(super_troll)
```

On utilise ici la méthode `attaquer()` de la classe `Monstre()`. Les trolls et les gobelins peuvent tous deux utiliser cette méthode car ils sont tous deux des instances de la classe `Monstre()`. Seuls leur `type` et donc leurs attributs `hp` et `force` diffèrent.

De la même manière qu’on accède aux attributs d’un objet avec `nom_objet.attribut` on exécute une méthode en utilisant `nom_objet.methode()`.

```python
# [...]
    def attaquer(self, cible):

        cible.hp -= self.force
```

Le troll attaque le 3ème gobelin grâce à l'instruction `super_troll.attaquer(armee_gobelins[2])`. L'interprétation de cette instruciton est totalement similaire à l'éxécution d'une fonction : le programme rentre dans la méthode `attaquer(self, cible)`, où `self` correspond à `super_troll`, et `cible` correspond au troisième gobelin.

Dans notre cas, on soustrait à `cible.hp` (les points de vie du troisième gobelin) la valeur `self.force` (la force du troll, 6).

Puis, chacun leur tour, les gobelins attaque le troll et soustrait aux hp du troll (50) la valeur de la force des gobelins (2 * 4).

```python
print("Une bataille à lieu !")
print("Super Troll n’a plus que " + str(super_troll.hp) + " hp !")
print("Le 3ème gobelin a désormais " + str(armee_gobelins[2].hp) + " hp !")
```
> Super Troll a 50 hp !  
> Une bataille à lieu !  
> Super Troll n’a plus que 42 hp !  
> Le 3ème gobelin a désormais 4 hp !  
