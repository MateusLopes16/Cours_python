# Operations sur chaines

Les chaînes de caractères en Python peuvent être manipulées de différentes manières. Voici quelques opérations courantes que vous pouvez effectuer sur les chaînes :

### Concaténation

La concaténation consiste à joindre deux chaînes de caractères pour en former une seule.

```python
chaine1 = "Bonjour"
chaine2 = "monde"
chaine_concatenee = chaine1 + " " + chaine2
print(chaine_concatenee)
# Affiche : Bonjour monde
```

### Multiplication

La multiplication d'une chaîne de caractères par un entier répète la chaîne le nombre de fois spécifié par cet entier.

```python
chaine = "Python "
chaine_multipliee = chaine * 3
print(chaine_multipliee)
# Affiche : Python Python Python
```

### Accès aux caractères

Vous pouvez accéder aux caractères individuels d'une chaîne en utilisant l'index de chaque caractère. L'indexation commence à 0 pour le premier caractère.

```python
chaine = "Python"
print(chaine[0])  # Affiche le premier caractère "P"
print(chaine[-1]) # Affiche le dernier caractère "n"
```

### Slicing (découpage)

Le slicing permet d'extraire une partie d'une chaîne en spécifiant une plage d'index.

```python
chaine = "Python"
print(chaine[2:5])  # Affiche "tho"
```

### Méthodes de formatage

Python offre différentes méthodes pour formater les chaînes de caractères, telles que format() et les f-strings.

```python
nom = "Alice"
age = 30
print("Je m'appelle nom et j'ai age ans.")
# Affiche : Je m'appelle nom et j'ai age ans.

print("Je m'appelle {} et j'ai {} ans.".format(nom, age))
# Affiche : Je m'appelle Alice et j'ai 30 ans.

print(f"Je m'appelle {nom} et j'ai {age} ans.")
# Affiche : Je m'appelle Alice et j'ai 30 ans.
```

[Cours Précédent](../Cours/3_Operations.md) | 
[Cours suivant](../Cours/5_Les%20Fonctions%20natives.md)