# Cours Python

Ce cours présente 18 leçons sur les notions importantes de Python. Chacune d'elles comprend une page de cours et potentiellement des exercices. Tout le cours est disponible à l'adresse [suivante](https://github.com/Cmoitchoupi/Cours_python).

## Prérequis

### Installation de Python

Pour installer Python :

1. Ouvrez le Microsoft Store.
2. Recherchez Python.
3. Installez la dernière version disponible.

### Éditeur de code

Il existe différents éditeurs de code. Vous pouvez également coder sur Bloc-notes ou sur un terminal. Dans ce cours, nous utilisons Visual Studio Code (VSCode).

#### Installation de VSCode

Pour installer VSCode :

1. Rendez-vous sur [le site officiel](https://code.visualstudio.com/download) et suivez les instructions.

### Récupération du projet

Vous avez deux choix pour récupérer le projet :

#### Option 1 : Télécharger le zip

1. Rendez-vous à l'adresse ci-dessus.
2. Cliquez sur le bouton "Code" et sélectionnez "Download ZIP".
3. Décompressez le dossier dans le dossier cible.

#### Option 2 : Utiliser Git

1. Installez Git.
2. Ouvrez VSCode

⚠️ Il est important de lancer VSCode apres l'installation de Git sinon il peut ne pas être détecté

3. Placez-vous dans le dossier cible : cliquez sur "Fichier" dans la barre d'outils, puis sur "Ouvrir dossier". 
4. Ouvrez un terminal : cliquez sur "Terminal" dans la barre d'outils, puis sur "Nouveau terminal".
5. Exécutez la commande 
```bash
git clone https://github.com/Cmoitchoupi/Cours_python.git
```
⚠️ cloner le projet va creer un nouveau dossier `Cours_python` a l'emplacement choisi

6. Le projet sera cloné dans votre dossier.

### Utilisation de VSCode

1. Installez l'extension "Python" dans l'onglet prévu sur la gauche.

Vous pourrez ensuite créer des fichiers grâce à l'explorateur de fichiers sur la gauche. Pour créer un fichier Python, ajoutez l'extension `.py` au nom du fichier.

Pour visualiser un fichier .md d'exercice ou de cours :

- Utilisez l'URL du projet pour le visualiser sur le Web.

ou

- Selectionner le fichier que vous voulez visualiser, et utilisez le raccourci `Ctrl + K`, relâchez, puis appuyez sur `V`.

Pour exécuter le code :

- Cliquez sur le bouton "Run Python code" en haut à droite de la fenêtre.

ou

- Utilisez un terminal : Entrez `python nom_fichier` et appuyez sur Entrée.

## Organisation des Dossiers

Dans ce projet, nous avons trois dossiers principaux :

- Cours_base_python : Ce dossier reprend l'ensemble des fonctionnalités principales de Python depuis le début.
    - **cours** : Contient les cours.
    - **exercices** : Contient les exercices associées au cours
    - **Projets** : Contient un projet d'exemple sous différentes versions

- Projet : Il s'agit d'un projet réalisé pendant un cours de mon semestre 6. Il comprend toutes les parties vues dans **Cours_base_python**. Ce dossier est divisé en trois parties :
    - **cours** : Contient les cours.
    - **exercices** : Contient l'énoncé du projet avec le programme de départ.
    - **solution** : Contient la solution finale, corrigée.
    
- IA : Ce dossier contient tous les cours et feuilles de TP proposés par la ressource `"Base de l'IA"`.


[Premier cours base Python](./Cours_base_python/Cours/1_Les%20types%20simples.md)
