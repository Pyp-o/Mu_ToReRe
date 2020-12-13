from pion import *
import random
import numpy as np


class agent():
    def __init__(self, symbole_pion):
        #mémoire des états vus et des actions faites lors de la dernière partie jouée
        self.mem_etat=[]
        self.mem_actions=[]
        self.historique_actions = []

        #couleur des pions (symbole dans notre cas)
        self.tab_pions=[]
        self.symbole_pion=symbole_pion

        #creation d'un tableau de 4 pions
        self.creation_pion()
        self.action_possible = []

        #possibilité de jouer (perdu ou non ?)
        self.deplacement_possible=0

    def creation_pion(self):
        i = 0
        pion_pos = 0
        if self.symbole_pion == '*':
            pion_pos = 0
        elif self.symbole_pion == 'o':
            pion_pos = 4
        
        while i < 4:
            self.tab_pions.append(pion(self.symbole_pion, pion_pos))
            pion_pos += 1
            i += 1
    
    def reset_pions(self):
        # On garde les objects pions précédemment utilisé et on les remet a la position initiale.
        i = 0
        pion_pos = 0
        self.deplacement_possible = 1
        
        if self.symbole_pion == '*':
            pion_pos = 0
        elif self.symbole_pion == 'o':
            pion_pos = 4

        for pions in self.tab_pions :
            pions.position = pion_pos
            pion_pos += 1
        
        
    #recupere le plateau de jeu, et choisit une action
    def play(self, plateau):
        game = 1
        index = -1 #l'index d'un tableau ne peut être négatif, on s'assure de ne pas avoir de problème pour détecter un nouvel état
        #print("état plateau : ", plateau.get_state_plateau())
        #print("état mémoire : ",self.mem_etat)
        for i in range(len(self.mem_etat)):
            if plateau.get_state_plateau() == self.mem_etat[i]:
                index = i   #on recupere l'etat
        #si l'etat du plateau est inconnu
        if index==-1:
            # ajout de l'etat du plateau à la memoire eds etats
            self.mem_etat.append(plateau.get_state_plateau())
            game = self.get_actions(plateau)
            #on ajoute à la mémoire des actions les actions et on initialise les probabilités à 0
            self.mem_actions.append([self.action_possible, [0.0,0.0,0.0,0.0]])            

        #on fait appel à la fonction de choix de déplacement
        if self.deplacement_possible == 1:
            self.deplacement(index)
        return game

    #en fonction du tableau de jeu, renvoie les actions possibles pour l'agent(règles connues)
    def get_actions(self, plateau):
        for i in range(len(self.tab_pions)):
            #print(self.action_possible)
            self.action_possible.append(self.tab_pions[i].voisins(plateau))
            #print("Déplacement possible sur : ", self.action_possible[-1])
            self.deplacement_possible = 1

        #si aucune action n'est possible, la partie est perdue
        Nactions = 0
        #print("self.action_possible", self.action_possible)
        for i in range(len(self.action_possible)):
            if self.action_possible[i] == -1 :
                Nactions +=1
        #print("Nactions", Nactions)
        if Nactions==4:
            #met fin à la partie pour le plateau
            plateau.game = 0
            # met fin à la partie pour l'agent également
            self.deplacement_possible = 0
            self.action_possible=[]
            self.recompense()
            return(0)
        else :
            return(1)

    #effectue un choix dans le tableau d'actions possibles
    def deplacement(self, etat):
        #print("C'est a moi de jouer : ", self.symbole_pion)
        Nactions = 4
        print("actions possibles : ", self.mem_actions[etat][0])
        for elem in self.mem_actions[etat][0]:
            if elem != -1 :
                Nactions -= 1
        
        if Nactions == 4 :
            return
            
        prob=1/(4-Nactions)
        choix=0

        #si l'etat est nouveau, on récupère la dernière valeur entrée dans le tableau
        if etat==-1:
            #print("On rencontre un nouvel état.")
            etat = len(self.mem_etat)-1
            for i in range(0,4):
                # Si le pion a une action possible 
                if (self.mem_actions[etat][0][i]!=-1):
                    self.mem_actions[etat][1][i] = prob


        # Sélection de l'action grace a sa probabilité
        choix = np.random.choice([0,1,2,3], 1, p = self.mem_actions[etat][1])[0]

        #print("Choix : ", choix)
        #print("mem etat", self.mem_etat)

        #print("Position pion : ",self.tab_pions[3].position)
        #print("Case disponible : ", self.mem_actions[etat][0][choix])

        #print("On regarde a cet indice de la mémoire : ", etat)


        #print("Position de base ; ",self.tab_pions[choix].position)
        self.tab_pions[choix].position = self.mem_actions[etat][0][choix]
        #print("Position aprés déplacement ; ",self.tab_pions[choix].position)

        self.historique_actions.append([etat, choix])
        #print("historique : ", self.historique_actions)
        self.action_possible=[]
            
    def recompense(self):
        print("recompense")
        #On parcour la liste dans le sens décroissant des indices.           
        for i in range(len(self.historique_actions)-1,-1,-1) :
            total_proba = 0
            #On modifie les probas des actions que l'agent a entreprit
            modification = (i/len(self.historique_actions))*(1/10)*self.mem_actions[self.historique_actions[i][0]][1][self.historique_actions[i][1]]
            #on parcourt les listes de proba
            action_possible=0
            for k in range(len(self.mem_actions[self.historique_actions[i][0]])):

                if self.mem_actions[self.historique_actions[i][0]][0][k] != -1 :
                    action_possible += 1
            
            if action_possible == 0:
                action_possible = 1

            modification = round(modification / action_possible,5)
            for y in range(4):
                #les autres actions on reduit leurs proba
                if self.historique_actions[i][1] != y :
                    if self.mem_actions[self.historique_actions[i][0]][1][y] - modification > 0.05:
                        self.mem_actions[self.historique_actions[i][0]][1][y] = round(self.mem_actions[self.historique_actions[i][0]][1][y] - modification,5)
                        total_proba += self.mem_actions[self.historique_actions[i][0]][1][y]
                        #print("Proba diminuée : ", self.mem_actions[self.historique_actions[i][0]][1][y] - modification)

                else :
                    if 1 - total_proba < 0.95 :
                        self.mem_actions[self.historique_actions[i][0]][1][self.historique_actions[i][1]] = round(1 - total_proba,5)
                        #print("proba complémentaire :", (1 - total_proba))
                #L'action qui a été choisit prend la valeur (1 - (la somme de ce que l'on a enlevé))
            print("Nouvelles proba :", self.mem_actions[self.historique_actions[i][0]][1])

