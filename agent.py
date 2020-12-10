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
        game = self.get_actions(plateau)
        if self.deplacement_possible == 1:
            self.deplacement()
        return game

    #en fonction du tableau de jeu, renvoie les actions possibles pour l'agent(règles connues)
    def get_actions(self, plateau):
        for i in range(len(self.tab_pions)):
            case_vide = self.tab_pions[i].voisins(plateau)
            self.action_possible.append(case_vide)
            self.deplacement_possible = 1

        #si aucune action n'est possible, la partie est perdue
        Nactions = 0
        for i in range(len(self.action_possible)):
            if self.action_possible[i] == [] :
                Nactions +=1
        if Nactions==4:
            print("fin de partie")
            #met fin à la partie pour le plateau
            plateau.game = 0
            # met fin à la partie pour l'agent également
            self.deplacement_possible = 0
            return 0
        else :
            return 1

    #effectue un choix dans le tableau d'actions possibles
    def deplacement(self):
        index_random = random.randrange(len(self.action_possible))
        #tant que l'on a pas un indice indcant une position correcte
        while(self.action_possible[index_random]==[]):
            index_random = random.randrange(len(self.action_possible))

        #self.action_possible[index_random][0] le dernier [0] permet d'extraire la valeur du tableau et d'éviter des bugs par la suite
        #n'est pas gênant, une seule position ne peut être contenu dans ce tableau
        self.tab_pions[index_random].position = self.action_possible[index_random][0]
        self.action_possible=[]