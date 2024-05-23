# Feuille d'Exercices : La Récursivité en Python

## Exercice 1 : Factorielle d'un nombre
Écrivez une fonction récursive `factorielle(n)` qui prend un nombre entier `n` et renvoie sa factorielle. Testez la fonction avec différentes valeurs de `n`.

<details>
  <summary>Solution</summary>
  
  ```python
  def factorielle(n):
      if n == 0:
          return 1
      else:
          return n * factorielle(n - 1)

  # Tests de la fonction
  print(factorielle(5))  # Affiche : 120
  print(factorielle(3))  # Affiche : 6
  print(factorielle(0))  # Affiche : 1
  ```
</details>

## Exercice 2 : Somme des chiffres d'un nombre
Écrivez une fonction récursive `somme_chiffres(n)` qui prend un nombre entier `n` et renvoie la somme de ses chiffres. Testez la fonction avec différentes valeurs de `n`.

<details>
  <summary>Solution</summary>
  
  ```python
  def somme_chiffres(n):
      if n == 0:
          return 0
      else:
          return n % 10 + somme_chiffres(n // 10)

  # Tests de la fonction
  print(somme_chiffres(123))  # Affiche : 6 (1 + 2 + 3)
  print(somme_chiffres(456))  # Affiche : 15 (4 + 5 + 6)
  print(somme_chiffres(0))    # Affiche : 0
  ```
</details>

## Exercice 3 : Nombre de Fibonacci
Écrivez une fonction récursive `fibonacci(n)` qui prend un nombre entier `n` et renvoie le n-ième nombre de Fibonacci. Testez la fonction avec différentes valeurs de `n`.

La suite de Fibonacci est une séquence de nombres dans laquelle chaque nombre est la somme des deux nombres précédents. Elle commence généralement par 0 et 1. Donc, la séquence commence comme suit : 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

<details>
  <summary>Solution</summary>
  
  ```python
  def fibonacci(n):
      if n <= 0:
          return 0
      elif n == 1:
          return 1
      else:
          return fibonacci(n - 1) + fibonacci(n - 2)

  # Tests de la fonction
  print(fibonacci(5))  # Affiche : 5
  print(fibonacci(10)) # Affiche : 55
  print(fibonacci(0))  # Affiche : 0
  ```
</details>

## Exercice 4 : Puissance d'un nombre
Écrivez une fonction récursive `puissance(base, exposant)` qui prend deux nombres entiers `base` et `exposant` et renvoie `base` élevé à la puissance `exposant`. Testez la fonction avec différentes valeurs de `base` et `exposant`.

<details>
  <summary>Solution</summary>
  
  ```python
  def puissance(base, exposant):
      if exposant == 0:
          return 1
      else:
          return base * puissance(base, exposant - 1)

  # Tests de la fonction
  print(puissance(2, 3))  # Affiche : 8 (2^3)
  print(puissance(5, 2))  # Affiche : 25 (5^2)
  print(puissance(7, 0))  # Affiche : 1  (7^0)
  ```
</details>

## Exercice 5 : Inversion d'une chaîne
Écrivez une fonction récursive `inversion(chaine)` qui prend une chaîne de caractères `chaine` et renvoie la chaîne inversée. Testez la fonction avec différentes chaînes.

<details>
  <summary>Solution</summary>
  
  ```python
  def inversion(chaine):
      if len(chaine) == 0:
          return chaine
      else:
          return chaine[-1] + inversion(chaine[:-1])

  # Tests de la fonction
  print(inversion("python"))  # Affiche : "nohtyp"
  print(inversion("recursion"))  # Affiche : "noisrucer"
  print(inversion(""))  # Affiche : ""
  ```
</details>

[Cours Précédent](../Cours/12_La%20récursivité.md) | 
[Cours Suivant](../Cours/13_Les%20classes.md)
