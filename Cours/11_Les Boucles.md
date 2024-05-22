# Les Boucles

Les boucles sont des structures de contrôle qui permettent de répéter un bloc de code plusieurs fois. En Python, les deux principales boucles sont `for` et `while`.

### La boucle `for` ou `pour`

La boucle `for` permet d'itérer sur une séquence (comme une liste, un tuple, un dictionnaire, une chaîne de caractères, ou une plage de nombres). 

Exemple :

```python
# La boucle for avec range
# i prend les valeurs de 0 à 4
for i in range(5):
    print(i)
# Affiche : 
# 0
# 1
# 2
# 3
# 4

# La boucle for avec range et un pas
# j prend les valeurs de 0 à 8 avec un pas de 2
for j in range(0, 10, 2):
    print(j)
# Affiche :
# 0
# 2
# 4
# 6
# 8

# La boucle for qui itère de 5 vers 0
for valeur in range(5, 0, -1):
    print(valeur)
# Affiche :
# 5
# 4
# 3
# 2
# 1

# Itération sur une liste
maListe = [1, 2, 3, 4, 5]
for element in maListe:
    print(element)
# Affiche :
# 1
# 2
# 3
# 4
# 5

# Itération sur une liste
maListe = [1, 2, 3, 4, 5]
for i in range(len(liste)):
    print(i)
# Affiche :
# 1
# 2
# 3
# 4
# 5

# Itération sur une chaîne de caractères
maChaine = "Python"
for caractere in maChaine:
    print(caractere)
# Affiche chaque caractère de la chaîne "Python" sur une nouvelle ligne :
# P
# y
# t
# h
# o
# n

# Itération sur un dictionnaire
monDictionnaire = {"nom": "Alice", "age": 25, "ville": "Paris"}
for cle, valeur in monDictionnaire.items():
    print(f"{cle} : {valeur}")
# Affiche :
# nom : Alice
# age : 25
# ville : Paris
```

### La boucle `while` ou `tant que`

La boucle while continue de s'exécuter tant qu'une condition est vraie.

```python
compteur = 0
while compteur < 5: # tant que le compteur est plus petit que 5 on execute le code dans la boucle
    print(compteur)
    compteur += 1
# Affiche 0, 1, 2, 3, 4 chacun sur une nouvelle ligne
```

Globalement on peut effectuer les mêmes actions avec les deux boucles, cependant dans les gros projets une boucle est plus efficace qu'une autre en dépendant des besoins du programme.

### Utilisation de la boucle for :
- Idéale lorsque le nombre d'itérations est connu à l'avance ou lorsque vous itérez sur une séquence (comme une liste, un tuple, etc.).
- Plus lisible et plus concise dans de nombreux cas.
- Convient bien lorsque vous devez exécuter une action un nombre spécifique de fois.
### Utilisation de la boucle while :
- Préférable lorsque vous devez itérer jusqu'à ce qu'une condition soit remplie.
- Utile lorsque le nombre d'itérations n'est pas connu à l'avance.
- Plus flexible car vous pouvez contrôler les conditions d'arrêt de manière plus dynamique.

Remarques : 

- Certaines boucles peuvent être inifies si elles n'arrivent pas à leur condition d'arret, il faur y faire attention pour éviter que ca arrive

[Cours Précédent](../Cours/10_Les%20types%20complexes.md) | 
EX | 
[Cours suivant](../Cours/11_Les%20Boucles.md)