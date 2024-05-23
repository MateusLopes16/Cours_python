# Feuille d'Exercices : Les Boucles en Python

## Exercice 1 : Compter les nombres pairs
Écrivez un programme qui utilise une boucle `for` pour afficher tous les nombres pairs de 0 à 20 inclus.

<details>
  <summary>Solution</summary>
  
  ```python
  for i in range(0, 21, 2):
      print(i)
  ```
</details>

## Exercice 2 : Somme des éléments d'une liste
Écrivez un programme qui utilise une boucle `for` pour calculer et afficher la somme des éléments d'une liste donnée `maListe = [1, 2, 3, 4, 5]`.

<details>
  <summary>Solution</summary>
  
```python
  maListe = [1, 2, 3, 4, 5]
  somme = 0
  for element in maListe:
      somme += element # equivalent de somme = somme + element
  print(somme)
  ```
</details>

## Exercice 3 : Boucle `while` et compteur
Écrivez un programme qui utilise une boucle `while` pour afficher les nombres de 10 à 1 dans l'ordre décroissant.

<details>
  <summary>Solution</summary>
  
  ```python
  compteur = 10
  while compteur > 0:
      print(compteur)
      compteur -= 1 # equivalent de compteur = compteur - 1
  ```
</details>

## Exercice 4 : Produit des éléments d'une liste
Écrivez un programme qui utilise une boucle `for` pour calculer et afficher le produit des éléments d'une liste donnée `maListe = [1, 2, 3, 4, 5]`.

<details>
  <summary>Solution</summary>
  
  ```python
  maListe = [1, 2, 3, 4, 5]
  produit = 1
  for element in maListe:
      produit *= element # equivalent de produit = produit * element
  print(produit)
  ```
</details>

## Exercice 5 : Filtrage des éléments d'une liste
Écrivez un programme qui utilise une boucle `for` pour afficher tous les éléments d'une liste `maListe = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` qui sont supérieurs à 5.

<details>
  <summary>Solution</summary>
  
  ```python
  maListe = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  for element in maListe:
      if element > 5:
          print(element)
  ```
</details>

## Exercice 6 : Calcul de la factorielle
Écrivez une fonction `factorielle(n)` qui utilise une boucle `for` pour calculer et renvoyer la factorielle de `n`. Testez la fonction avec différentes valeurs de `n`.

<details>
  <summary>Solution</summary>
  
  ```python
  def factorielle(n):
      resultat = 1
      for i in range(1, n + 1):
          resultat *= i
      return resultat

  # Tests de la fonction
  print(factorielle(5))  # Affiche : 120
  print(factorielle(3))  # Affiche : 6
  print(factorielle(0))  # Affiche : 1
  ```
</details>

## Exercice 7 : Somme des nombres impairs
Écrivez un programme qui utilise une boucle `while` pour calculer et afficher la somme de tous les nombres impairs de 1 à 10 inclus.

<details>
  <summary>Solution</summary>
  
  ```python
  somme = 0
  compteur = 1
  while compteur <= 10:
      if compteur % 2 != 0:
          somme += compteur
      compteur += 1
  print(somme)
  ```
</details>

## Exercice 8 : Affichage de mots dans une phrase
Écrivez un programme qui utilise une boucle `for` pour afficher chaque mot d'une phrase donnée `maPhrase = "Python est un langage de programmation"` sur une nouvelle ligne.

<details>
  <summary>Solution</summary>
  
  ```python
  # Solution 1
  maPhrase = "Python est un langage de programmation"
  mots = maPhrase.split()
  for mot in mots:
      print(mot)

# Solution 2
maPhrase = "Python est un langage de programmation"
mot = ""
for i in range(len(maPhrase)):
    lettre = maPhrase[i]
    mot += lettre 
    if lettre == " " or i == len(maPhrase) - 1:
        print(mot)
        mot = ""      
  ```
</details>

[Retour au cours](../Cours/11_Les%20Boucles.md) | 
[Cours Suivant](../Cours/12_La%20récursivité.md)
