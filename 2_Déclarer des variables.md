# Déclarer des variables

Pour déclarer des variables en Python, nous n'avons pas besoin d’inclure le type de la variable. Il suffit de faire :

```python
ma_chaine = "premiere chaine"
mon_entier = 35
mon_numerique = 35.0 
mon_booleen = False
```

Si nous appelons les variables plus tard dans le fichier, elles contiendront toujours la même valeur à moins de la changer :

```python
print(ma_chaine)  # premiere chaine
ma_chaine = "autre chaine"
print(ma_chaine)  # autre chaine
```

### Remarques :

- Ne pas oublier les guillemets pour déclarer une chaîne.
- Ne pas mettre d'espace dans le nom des variables.
- Les booléens peuvent avoir comme valeur True, False ou 1 et 0.
- 35.0 et 35. sont le même nombre
- On peut décider de suivre des normes de langage comme le camel case :
- Pour commenter du code en Python, on utilise le symbole #. Tout ce qui suit ce caractère sur la même ligne sera inactif lors de l'exécution du code

- La règle dit que chaque première lettre d'un mot doit être en majuscule sauf pour le premier mot.
Dans notre cas, les variables devraient être renommées ainsi :

```python 
maChaine = "premiere chaine"
monEntier = 35
monNumerique = 35.0
monBooleen = False
```