# Traitement de fichiers

## Introduction

Le traitement de fichiers en Python permet de lire, écrire et manipuler des fichiers sur le système de fichiers. Python offre plusieurs façons de travailler avec les fichiers, que ce soit des fichiers texte ou des fichiers binaires.

## Ouvrir un fichier

Pour ouvrir un fichier en Python, utilisez la fonction `open()`. Cette fonction prend deux arguments principaux : le nom du fichier et le mode d'ouverture.

```python
# Ouvrir un fichier en mode lecture (r)
fichier = open('exemple.txt', 'r')
```

Les modes les plus couramment utilisés sont :
- `'r'` : lecture seule
- `'w'` : écriture (écrase le fichier s'il existe déjà)
- `'a'` : ajout (écrit à la fin du fichier)
- `'b'` : mode binaire (ajouter à `'r'`, `'w'` ou `'a'`)

## Lire un fichier

Pour lire le contenu d'un fichier, utilisez les méthodes `read()`, `readline()` ou `readlines()`.

```python
# Lire tout le contenu du fichier
contenu = fichier.read()
print(contenu)
fichier.close()
```

```python
# Lire le fichier ligne par ligne
fichier = open('exemple.txt', 'r')
for ligne in fichier:
    print(ligne, end='')
fichier.close()
```

## Écrire dans un fichier

Pour écrire dans un fichier, ouvrez-le en mode écriture (`'w'`) ou ajout (`'a'`), puis utilisez la méthode `write()`.

```python
# Écrire dans un fichier
fichier = open('exemple.txt', 'w')
fichier.write("Bonjour, monde!")
fichier.close()
```

```python
# Ajouter à un fichier
fichier = open('exemple.txt', 'a')
fichier.write("\nAjouter une nouvelle ligne.")
fichier.close()
```

## Utiliser le bloc `with`

Utiliser le mot-clé `with` pour ouvrir et fermer automatiquement le fichier.

```python
# Utiliser 'with' pour ouvrir et fermer le fichier automatiquement
with open('exemple.txt', 'r') as fichier:
    contenu = fichier.read()
    print(contenu)
```

```python
# Écrire dans un fichier avec 'with'
with open('exemple.txt', 'w') as fichier:
    fichier.write("Bonjour, monde!")
```

## Gérer les exceptions

Il est important de gérer les erreurs lors de l'ouverture et de la manipulation des fichiers.

```python
try:
    fichier = open('exemple.txt', 'r')
    contenu = fichier.read()
    print(contenu)
except FileNotFoundError:
    print("Le fichier n'a pas été trouvé.")
finally:
    fichier.close()
```

## Les fichiers binaires

Pour travailler avec des fichiers binaires, utilisez le mode `'b'`.

```python
# Lire un fichier binaire
with open('image.png', 'rb') as fichier:
    contenu = fichier.read()
    print(contenu[:20])  # Affiche les 20 premiers octets
```

```python
# Écrire dans un fichier binaire
with open('image_copie.png', 'wb') as fichier:
    fichier.write(contenu)
```

[Cours Précédent](../Cours/14_Gestion%20des%20erreurs%20et%20des%20exceptions.md) | 
[Page d'exercices](../Exercices/Exercices_traitement_fichiers.md) | 
[Cours suivant](../Cours/16_Les%20test%20unitaires.md)
