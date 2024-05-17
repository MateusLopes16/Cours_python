# Les types complexes

Les types qu'on appelle complexes sont des types natifs au langage qui permettent de réunir plusieurs valeurs dans une seule variable.

Parmi les plus courants, on trouve :

- **Liste** `[]` : Une liste est un ensemble de valeurs entourées par des **[]** que l'on peut modifier dans le code.
- **Tuple** `()` : Un tuple est un ensemble de valeurs entourées par des **()**. Le tuple n'est pas modifiable.
- **Dictionnaire** `{}` : Un dictionnaire est un ensemble de données associées par un nom et une valeur.

Les valeurs dans les listes et les tuples sont accessibles grâce à la position dans la liste qu'on appelle `indice`.
⚠️ L'indice commence à `0` et non à `1`.

```python
monTableau = [1, 2, 3, 4, 5, 6]
monTuple = (1, 2, 3, 4, 5, 6)
monDictionnaire = {"nom": "Alice", "age": 25, "ville": "Paris"}

print(monTableau[0])  # affiche 1
print(monTableau[1])  # affiche 2

print(monTuple[6])    # provoque une erreur
print(monTuple[5])    # affiche 6

print(monDictionnaire["nom"])  # affiche Alice
print(monDictionnaire["age"])  # affiche 25
```

Il existe des fonctions natives pour ajouter ou supprimer des valeurs dans les tableau :

- `monTableau.append(5)` : ajoute la valeur 5 à la fin de la liste `monTableau`.
- `monTableau.pop()` : supprime la dernière valeur de la liste `monTableau`.

N'hésitez pas à consulter la documentation officielle pour plus découvrir toutes les fonctions et pour plus d'informations sur ces fonctions :
[Documentation officielle Python](https://docs.python.org/fr/3/library/functions.html)

```python
monTableau = [1, 2, 3, 4, 5, 6]
monTableau.append(9)  # ajoute la valeur 9 à la fin de la liste

print(monTableau)  # affiche [1, 2, 3, 4, 5, 6, 9]

monTableau.pop()  # supprime la dernière valeur de la liste

print(monTableau)  # affiche [1, 2, 3, 4, 5, 6]

```


Il existe des fonctions natives pour ajouter ou supprimer des valeurs dans les dictionnaires :

- `monDictionnaire["nouvelle_cle"] = "nouvelle_valeur"` : ajoute une nouvelle clé avec sa valeur dans le dictionnaire `monDictionnaire`.
- `monDictionnaire.pop("cle")` : supprime la clé spécifiée et sa valeur du dictionnaire `monDictionnaire`.

Exemple :

```python
monDictionnaire = {"nom": "Alice", "age": 25, "ville": "Paris"}
monDictionnaire["profession"] = "Ingénieure"  # Ajoute une nouvelle clé et valeur

print(monDictionnaire)  # affiche {'nom': 'Alice', 'age': 25, 'ville': 'Paris', 'profession': 'Ingénieure'}

monDictionnaire.pop("age")  # Supprime la clé 'age' et sa valeur

print(monDictionnaire)  # affiche {'nom': 'Alice', 'ville': 'Paris', 'profession': 'Ingénieure'}
```
