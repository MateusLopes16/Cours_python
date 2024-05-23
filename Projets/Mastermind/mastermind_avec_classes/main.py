from mastermind import Mastermind # on importe la classe Mastermind du fichier mastermind.py

if __name__ == '__main__':
    jouer = True
    while jouer:
        jeu = input("Voulez-vous jouer au Mastermind ? (o/n) ")
        if jeu.lower() != "o":
            jouer = False
        else:
            game = Mastermind()
            game.run()