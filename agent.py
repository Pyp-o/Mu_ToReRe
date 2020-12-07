from pion import *
import random

class agent():
    def __init__(self, symbole_pion):
        self.tab_etat=[]
        self.tab_pions=[]
        self.action_possible = []
        self.historique=[]
        self.deplacement_possible=0

        random.seed()

        self.symbole_pion=symbole_pion
        self.creation_pion(self.symbole_pion)            

    def creation_pion(self, symbole_pion):
        i = 0
        if symbole_pion == '*':
            position = 0
        elif symbole_pion == 'o':
            position = 4
        while i < 4:
            self.tab_pions.append(pion(symbole_pion, position))
            position += 1
            i += 1
    
    def play(self, plateau):
        self.get_actions(plateau)
        if self.deplacement_possible == 1:
            self.deplacement()

    def get_actions(self, plateau):
        i = 0
        y = 0
        for id_pions in range(len(self.tab_pions)):
            case_vide = self.tab_pions[id_pions].voisins(plateau)
            if case_vide != [] :
                self.action_possible.append([id_pions,case_vide])
            self.deplacement_possible = 1
        if self.action_possible == [] :
            print("fin de partie")
            plateau.game = 0
            self.deplacement_possible = 0            

    def deplacement(self):
        index_random = random.randrange(len(self.action_possible))
        self.tab_pions[self.action_possible[index_random][0]].position = self.action_possible[index_random][1][0]
        self.action_possible=[]