class Interface:
    def __init__(self) -> None:
        pass

    def afficher_accueil(self):
        print("\033[0mBienvenue dans le jeu du Mastermind !")
        print("\033[0mTrouvez la combinaison à 4 chiffres. Vous avez 10 essais.")
        print("\033[0mLes chiffres sont compris entre 0 et 9.")
        print("\033[0mBonne chance !")

    def demander_combinaison(self):
        return input("\033[0mEntrez une combinaison : \033[92m")
    
    def afficher_resultat(self, bien_place, mal_place):
        print(f"\033[0m{bien_place} bien placé(s), {mal_place} mal placé(s).")
    
    def afficher_victoire(self, cpt):
        print(f"\033[0mBravo, vous avez trouvé la combinaison en {cpt} coups !")
    
    def afficher_defaite(self, chaine_a_trouver):
        print(f"\033[0mPerdu, la combinaison était \033[91m{chaine_a_trouver}\033[0m.")
    
    def afficher_fin(self):
        print("\033[0mMerci d'avoir joué au Mastermind !")

    def afficher_erreur(self):
        print("\033[0mLa combinaison doit contenir 4 chiffres.")
