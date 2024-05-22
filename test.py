maPhrase = "Python est un langage de programmation"
mot = ""
for i in range(len(maPhrase)):
    lettre = maPhrase[i]
    mot += lettre 
    if lettre == " " or i == len(maPhrase) - 1:
        print(mot)
        mot = "" 