# creer le jeu mastermind

import random

def mastermind():
    chaine_a_trouver = ""
    for i in range(4):
        chaine_a_trouver += str(random.randint(0, 9))

    # print(chaine_a_trouver) # pour afficher la solution quand on teste le programme
    
    print("Bienvenue dans le jeu du Mastermind !")
    print("Trouvez la combinaison à 4 chiffres.")
    print("Les chiffres sont compris entre 0 et 9.")
    print("Bonne chance !")

    chaine_utilisateur = ""
    cpt = 0
    while chaine_utilisateur != chaine_a_trouver:
        chaine_a_trouver_modifiable = chaine_a_trouver
        chaine_utilisateur = input("Entrez une combinaison : ")
        if len(chaine_utilisateur) != 4:
            print("La combinaison doit contenir 4 chiffres.")
        else:
            bien_place = 0
            mal_place = 0
            for i in range(4):
                if chaine_utilisateur[i] == chaine_a_trouver_modifiable[i]:
                    bien_place += 1
                    liste_caracteres = list(chaine_a_trouver_modifiable)
                    liste_caracteres[i] = "X"
                    chaine_a_trouver_modifiable = ''.join(liste_caracteres)
            
            for i in range(4):
                if chaine_utilisateur[i] in chaine_a_trouver_modifiable and chaine_utilisateur[i] != chaine_a_trouver_modifiable[i]:
                    mal_place += 1
                    chaine_a_trouver_modifiable = chaine_a_trouver_modifiable.replace(chaine_utilisateur[i], "X", 1)

            print(f"{bien_place} bien placé(s), {mal_place} mal placé(s).")
            cpt += 1

    print("Bravo, vous avez trouvé la combinaison !")

if __name__ == '__main__':
    mastermind()