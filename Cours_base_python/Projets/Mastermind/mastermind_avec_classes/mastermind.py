import random
from Interface import Interface

# Définition de la classe Mastermind
class Mastermind:
    # Méthode d'initialisation de la classe
    def __init__(self):
        # Génération de la combinaison à trouver, composée de 4 chiffres aléatoires
        self.chaine_a_trouver = ""
        for i in range(4):
            self.chaine_a_trouver += str(random.randint(0, 9))
        self.cpt = 0
        self.interface = Interface()

    # Méthode pour exécuter le jeu
    def run(self):
        self.interface.afficher_accueil()
        trouver = False
        # on continuer tant qu'on a pas trouver ou tant que le nombre de tours est inférieur à 10
        while not trouver and self.cpt < 10:
            trouver = self.nouveau_tour()

        # Vérification du résultat du jeu
        if trouver:
            self.interface.afficher_victoire(self.cpt)
        else:

            self.interface.afficher_defaite(self.chaine_a_trouver)
        
        # Affichage de l'écran de fin
        self.interface.afficher_fin()

    # Méthode pour un nouveau tour de jeu
    def nouveau_tour(self):
        # Demande de la combinaison à l'utilisateur
        chaine_utilisateur = self.interface.demander_combinaison()
       
        if len(chaine_utilisateur) != 4:
            self.interface.afficher_erreur()
        else:
            # Appel des méthodes pour vérifier les éléments bien placés et mal placés
            nouvelle_chaine, bien_place = self.verifie_elements_bien_places(chaine_utilisateur)
            mal_place = self.verifie_elements_mal_place(chaine_utilisateur, nouvelle_chaine)

            self.interface.afficher_resultat(bien_place, mal_place)
            self.cpt += 1

    # Méthode pour vérifier les éléments bien placés dans la combinaison de l'utilisateur
    def verifie_elements_bien_places(self, chaine_utilisateur):
        bien_place = 0
        chaine_retour = self.chaine_a_trouver
        for i in range(4):
            # Si le caractère est bien placé, on incrémente le compteur et on remplace le caractère par un X
            if chaine_utilisateur[i] == chaine_retour[i]:
                bien_place += 1
                liste_caracteres = list(chaine_retour)
                liste_caracteres[i] = "X"
                chaine_retour = ''.join(liste_caracteres)
        return chaine_retour, bien_place

    # Méthode pour vérifier les éléments mal placés dans la combinaison de l'utilisateur
    def verifie_elements_mal_place(self, chaine_utilisateur, chaine_de_recherche):
        mal_place = 0
        for i in range(4):
            # Si le caractère est mal placé, on incrémente le compteur et on remplace le caractère par un X
            if chaine_utilisateur[i] in chaine_de_recherche and chaine_utilisateur[i] != chaine_de_recherche[i]:
                mal_place += 1
                chaine_de_recherche = chaine_de_recherche.replace(chaine_utilisateur[i], "X", 1)
        return mal_place
