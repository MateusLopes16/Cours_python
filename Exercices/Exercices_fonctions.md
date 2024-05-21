# Feuille d'Exercices : Les Fonctions en Python

## Exercice 1 : Fonction de salutation
Écrivez une fonction `salut(nom)` qui prend un seul paramètre, `nom`, et affiche "Bonjour, `nom`!".

<details>
  <summary>Solution</summary>
  
  ```python
def salut(nom):
    print(f"Bonjour, {nom}!")

# Test de la fonction
salut("Alice")  # Affiche : Bonjour, Alice!
salut("Bob")    # Affiche : Bonjour, Bob!
```
</details>

## Exercice 2 : Fonction de multiplication
Écrivez une fonction `multiplie(x, y)` qui prend deux nombres `x` et `y` comme paramètres et renvoie le produit des deux nombres.

<details>
  <summary>Solution</summary>
  
  ```python
def multiplie(x, y):
    return x * y

# Test de la fonction
resultat = multiplie(5, 3)
print(resultat)  # Affiche : 15
```
</details>

## Exercice 3 : Fonction de calcul de la somme des carrés
Écrivez une fonction `sommeDesCarres(a, b)` qui prend deux nombres `a` et `b` et renvoie la somme de leurs carrés.

<details>
  <summary>Solution</summary>
  
  ```python
def sommeDesCarres(a, b):
    return a**2 + b**2

# Test de la fonction
resultat = sommeDesCarres(3, 4)
print(resultat)  # Affiche : 25

```
</details>

## Exercice 4 : Fonction de recherche du maximum
Écrivez une fonction `maxDeuxNombres(a, b)` qui prend deux nombres `a` et `b` et renvoie le plus grand des deux.

<details>
  <summary>Solution</summary>
  
  ```python
def maxDeuxNombres(a, b):
    if a > b:
        return a
    else:
        return b

# Test de la fonction
print(maxDeuxNombres(3, 7))  # Affiche : 7
print(maxDeuxNombres(10, 5)) # Affiche : 10
```
</details>

## Exercice 5 : 
Écrivez une fonction `estPossible(a, b)` qui prend deux nombres `a` et `b` et renvoie si la division euclidienne est possible sans reste.

<details>
  <summary>Solution</summary>
  
  ```python
def estPossible(a, b):
    if b == 0:
        return False
    return a % b == 0 # On renvoie une codition, donc si elle est vraie on renvoir True sinon False

# Test de la fonction
print(estPossible(10, 2))  # Affiche : True
print(estPossible(10, 3))  # Affiche : False
print(estPossible(10, 0))  # Affiche : False
```
</details>

