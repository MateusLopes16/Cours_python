# Les Fonctions  

Chaque bloc de code peut être séparé en fonctions. Une fonction est un bloc de code réutilisable qui remplit une tâche précise.

On initialise une fonction grâce au mot-clé `def`, suivi du nom de la fonction entre parenthèses, et enfin deux points :

```python
def affiche():
    print("Dans la fonction affiche")
```

### Paramètres des fonctions

Les fonctions peuvent contenir ou non ce qu'on appelle des paramètres, ce sont des valeurs que l'on transmet du code principal vers la fonction.

Ces paramètres sont déclarés dans les parenthèses de la fonction.

Une fonction a besoin d'être appelée pour être utilisée :

```python
premier_message = "Je suis le message"

def affiche(message):
    print(message)  # Affiche le message 'Je suis le message'

x = 10
y = 10

def multiplie(x, y):
    print(x * y)  # Affiche 100

affiche(premier_message)
```

### Le retour

Une fonction peut renvoyer des valeurs au code principal en utilisant le mot-clé ``return``.

Chaque fonction qui renvoie une valeur doit se voir attribuer une variable pour pouvoir l'utiliser par la suite.

```python
premier_message = "Je suis le message"

def ajouteUnPoint(message):
    return message + "."

nouveau_message = ajouteUnPoint(premier_message)
print(nouveau_message) # affiche 'Je suis le message.'
```

### Remarques : 

- Il est important de déclarer la fonction avant de l'appeler.
- Une fonction n'a pas accès aux déclarations de variables du fichier.

```python
message = "je suis le message"

def affiche():
    print(message) # provoque une erreur car message n'est pas défini dans la fonction
```


[Cours suivant](../Cours/8_Portes%20logiques.md)