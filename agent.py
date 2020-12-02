from pion import *

class agent():
    def __init__(self, symbole_pion):
        self.tab_etat=[]
        self.tab_pions=[]
        self.action_possible = []
        self.historique=[]
        self.symbole_pion=symbole_pion
        self.creation_pion(self.symbole_pion)            

    def creation_pion(self, symbole_pion):
        i = 0
        if symbole_pion == '*':
            position = 0
        elif symbole_pion == 'o':
            position = 5
        while i < 4:
            self.tab_pions.append(pion(symbole_pion, position))
            position += 1
            i += 1
    
    def get_actions(self, plateau):
        i = 0
        y = 0
        for i in range (len(self.tab_pions)):
            voisins = self.tab_pions[i].voisins(plateau)
            for y in range (len(voisins)):
                self.action_possible.append(voisins[y])
        print(self.action_possible)