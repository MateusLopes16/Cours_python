# La récursivité

La récursivité est un concept fondamental en programmation où une fonction se rappelle elle-même pour résoudre un problème. Elle est largement utilisée pour résoudre des problèmes qui peuvent être décomposés en des sous-problèmes plus petits et similaires.

### Fonction récursive
Une fonction récursive est une fonction qui s'appelle elle-même à l'intérieur de sa définition. Elle comprend deux parties :

Cas de base : Une condition qui spécifie quand la fonction doit arrêter de s'appeler elle-même. C'est essentiel pour éviter une boucle infinie.
Cas récursif : Une ou plusieurs appels récursifs à la fonction elle-même, avec des arguments différents, pour résoudre le problème de manière itérative.

```python
nombre = 5

def fonctionX(i):
    if i == 1:
        return 1
    else:
        return i + fonctionX(i - 1)

resultat = fonctionX(nombre)
print(resultat) # affiche 15
```

La fonction précédente effectue les actions suivantes :

- On vérifie la valeur de `i` qui est égale à 5.
  - 5 n'est pas égal à 1 donc on fait :
    - ``5 + fonctionX(4)``

- On vérifie la valeur de `i` qui est égale à 4.
  - 4 n'est pas égal à 1 donc on fait :
    - ``5 + 4 + fonctionX(3)`` car **function(5)** nous renvoie `5 + fonctionX(4)` et **fonctionX(4)** renvoie `4 + fonctionX(3)` on a donc `5 + 4 + fonctionX(3)`

- On continue jusqu'à arriver à la condition d'arrêt étant `i == 1` qui renvoie simplement 1.

- On a donc 5 + 4 + 3 + 2 + 1, ce qui donne 15.

### Remarque 

Certaines fonctions récursives peuvent demander trop de ressources et de stockage d'informations en attendant la condition d'arrêt, ce qui peut entraîner une surcharge et un plantage du programme. Il est donc important de bien analyser et optimiser les fonctions récursives pour éviter ces problèmes potentiels.

[Cours Précédent](../Cours/11_Les%20Boucles.md) | 
[Cours suivant](../Cours/12_La%20récursivité.md)