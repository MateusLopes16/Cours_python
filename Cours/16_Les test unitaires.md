# Les test unitaires

[Cours Précédent](../Cours/15_Traitement%20de%20fichiers.md) | 
[Cours suivant](../Cours/17_La%20documentation.md)

### Introduction aux tests unitaires

Les tests unitaires sont une pratique essentielle en développement logiciel. Ils consistent à tester individuellement chaque composant logiciel pour s'assurer qu'il fonctionne correctement de manière isolée.

### Écriture de tests unitaires en Python

En Python, le module `unittest` est souvent utilisé pour écrire des tests unitaires. Voici un exemple de test unitaire pour la fonction qui trouve le mot le plus fréquent dans un fichier :

```python
import unittest
from collections import Counter

def mot_plus_frequent(nom_fichier):
    with open(nom_fichier, 'r') as fichier:
        contenu = fichier.read()
    mots = contenu.split()
    compte_mots = Counter(mots)
    mot_frequent = compte_mots.most_common(1)[0]
    return mot_frequent

class TestMotPlusFrequent(unittest.TestCase):

    def test_mot_plus_frequent(self):
        mot = mot_plus_frequent('texte.txt') # Verifier le chemin d'acces
        self.assertEqual(mot, ('Python', 5))

if __name__ == '__main__':
    unittest.main()
```

### Explication du code

- La fonction `mot_plus_frequent` prend le nom d'un fichier en entrée et renvoie le mot le plus fréquent ainsi que son nombre d'occurrences.
- La classe `TestMotPlusFrequent` hérite de `unittest.TestCase` et contient une méthode `test_mot_plus_frequent` qui teste la fonction `mot_plus_frequent`.
- Dans la méthode de test, nous appelons `mot_plus_frequent` avec un fichier de test `texte.txt`, contenu dans le repertoire fichiers, et vérifions si le résultat est celui attendu.

### Exécution des tests unitaires

Pour exécuter les tests unitaires, exécutez le script Python. Les résultats des tests seront affichés dans la console.

### Avantages des tests unitaires
- Les tests unitaires permettent de vérifier le bon fonctionnement des composants logiciels de manière automatisée.
- Ils facilitent la détection précoce des erreurs et des bogues.
- Ils favorisent la conception modulaire et la réutilisation du code.

[Cours Précédent](../Cours/15_Traitement%20de%20fichiers.md) | 
[Cours suivant](../Cours/17_La%20documentation.md)