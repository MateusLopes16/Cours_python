# Portes logiques

On peut pousser plus loin les conditions en y intégrant tout ce qui est opérations logiques. Les opérations logiques sont des opérations entre deux booléens à la fois. Il existe trois opérations logiques principales :

- **Et** : Les deux valeurs sont vraies.

| a    | b    | Résultat |
|------|------|----------|
| Vrai | Vrai | **Vrai**     |
| Vrai | Faux | **Faux**     |
| Faux | Vrai | **Faux**     |
| Faux | Faux | **Faux**     |

- **Ou** : Au moins l'une des valeurs est vraie.

| a    | b    | Résultat |
|------|------|----------|
| Vrai | Vrai | **Vrai**     |
| Vrai | Faux | **Vrai**     |
| Faux | Vrai | **Vrai**     |
| Faux | Faux | **Faux**     |

- **Ou exclusif** : Une seule des valeurs est vraie, mais pas les deux.

| a    | b    | Résultat |
|------|------|----------|
| Vrai | Vrai | **Faux**     |
| Vrai | Faux | **Vrai**     |
| Faux | Vrai | **Vrai**     |
| Faux | Faux | **Faux**     |

Ils sont représentés par `and`, `or` et `xor` en Python.

Exemple :

```python
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(a ^ b)    # True (XOR)
```

Comme dit précédemment, on peut intégrer les opérations logiques dans nos conditions.

```python
x = True 
y = False
z = True

if x and y:
    print("x and y") # ne va pas s'executer car x est vrai mais pas y
elif x and z:
    print("x and z") # va s'executer car les deux valeurs sont vraies
else:
    print("x") # ne va pas s'executer car on a rempli une condition précédente

a = False

if a or y:
    print("a or y") # ne va pas s'executer car les deux valeurs sont fausses
elif x or a:
    print("x or z") # va s'executer car x est vrai
else:
    print("x") # ne va pas s'executer car on a rempli une condition précédente
```
