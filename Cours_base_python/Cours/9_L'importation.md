# L'importation

Dans python il existe la notion d'importation, elle permet a ne pas avoir a réécrire les mêmes fonctions a trâvers les différents fichiers du même projet, ou a pourvoir integrer des modules, ou librairies, dans nos projets tels que le module `math` qui permet de completer le projet avec des formules mathématiques complexes comme la racine carrée.

```python
from math import sqrt # permet d'import uniquement la racine carre

print(sqrt(25))

import math # importe toute la librairie/module math

print(math.sqrt(25))

import math as m # renomme la librairie math par m

print(m.sqrt(25))

from premier_fichier import premiere_fonction # importe la fonction premiere_fonction a notre fichier

premiere_fonction # execute la fonction premiere_fonction du fichier premier_fichier
```

[Cours Précédent](../Cours/8_Portes%20logiques.md) | 
[Cours suivant](../Cours/10_Les%20types%20complexes.md)