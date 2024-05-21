# Les classes

En Python, les classes permettent de créer vos propres types de données définis par l'utilisateur. Une classe est un modèle pour créer des objets (une instance de la classe). Les classes encapsulent les données et les comportements qui sont associés.

Elles permettent de regrouper plusieurs variables de différents types dans un seul type.

Concrètement, prenons un animal il possede un nom, un poids, une taille...

Pour matérialiser cet animal, créons une classe qui contiendra chacune de ces variables.

### Définir une classe

Pour définir une classe, utilisez le mot-clé `class` suivi du nom de la classe. Par convention, les noms de classe utilisent le style CamelCase.

```python
class Animal:
    pass  # Utilisez 'pass' pour une classe vide

```

### Initialiser une classe

La méthode `__init__` est une méthode spéciale appelée un constructeur. Elle est appelée lorsque vous créez une nouvelle instance de la classe.
C'est ici qu'on va définir toutes les variables de notre classe.

On utilise le mot-clé `self` pour déterminer les attributs associées à la classe.
On passe en paramètre toutes les valeurs uniques à chaque instance de la classe.
On peut aussi avoir des valeurs communes.

```python
class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.lieu = "Maison"
```

### Créer une instance

Une instance d'une classe est un objet qu'on crée. Chaque classe peut avoir un nombre illimité d'instances.

Pour créer une instance d'une classe, appelez la classe comme si c'était une fonction.

```python
mon_premier_animal = Animal("Max", 3)
mon_second_animal = Animal("Luna", 5)
```

### Attributs d'instance

Les attributs d'instance sont des variables appartenant à l'instance spécifique d'une classe. Ils sont définis dans la méthode `__init__` en utilisant `self`.

```python
print(mon_premier_animal.nom)  # Affiche "Max"
print(mon_premier_animal.age)  # Affiche 3

print(mon_second_animal.nom)  # Affiche "Luna"
print(mon_second_animal.age)  # Affiche 5
```

### Méthodes

Pour chaque classe, on peut définir des fonctions propres à la classe qu'on appelle méthodes. Elles sont utilisées pour définir les comportements des objets de la classe.

```python
class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def decrit(self):
        return f"{self.nom} a {self.age} ans."

    def changeAge(self, age):
        self.age = age

mon_premier_animal = Animal("Max", 3)
print(mon_premier_animal.decrit())  # Affiche "Max a 3 ans."
mon_premier_animal.changeAge(4)
print(mon_premier_animal.decrit())  # Affiche "Max a 4 ans."
```

Dans les méthodes de classe, le mot-clé `self` passé en paramètre sert à identifier quelle instance de la classe on modifie.

Ici, la méthode `decrit` est appelée à la suite de `mon_premier_animal`, la méthode va donc considérer qu'on appelle la méthode `decrit` sur l'objet/l'instance `mon_premier_animal`, et elle va donc récupérer les informations propres à cette instance qu'on a défini au moment de la création.


### Héritage

L'héritage est une notion un peu plus complexe qui permet de créer une nouvelle classe basée sur une classe existante. La nouvelle classe (classe enfant) hérite des attributs et des méthodes de la classe existante (classe parent).

Concrètement, si on veut représenter les chiens et les chats, nous pouvons partir du principe que ces deux espèces soient toutes les deux des animaux auxquels on ajoute d'autres paramètres.

On utilise donc la notion d'héritage avec une classe parent qui contient tous les paramètres/attributs en commun entre les espèces animales et on crée une classe pour chaque animal avec les paramètres supplémentaires qu'il a besoin.

```python
class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def decrit(self):
        return f"{self.nom} a {self.age} ans."

class Chien(Animal):
    def __init__(self, nom, age, race):
        super().__init__(nom, age)  # Appel du constructeur de la classe parent
        self.race = race

    def aboie(self):
        return f"{self.nom} aboie!"

class Chat(Animal):
    def __init__(self, nom, age, couleur):
        super().__init__(nom, age)  # Appel du constructeur de la classe parent
        self.couleur = couleur

    def miaule(self):
        return f"{self.nom} miaule!"

mon_chien = Chien("Rex", 5, "Labrador")
mon_chat = Chien("Max", 6, "Gris")

print(mon_chien.decrit())  # Affiche "Rex a 5 ans."
print(mon_chien.aboie())   # Affiche "Rex aboie!"

print(mon_chat.decrit())  # Affiche "Max a 6 ans."
print(mon_chat.miaule())   # Affiche "Max miaule!"

print(mon_chat.aboie()) # provoque une erreur car mon_chat n'est pas un chien
```

### Remarque 

- Programmer avec des classes, on appelle ça l'orienté objet.

[Cours Précédent](../Cours/12_La%20récursivité.md) | 
[Cours suivant](../Cours/14_Gestion%20des%20erreurs%20et%20des%20exceptions.md)