# Feuille d'Exercices : Les Portes Logiques

## Exercice 1 : Fonction de vérification de multiples
Écrivez une fonction ``est_multiple(n)`` qui prend un seul paramètre, ``n``, et qui renvoie **True** si le nombre est un multiple de 10 ou de 3, et **False** sinon.

<details>
  <summary>Solution</summary>
  
  ```python
def est_multiple(n):
    return n % 10 == 0 or n % 3 == 0

# Tests de la fonction
print(est_multiple(30))  # Affiche : True (30 est multiple de 10 et de 3)
print(est_multiple(9))   # Affiche : True (9 est multiple de 3)
print(est_multiple(20))  # Affiche : True (20 est multiple de 10)
print(est_multiple(7))   # Affiche : False (7 n'est multiple ni de 10 ni de 3)
print(est_multiple(0))   # Affiche : True (0 est multiple de tout nombre)
```
</details>

## Exercice 2 : Fonction de vérification de multiples communs
Écrivez une fonction ``est_multiple_commun(n)`` qui prend un seul paramètre, ``n``, et qui renvoie **True** si le nombre est un multiple de 10 et de 3, et **False** sinon.

<details>
  <summary>Solution</summary>
  
  ```python
def est_multiple_commun(n):
    return n % 10 == 0 and n % 3 == 0

# Tests de la fonction
print(est_multiple_commun(30))  # Affiche : True (30 est multiple de 10 et de 3)
print(est_multiple_commun(9))   # Affiche : False (9 est multiple de 3)
print(est_multiple_commun(20))  # Affiche : False (20 est multiple de 10)
print(est_multiple_commun(7))   # Affiche : False (7 n'est multiple ni de 10 ni de 3)
print(est_multiple_commun(0))   # Affiche : True (0 est multiple de tout nombre)
```
</details>

## Exercice 3 : Vérification de multiples dans une borne
Écrivez une fonction ``est_multiple_borne(n, mini, maxi)`` qui prend trois paramètres, ``n``, ``mini`` et ``maxi``, et qui renvoie **True** si ``n`` est un multiple de 2 et est compris entre ``mini`` et ``maxi`` (inclus), et **False** sinon.

<details>
  <summary>Solution</summary>
  
  ```python
def est_multiple_borne(n, mini, maxi):
    return n % 2 == 0 and mini <= n <= maxi

# Tests de la fonction
print(est_multiple_borne(4, 1, 10))  # Affiche : True (4 est multiple de 2 et est compris entre 1 et 10)
print(est_multiple_borne(7, 1, 10))  # Affiche : False (7 n'est pas multiple de 2)
print(est_multiple_borne(12, 5, 15)) # Affiche : True (12 est multiple de 2 et est compris entre 5 et 15)
print(est_multiple_borne(20, 5, 15)) # Affiche : False (20 est multiple de 2 mais n'est pas compris entre 5 et 15)
print(est_multiple_borne(0, -5, 5))  # Affiche : True (0 est multiple de 2 et est compris entre -5 et 5)

```
</details>

## Exercice 4 : Vérification de multiples hors d'une borne
Écrivez une fonction ``est_multiple_borne_ext(n, mini, maxi)`` qui prend trois paramètres, ``n``, ``mini`` et ``maxi``, et qui renvoie **True** si ``n`` est un multiple de 2 et est inferieur a ``mini`` ou superieur a ``maxi`` (inclus), et **False** sinon.

<details>
  <summary>Solution</summary>
  
  ```python
def est_multiple_borne_ext(n, mini, maxi):
    return (n % 2 == 0) and (n < mini or n > maxi)

# Tests de la fonction
print(est_multiple_borne_ext(4, 1, 10))   # Affiche : False (4 est multiple de 2 mais compris entre 1 et 10)
print(est_multiple_borne_ext(7, 1, 10))   # Affiche : False (7 n'est pas multiple de 2)
print(est_multiple_borne_ext(12, 5, 15))  # Affiche : False (12 est multiple de 2 mais compris entre 5 et 15)
print(est_multiple_borne_ext(20, 5, 15))  # Affiche : True (20 est multiple de 2 et est supérieur à 15)
print(est_multiple_borne_ext(0, -5, 5))   # Affiche : False (0 est multiple de 2 mais compris entre -5 et 5)
print(est_multiple_borne_ext(-3, -5, 5))  # Affiche : False (-3 n'est pas multiple de 2 et est inférieur à -5)
print(est_multiple_borne_ext(25, -5, 5))  # Affiche : True (25 n'est pas multiple de 2 et est supérieur à 5)
```
</details>


[Retour au cours](../Cours/8_Portes%20logiques.md) | 
[Cours Suivant](../Cours/9_L'importation.md)