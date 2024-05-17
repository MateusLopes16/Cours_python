# Exercice 1

Écrivez un programme qui prend un nombre entier en entrée de l'utilisateur et affiche "Pair" s'il est pair et "Impair" s'il est impair.

<details>
  <summary>Solution</summary>
  
  ```python
nombre_choisis = input("Veuillez entrer un nombre : ")

if int(nombre_choisis) % 2 == 0:
    print("Pair")
else:
    print("Impair")
```
</details>

# Exercice 2

Écrivez un programme qui prend un nombre entier en entrée de l'utilisateur et affiche "Positif" s'il est strictement positif, "Nul" s'il est nul et "Negatif" s'il est strictement négatif.

<details>
  <summary>Solution</summary>
  
  ```python
nombre_choisis = int(input("Veuillez entrer un nombre : "))

if nombre_choisis > 0:
  print("Positif")
elif nombre_choisis == 0:
  print("Nul")
else:
  print("Negatif")
```
</details>

# Exercice 3

Écrivez un programme qui prend deux nombres en entrée de l'utilisateur et affiche "Le premier nombre est plus grand" si le premier nombre est plus grand que le deuxième, "Le deuxième nombre est plus grand" s'il est plus petit, et "Les deux nombres sont égaux" s'ils sont égaux.

<details>
  <summary>Solution</summary>
  
  ```python
nombre1 = int(input("Entrez le premier nombre : "))
nombre2 = int(input("Entrez le deuxième nombre : "))

if nombre1 > nombre2:
    print("Le premier nombre est plus grand")
elif nombre1 < nombre2:
    print("Le deuxième nombre est plus grand")
else:
    print("Les deux nombres sont égaux")
```
</details>

# Exercice 4

Écrivez un programme qui prend deux nombres en entrée de l'utilisateur et affiche "Le premier nombre est divisible par le deuxième" si le premier nombre est divisible par le deuxième, et "Le premier nombre n'est pas divisible par le deuxième" sinon.

<details>
  <summary>Solution</summary>
  
  ```python
nombre1 = int(input("Entrez le premier nombre : "))
nombre2 = int(input("Entrez le deuxième nombre : "))

if nombre1 % nombre2 == 0:
    print("Le premier nombre est divisible par le deuxième")
else:
    print("Le premier nombre n'est pas divisible par le deuxième")
```
</details>



[Retour au cours](../Cours/6_Conditions.md) | 
[Cours suivant](../Cours/7_Les%20Fonctions.md)

