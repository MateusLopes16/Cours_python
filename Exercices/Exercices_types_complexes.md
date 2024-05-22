# Feuille d'Exercices : Les Types Complexes en Python

## Exercice 1 : Manipulation de listes
1. Créez une liste appelée `maListe` contenant les nombres 1, 2, 3, 4, et 5.
2. Ajoutez le nombre 6 à la fin de la liste.
3. Supprimez le dernier élément de la liste.
4. Affichez le deuxième élément de la liste.
5. Remplacez le troisième élément de la liste par le nombre 10.

<details>
  <summary>Solution</summary>
  
  ```python
  maListe = [1, 2, 3, 4, 5]
  maListe.append(6)
  maListe.pop()
  print(maListe[1])
  maListe[2] = 10
  print(maListe)
  ```
</details>

## Exercice 2 : Manipulation de tuples
1. Créez un tuple appelé `monTuple` contenant les nombres 1, 2, 3, 4, et 5.
2. Affichez le premier élément du tuple.
3. Tentez de remplacer le deuxième élément du tuple par le nombre 20 et observez ce qui se passe.

<details>
  <summary>Solution</summary>
  
  ```python
  monTuple = (1, 2, 3, 4, 5)
  print(monTuple[0])
  # monTuple[1] = 20  # provoque une erreur car les tuples sont immuables
  ```
</details>

## Exercice 3 : Manipulation de dictionnaires
1. Créez un dictionnaire appelé `monDictionnaire` avec les paires clé-valeur suivantes : "nom" : "Alice", "age" : 25, "ville" : "Paris".
2. Ajoutez une nouvelle paire clé-valeur "profession" : "Ingénieure".
3. Modifiez la valeur associée à la clé "age" pour qu'elle soit 26.
4. Supprimez la paire clé-valeur avec la clé "ville".
5. Affichez uniquement les clés du dictionnaire.

<details>
  <summary>Solution</summary>
  
  ```python
  monDictionnaire = {"nom": "Alice", "age": 25, "ville": "Paris"}
  monDictionnaire["profession"] = "Ingénieure"
  monDictionnaire["age"] = 26
  monDictionnaire.pop("ville")
  print(monDictionnaire.keys())
  ```
</details>

[Retour au cours](../Cours/10_Les%20types%20complexes.md) | 
[Cours Suivant](../Cours/11_Les%20Boucles.md)
