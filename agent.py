from pion import *
import random

class agent():
    def __init__(self, symbole_pion):
        #mémoire des états vus et des actions faites lors de la dernière partie jouée
        self.tab_etat=[]
        self.historique_actions = []

        #couleur des pions (symbole dans notre cas)
        self.symbole_pion=symbole_pion

        #creation d'un tableau de 4 pions
        self.tab_pions = self.creation_pion(self.symbole_pion)
        self.action_possible = []

        #possibilité de jouer (perdu ou non ?)
        self.deplacement_possible=0

    def creation_pion(self, symbole_pion):
        i = 0
        tab_pions = []
        if symbole_pion == '*':
            position = 0
        elif symbole_pion == 'o':
            position = 4
        while i < 4:
            tab_pions.append(pion(symbole_pion, position))
            position += 1
            i += 1
        return tab_pions

    #recupere le plateau de jeu, et choisit une action
    def play(self, plateau):
        self.get_actions(plateau)
        if self.deplacement_possible == 1:
            self.deplacement()

    #en fonction du tableau de jeu, renvoie les actions possibles pour l'agent(règles connues)
    def get_actions(self, plateau):
        for id_pions in range(len(self.tab_pions)):
            case_vide = self.tab_pions[id_pions].voisins(plateau)
            if case_vide != [] :
                self.action_possible.append([id_pions,case_vide])
            self.deplacement_possible = 1
        #si aucune action n'est possible, la partie est perdue
        if self.action_possible == [] :
            print("fin de partie")
            #met fin à la partie pour le plateau
            plateau.game = 0
            # met fin à la partie pour l'agent également
            self.deplacement_possible = 0

    #effectue un choix dans le tableau d'actions possibles
    def deplacement(self):
        index_random = random.randrange(len(self.action_possible))
        self.tab_pions[self.action_possible[index_random][0]].position = self.action_possible[index_random][1][0]
        self.action_possible=[]