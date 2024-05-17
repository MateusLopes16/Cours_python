# Conditions

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