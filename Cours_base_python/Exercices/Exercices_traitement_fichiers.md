# Exercices de Traitement de fichiers

## Exercice 1 : Lecture de fichier

Écrivez un programme Python qui lit le contenu d'un fichier nommé `poeme.txt` et affiche son contenu ligne par ligne.

<details>
  <summary>Solution</summary>
  
  ```python
  with open('poeme.txt', 'r') as fichier:
      for ligne in fichier:
          print(ligne, end='')
  ```
</details>

## Exercice 2 : Compter les lignes

Modifiez le programme précédent pour compter et afficher le nombre de lignes dans le fichier `poeme.txt`.

<details>
  <summary>Solution</summary>
  
  ```python
  nombre_lignes = 0
  with open('poeme.txt', 'r') as fichier:
      for ligne in fichier:
          nombre_lignes += 1
  print(f'Le fichier contient {nombre_lignes} lignes.')
  ```
</details>

## Exercice 3 : Écriture dans un fichier

Écrivez un programme qui demande à l'utilisateur de saisir une phrase et qui écrit cette phrase dans un fichier nommé `output.txt`.

<details>
  <summary>Solution</summary>
  
  ```python
  phrase = input("Saisissez une phrase : ")
  with open('output.txt', 'w') as fichier:
      fichier.write(phrase)
  ```
</details>

## Exercice 4 : Ajout dans un fichier

Modifiez le programme précédent pour qu'il ajoute la phrase saisie par l'utilisateur à la fin du fichier `output.txt` au lieu de l'écraser.

<details>
  <summary>Solution</summary>
  
  ```python
  phrase = input("Saisissez une phrase : ")
  with open('output.txt', 'a') as fichier:
      fichier.write(phrase + '\n')
  ```
</details>

## Exercice 5 : Gestion des exceptions

Écrivez un programme qui tente de lire un fichier nommé `inexistant.txt` et gère l'erreur si le fichier n'existe pas.

<details>
  <summary>Solution</summary>
  
  ```python
  try:
      with open('inexistant.txt', 'r') as fichier:
          contenu = fichier.read()
          print(contenu)
  except FileNotFoundError:
      print("Le fichier 'inexistant.txt' n'a pas été trouvé.")
  ```
</details>

## Exercice 6 : Copier un fichier binaire

Écrivez un programme qui copie un fichier binaire nommé `source.bin` vers un fichier `destination.bin`.

<details>
  <summary>Solution</summary>
  
  ```python
  with open('source.bin', 'rb') as fichier_source:
      contenu = fichier_source.read()
  with open('destination.bin', 'wb') as fichier_destination:
      fichier_destination.write(contenu)
  ```
</details>

## Exercice 7 : Lire les premières lignes

Écrivez un programme qui lit et affiche les 5 premières lignes d'un fichier nommé `grand_texte.txt`.

<details>
  <summary>Solution</summary>
  
  ```python
  with open('grand_texte.txt', 'r') as fichier:
      for i in range(5):
          ligne = fichier.readline()
          if not ligne:
              break
          print(ligne, end='')
  ```
</details>

## Exercice 8 : Mot le plus fréquent

Écrivez un programme qui lit un fichier nommé `texte.txt`, compte la fréquence de chaque mot et affiche le mot le plus fréquent.

<details>
  <summary>Solution</summary>
  
  ```python
  from collections import Counter
  
  with open('texte.txt', 'r') as fichier:
      contenu = fichier.read()
  mots = contenu.split()
  compte_mots = Counter(mots)
  mot_frequent = compte_mots.most_common(1)[0]
  print(f"Le mot le plus fréquent est '{mot_frequent[0]}' avec {mot_frequent[1]} occurrences.")
  ```
</details>

[Cours Précédent](../Cours/15_Traitement%20de%20fichiers.md) | 
[Cours suivant](../Cours/16_Les%20test%20unitaires.md)
