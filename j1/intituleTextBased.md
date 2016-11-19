# Construction d'un jeu vidéo text-based

Dans le jeu em mode texte que nous proposons de réaliser, le personnage vit dans
un appartement contrôlé par une intelligence artificielle qui fait attention à
tous vos faits et gestes. Cette entité infernale le réveille chaque matin
et l'empêche de sortir de chez lui s’il n’a pas mangé, ne s’est pas lavé ni habillé ou s’il n’est pas complètement réveillé !
Réussira-t-il à s'extraire de son appartement ?

#### 1. Menu de navigation entre les pièces

Nous commençons par réaliser un menu permettant de naviguer entre les différentes
pièces d'une maison. Il peut ressembler à ceci :

```
--> Vous êtes dans la chambre.

‘Où aller ?’
1 > Cuisine
2 > Salle de bain

Sélection : 2

--> Vous êtes maintenant dans salle de bain.
```

##### 1-1

Ajouter une clé `"piece actuelle"` au dictionnaire du personnage, qui corresponds à la
pièce dans laquelle il se situe. Définir une fonction `afficher_pieces()` qui
affiche où se situe actuellement le personnage, et dans un deuxième temps la
liste des pièces où il peut aller (ne pas afficher la pièce dans laquelle le personnage se trouve). Tester cette fonction.

> **Éléments utiles**  
> -> Itérer sur une liste  
> -> Opérateur !=

##### 1-2

Adapter la fonction précédente pour afficher l'indice des pièces devant leur
nom, séparé par un symbole comme '>'. Tester cette fonction.

> **Éléments utiles**  
> -> enumerate()  
> -> str()

##### 1-3

Ajouter une fonction `changer_piece()` qui propose au joueur de changer de pièce
en l’invitant à taper un numéro de pièce. Lui afficher soit le changement de
pièce, soit un message d'erreur lorsqu’il rentre un numéro plus grand que le
nombre d'éléments dans la liste `piece`. Tester cette fonction.

> **Éléments utiles**  
> -> int()


#### 2. Boucle principale du jeu, condition de victoire

Ajoutez une pièce "Dehors" à la liste des pièces.

Programmez une boucle qui affiche sans cesse la liste des pièces et propose de
changer de pièce tant que le joueur ne décide pas d'aller dehors. Vous pouvez
aussi afficher un petit message de fin.


#### 3. Menu d’action propre à chaque pièce

Nous voulons maintenant pouvoir effectuer des actions dans les différentes pièces,
telles que manger, prendre une douche, s'habiller, retourner se coucher, etc...
qui affecterons l'état du personnage (par exemple, manger a pour incidence que
le personnage n'est plus affamé !)

Actions pour la chambre : S'habiller, Retourner se coucher
Actions pour la salle de bain : Prendre une douche, Se laver les dents
Actions pour la cuisine : Manger un truc, Boire un café

(Vous pouvez aussi imaginer d'autres pièces et actions possibles vous-même !)

##### 3-1

Définir un dictionnaire `actions` ayant pour clés le nom de chaque pièces, et
pour valeurs les listes d'actions possibles dans chaque pièce. Programmer une
fonction `determiner_actions_possibles()` qui retournera la liste des actions
possibles dans la pièce actuelle. Tester que cette fonction renvoie le résultat
souhaitée.

##### 3-2

Faire en sorte que `determiner_actions_possibles()` retourne aussi une action
particulière `Changer de pièce` quelque soit la pièce actuelle.

> **Éléments utiles**  
> -> Méthode append() sur les listes

##### 3-3

Programmer une nouvelle fonction `demander_action()` qui imprime à
l’écran les actions possibles (et leurs indices) à la manière de `afficher_pieces()`.

##### 3-4

Compléter cette fonction par une invitation à entrer un numéro pour sélectionner
une action à la manière de `changer_piece`. Vérifiez si le nombre entré est un
numéro d'action valide, et afficher une erreur si ce n'est pas le cas.

#### 4. Programmation des actions possibles

##### 4-1

Programmer une fonction `faire()` qui prend en argument une `action`. Écrivez
toute une série de conditions qui modifieront l'état du personnage en fonction
de l'action demandée. Par exemple, si `action` vaut "manger", cela devra modifier
perso[« affamé"].

> **Éléments utiles**  
> -> elif

##### 4-2

Ajouter un appel à `faire()` à la fin de `demander_action()`


#### 5. Ajouter un peu de storytelling à notre jeu text-based

##### 5-1

Programmer une fonction `afficher_etat()` qui indiquera au joueur s’il est ou
n’est pas habillé, si il a faim, etc...  Ajoutez une action de base à
`actions_possibles` du type "Lancer l’application ManageYourself".  Ajoutez une
condition qui appelle la fonction `afficher_etat()` dans la fonction `faire()`.

##### 5-2

Programmer une fonction `conditions_pour_sortir()` qui renvoie True ou False si
le personnage est prêt pour sortir (du point de vue de l’IA !) (e.g. le perso doit
être propre, habillé, avoir mangé, ...). Cette fonction peut aussi afficher des
messages personnalisé afin d’aider le joueur à savoir quoi faire s’il tente de
sortir avant d’avoir rempli toutes les conditions.

##### 5-3

Utiliser la fonction `conditions_pour_sortir()` depuis `changer_piece()` pour
autoriser ou non le personnage à aller `Dehors` lorsqu'il le demande.
