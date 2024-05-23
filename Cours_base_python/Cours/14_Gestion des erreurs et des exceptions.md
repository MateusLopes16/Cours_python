# Gestion des erreurs et des exceptions

En programmation, les erreurs peuvent survenir pour diverses raisons, telles que des erreurs de syntaxe, des erreurs de logique ou des situations imprévues. Pour gérer ces erreurs de manière efficace, Python propose des mécanismes de gestion des erreurs et des exceptions.

## Les types d'erreurs

### SyntaxError

Une erreur de syntaxe se produit lorsque le code ne respecte pas les règles de syntaxe de Python. Par exemple, une parenthèse manquante ou une indentation incorrecte peuvent entraîner une SyntaxError.

### NameError

Une NameError se produit lorsqu'un nom ou un symbole utilisé dans le code n'est pas défini. Cela peut se produire lorsque vous essayez d'utiliser une variable qui n'a pas été déclarée.

### TypeError

Une TypeError se produit lorsqu'une opération est effectuée sur un objet dont le type ne prend pas en charge cette opération. Par exemple, l'ajout d'un entier à une chaîne de caractères provoque une TypeError.

## Les exceptions

### try...except

Pour gérer les erreurs de manière contrôlée, Python utilise la structure try...except. Dans un bloc try, vous placez le code susceptible de provoquer une erreur, et dans le bloc except, vous spécifiez comment gérer cette erreur.

```python
try:
    resultat = 10 / 0
except ZeroDivisionError:
    print("Division par zéro !")
```

### finally

La clause finally est utilisée pour exécuter un code indépendamment de la survenue d'une exception ou non. Cela peut être utile pour nettoyer les ressources ou effectuer des actions de clôture.

```python
try:
    fichier = open("mon_fichier.txt", "r")
    contenu = fichier.read()
except FileNotFoundError:
    print("Fichier non trouvé !")
finally:
    fichier.close()
```

### raise

Vous pouvez également lever une exception manuellement à l'aide du mot-clé raise. Cela permet de signaler une condition d'erreur spécifique dans votre programme.

```python
age = -1
if age < 0:
    raise ValueError("L'âge ne peut pas être négatif")
```

## Gestion des exceptions spécifiques

Vous pouvez utiliser plusieurs blocs except pour gérer différents types d'exceptions de manière spécifique.

```python
try:
    resultat = 10 / 0
except ZeroDivisionError:
    print("Division par zéro !")
except TypeError:
    print("Type de données incorrect !")
```

[Cours Précédent](../Cours/13_Les%20classes.md) | 
[Cours suivant](../Cours/15_Traitement%20de%20fichiers.md)