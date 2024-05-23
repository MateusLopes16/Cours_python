# Feuille d'Exercices : Les Classes en Python

## Exercice 1 : Création d'une classe Animal
1. Définissez une classe appelée `Peripherique`.
2. Ajoutez une méthode `__init__` à la classe `Peripherique` prenant les paramètres `couleur` et `pourcentage_batterie`.
3. À l'intérieur de la méthode `__init__`, initialisez les attributs `couleur` et `pourcentage_batterie` à partir des paramètres fournis, et un attribut `batterie_max` initialisé à 100.
4. Créez deux instances de la classe `Peripherique` avec des couleurs et des pourcentage_batterie différents.
5. Affichez les attributs `couleur` et `pourcentage_batterie` de chaque instance.

<details>
  <summary>Solution</summary>
  
  ```python
  class Peripherique:
      def __init__(self, couleur, pourcentage_batterie):
          self.couleur = couleur
          self.pourcentage_batterie = pourcentage_batterie
          self.batterie_max = 100

  mon_clavier = Peripherique("Noir", 80)
  ma_souris = Peripherique("Bleu", 50)

  print(mon_clavier.couleur, mon_clavier.pourcentage_batterie)  
  print(ma_souris.couleur, ma_souris.pourcentage_batterie)   
  ```
</details>

## Exercice 2 : Méthodes de classe Peripherique
1. Ajoutez une méthode `description` à la classe `Peripherique` qui retourne une chaîne de caractères décrivant le périphérique avec sa couleur et son pourcentage de batterie.
2. Ajoutez une méthode `recharger_batterie` à la classe `Peripherique` qui prend un pourcentage de charge, et non pas un nouveau pourcentage de batterie, en paramètre et met à jour l'attribut `pourcentage_batterie` de l'objet.
3. Appelez les méthodes `description` et `recharger_batterie` pour chaque instance créée dans l'exercice précédent.

<details>
  <summary>Solution</summary>
  
  ```python
  class Peripherique:
      def __init__(self, couleur, pourcentage_batterie):
          self.couleur = couleur
          self.pourcentage_batterie = pourcentage_batterie
          self.batterie_max = 100

      def description(self):
          return f"{self.couleur}, {self.pourcentage_batterie}% de batterie"

      def recharger_batterie(self, pourcentage_charge):
          self.pourcentage_batterie += pourcentage_charge
          if self.pourcentage_batterie > self.batterie_max:
              self.pourcentage_batterie = self.batterie_max

  mon_clavier = Peripherique("Noir", 80)
  ma_souris = Peripherique("Bleu", 50)

  print(mon_clavier.description())  
  print(ma_souris.description())   

  mon_clavier.recharger_batterie(20)
  ma_souris.recharger_batterie(40)

  print(mon_clavier.description())  
  print(ma_souris.description())  
  ```
</details>

## Exercice 3 : Héritage avec les classes Clavier et Souris
1. Créez une classe `Clavier` qui hérite de la classe `Peripherique`.
2. Ajoutez un attribut supplémentaire `type` à la classe `Clavier`.
3. Ajoutez une méthode `appuyer_touche` à la classe `Clavier` qui retourne une chaîne de caractères indiquant que la touche a été appuyée.
4. Créez une classe `Souris` qui hérite également de la classe `Peripherique`.
5. Ajoutez un attribut supplémentaire `boutons` à la classe `Souris`.
6. Ajoutez une méthode `clic` à la classe `Souris` qui retourne une chaîne de caractères indiquant que le bouton de la souris a été cliqué.
7. Créez une instance de la classe `Clavier` et une instance de la classe `Souris`, et appelez les méthodes spécifiques à chaque classe.

<details>
  <summary>Solution</summary>
  
  ```python
  class Clavier(Peripherique):
      def __init__(self, couleur, pourcentage_batterie, type):
          super().__init__(couleur, pourcentage_batterie)
          self.type = type

      def appuyer_touche(self):
          return "Touche appuyée"

  class Souris(Peripherique):
      def __init__(self, couleur, pourcentage_batterie, boutons):
          super().__init__(couleur, pourcentage_batterie)
          self.boutons = boutons

      def clic(self):
          return "Bouton de la souris cliqué"

  mon_clavier = Clavier("Noir", 80, "Mécanique")
  ma_souris = Souris("Bleu", 50, 3)

  print(mon_clavier.description())  
  print(mon_clavier.appuyer_touche())  

  print(ma_souris.description())   
  print(ma_souris.clic())  
  ```
</details>

## Exercice 4 : Utilisation de la méthode héritée
1. Utilisez la méthode `recharger_batterie` de la classe `Peripherique` pour recharger la batterie de l'instance de la classe `Clavier` créée dans l'exercice précédent avec un pourcentage de charge de 30%.
2. Affichez la description du clavier après avoir rechargé la batterie.

<details>
  <summary>Solution</summary>
  
  ```python
  mon_clavier = Clavier("Noir", 80, "Mécanique")
  mon_clavier.recharger_batterie(30)
  print(mon_clavier.description())  
  ```
</details>


[Retour au cours](../Cours/13_Les%20classes.md) | 
[Cours Suivant](../Cours/14_Gestion%20des%20erreurs%20et%20des%20exceptions.md)