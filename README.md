# PYTHON

## Les types simples

En Python, on a différentes entités appelées variables qui vont déterminer des valeurs associées à un nom. Il en existe différents types :

- **Une variable de type `int`** est un nombre réel, donc tout nombre positif ou négatif mais entier.
- **Une variable de type `float`** est un nombre réel positif ou négatif à virgule flottante, stocké sur un certain nombre de bits.
- **Une variable de type `str`** est une chaîne de caractères.
- **Une variable de type `bool`** est une valeur vraie ou fausse.

Ces quatre types représentent les types communs, appelés types primitifs.

## Déclarer des variables

Pour déclarer des variables en Python, nous n'avons pas besoin d’inclure le type de la variable. Il suffit de faire :

```python
ma_chaine = "premiere chaine"
mon_entier = 35
mon_numerique = 35.0 
mon_booleen = False
```

Si nous appelons les variables plus tard dans le fichier, elles contiendront toujours la même valeur à moins de la changer :

```python
print(ma_chaine)  # premiere chaine
ma_chaine = "autre chaine"
print(ma_chaine)  # autre chaine
```

### Remarques :

- Ne pas oublier les guillemets pour déclarer une chaîne.
- Ne pas mettre d'espace dans le nom des variables.
- Les booléens peuvent avoir comme valeur True, False ou 1 et 0.
- 35.0 et 35. sont le même nombre
- On peut décider de suivre des normes de langage comme le camel case :
- Pour commenter du code en Python, on utilise le symbole #. Tout ce qui suit ce caractère sur la même ligne sera inactif lors de l'exécution du code

- La règle dit que chaque première lettre d'un mot doit être en majuscule sauf pour le premier mot.
Dans notre cas, les variables devraient être renommées ainsi :

```python 
maChaine = "premiere chaine"
monEntier = 35
monNumerique = 35.0
monBooleen = False
```

## Conditions

Cette notion est l’une des plus importantes en programmation. Elle permet de diriger le programme vers une direction en fonction d’une certaine valeur ou plus simplement :

**SI cela ALORS ceci SINON cela**

Les mots clées utilisées pour définir cette action son **IF** et **ELSE**

Exemple :

```python
x = 10

if x > 0:
    print("x est positif")
else:
    print("x est négatif")
```

On peut aussi ajouter des conditions supplémentaires avec **ELIF** (sinon si) :

Exemple :

```python
note = 85

if note >= 90:
    print("Excellent")
elif note >= 80:
    print("Très bien")
elif note >= 70:
    print("Bien")
else:
    print("Peut mieux faire")

```

### Remarques :

- **else** n'est pas obligatoire dans toutes les conditions s'il n'est pas nécessaire.
- Pour vérifier une égalité entre deux variables, on utilise l'opérateur **==**

```python
x = 10

if x == 10:
    print("x est 10")
```

- Il est important de placer les **:** après la condition car c'est la syntaxe qui remplace **alors**.
- La tabulation, appelée indentation, est aussi à respecter car il n'y a pas de balise de fin de condition :

```python
x = 10

if x == 10:
    print("x est 10") # dans la condition, executer seulement si x = 10
print("x est 10") # hors de la condition, executer a chaque fois
```

## Portes logiques

On peut pousser plus loin les conditions en y intégrant tout ce qui est opérations logiques. Les opérations logiques sont des opérations entre deux booléens à la fois. Il existe trois opérations logiques principales :

- **Et** : Les deux valeurs sont vraies.

| a    | b    | Résultat |
|------|------|----------|
| Vrai | Vrai | **Vrai**     |
| Vrai | Faux | **Faux**     |
| Faux | Vrai | **Faux**     |
| Faux | Faux | **Faux**     |

- **Ou** : Au moins l'une des valeurs est vraie.

| a    | b    | Résultat |
|------|------|----------|
| Vrai | Vrai | **Vrai**     |
| Vrai | Faux | **Vrai**     |
| Faux | Vrai | **Vrai**     |
| Faux | Faux | **Faux**     |

- **Ou exclusif** : Une seule des valeurs est vraie, mais pas les deux.

| a    | b    | Résultat |
|------|------|----------|
| Vrai | Vrai | **Faux**     |
| Vrai | Faux | **Vrai**     |
| Faux | Vrai | **Vrai**     |
| Faux | Faux | **Faux**     |

Ils sont représentés par `and`, `or` et `xor` en Python.

Exemple :

```python
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(a ^ b)    # True (XOR)
```

Comme dit précédemment, on peut intégrer les opérations logiques dans nos conditions.

```python
x = True 
y = False
z = True

if x and y:
    print("x and y") # ne va pas s'executer car x est vrai mais pas y
elif x and z:
    print("x and z") # va s'executer car les deux valeurs sont vraies
else:
    print("x") # ne va pas s'executer car on a rempli une condition précédente

a = False

if a or y:
    print("a or y") # ne va pas s'executer car les deux valeurs sont fausses
elif x or a:
    print("x or z") # va s'executer car x est vrai
else:
    print("x") # ne va pas s'executer car on a rempli une condition précédente
```

## Les Fonctions  

Chaque bloc de code peut être séparé en fonctions. Une fonction est un bloc de code réutilisable qui remplit une tâche précise.

On initialise une fonction grâce au mot-clé `def`, suivi du nom de la fonction entre parenthèses, et enfin deux points :

```python
def affiche():
    print("Dans la fonction affiche")
```

### Paramètres des fonctions

Les fonctions peuvent contenir ou non ce qu'on appelle des paramètres, ce sont des valeurs que l'on transmet du code principal vers la fonction.

Ces paramètres sont déclarés dans les parenthèses de la fonction.

Une fonction a besoin d'être appelée pour être utilisée :

```python
premier_message = "Je suis le message"

def affiche(message):
    print(message)  # Affiche le message 'Je suis le message'

x = 10
y = 10

def multiplie(x, y):
    print(x * y)  # Affiche 100

affiche(premier_message)
```

### Remarques : 

- Il est important de déclarer la fonction avant de l'appeler.
- Une fonction n'a pas accès aux déclarations de variables du fichier.

```python
message = "je suis le message"

def affiche():
    print(message) # provoque une erreur car message n'est pas défini dans la fonction
```

## Les Fonctions natives

Tous les langages de programmation comportent des fonctions natives plus-ou-moins communes, des fonctions comme :

- `print` : pour afficher une chaîne de caractères.
- `len` : pour obtenir la longueur d'une séquence (comme une chaîne de caractères, etc.).
- ...

Dans Python, ces fonctions sont intégrées dans le langage et peuvent être utilisées sans avoir besoin de les définir.

Toutes les fonctions sont répertoriées dans la documentation officielle accessible via https://docs.python.org/fr/3/library/functions.html

## L'importation

Dans python il existe la notion d'importation, elle permet a ne pas avoir a réécrire les mêmes fonctions a trâvers les différents fichiers du même projet, ou a pourvoir integrer des modules, ou librairies, dans nos projets tels que le module `math` qui permet de completer le projet avec des formules mathématiques complexes comme la racine carrée.

```python
from math import sqrt # permet d'import uniquement la racine carre

print(sqrt(25))

import math # importe toute la librairie/module math

print(math.sqrt(25))

import math as m # renomme la librairie math par m

print(m.sqrt(25))

from premier_fichier import premiere_fonction # importe la fonction premiere_fonction a notre fichier
```

