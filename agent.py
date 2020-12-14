from pion import *
import random
import numpy as np
import math

TAUX_APPRENTISSAGE = 0.10

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
            #self.recompense()
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
            
        prob=int(100/(4-Nactions))
        choix=0

        #si l'etat est nouveau, on récupère la dernière valeur entrée dans le tableau
        somme_prob = 0
        
        if etat==-1:
            #print("On rencontre un nouvel état.")
            etat = len(self.mem_etat)-1
            
            for i in range(0,4):
                # Si le pion a une action possible 
                if (self.mem_actions[etat][0][i]!=-1):
                    self.mem_actions[etat][1][i] = prob

            #self.mem_actions[etat][1][random.randint(0,3)] += 1 - somme_prob

        sum=0
        prob=100
        indice = -1
        for i in range(len(self.mem_actions[etat][1])):
            sum+=self.mem_actions[etat][1][i]
            if self.mem_actions[etat][1][i]<prob and self.mem_actions[etat][1][i]>0:
                prob = self.mem_actions[etat][1][i]
                indice = i
        
        self.mem_actions[etat][1][indice]+=100-sum

        print("mem_actions",self.mem_actions[etat])
        # Sélection de l'action grace a sa probabilité
        #print("L'erreur est la : ", self.mem_actions[etat][1])
        proba=[]
        for i in range(len(self.mem_actions[etat][1])):
            proba.append(self.mem_actions[etat][1][i]/100)
        #print("proba ", proba)
        choix = np.random.choice([0,1,2,3], 1, p = proba)[0]

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
        #On parcourt l'historique
        for i in range(len(self.historique_actions)-1,-1,-1) :
            modification = int((i/len(self.historique_actions))*(TAUX_APPRENTISSAGE)*self.mem_actions[self.historique_actions[i][0]][1][self.historique_actions[i][1]])
            nb_action = 0

            for y in range(len(self.mem_actions[self.historique_actions[i][0]])):
                if self.mem_actions[self.historique_actions[i][0]][y] != -1 :
                    nb_action += 1 

            # Augmentation de la probba de l'action choisi a l'index i de l'historique
            self.mem_actions[self.historique_actions[i][0]][1][self.historique_actions[i][1]] += modification

            offset=0
            if self.mem_actions[self.historique_actions[i][0]][1][self.historique_actions[i][1]] > 100 :
                offset = self.mem_actions[self.historique_actions[i][0]][1][self.historique_actions[i][1]] - 100
                self.mem_actions[self.historique_actions[i][0]][1][self.historique_actions[i][1]] = 100

            # Parcours des proba des actions pour 
            for y in range(len(self.mem_actions[self.historique_actions[i][0]])):
                if y != self.historique_actions[i][1] :
                    self.mem_actions[self.historique_actions[i][0]][1][y] -= int((modification - offset)/nb_action)

            sum=0
            prob_min=100
            indice_min = -1
            prob_max=0
            indice_max = -1
            for y in range(len(self.mem_actions[self.historique_actions[i][0]][1])):
                sum+=self.mem_actions[self.historique_actions[i][0]][1][y]
                if self.mem_actions[self.historique_actions[i][0]][1][y] < prob_min and self.mem_actions[self.historique_actions[i][0]][1][y] > 0 :
                    prob_min = self.mem_actions[self.historique_actions[i][0]][1][y]
                    indice_min = i
                if self.mem_actions[self.historique_actions[i][0]][1][y] > prob_max and self.mem_actions[self.historique_actions[i][0]][1][y] < 100:
                    prob_max = self.mem_actions[self.historique_actions[i][0]][1][y]
                    indice_max = i
            print("indice max :", indice_max)
            print("indice min :", indice_min)
            print("self.mem_actions[self.historique_actions[i][0]][1]", self.mem_actions[self.historique_actions[i][0]][1])
            print("sum", sum)
            print("offset", offset)
            if indice_min != -1 or indice_max!=-1:
                if sum < 100:
                    self.mem_actions[self.historique_actions[i][0]][1][indice_min]+=100-sum
                else :
                    self.mem_actions[self.historique_actions[i][0]][1][indice_max]+=100-sum
            

            


        """for i in range(len(self.historique_actions)-1,-1,-1) :
            liste_indice_actions = []
            offset = 0
            #Calcul ajout valeur propa
            modification = self.round_up((i/len(self.historique_actions))*(1/10)*self.mem_actions[self.historique_actions[i][0]][1][self.historique_actions[i][1]],3)
            
            #Modification de la probabilité de l'action choisie a l'état i de l'historique en s'assurant de ne pas dépasser une valeur
            if self.mem_actions[self.historique_actions[i][0]][1][self.historique_actions[i][1]]+ modification > 1 :
                offset = self.mem_actions[self.historique_actions[i][0]][1][self.historique_actions[i][1]] - 1
                self.mem_actions[self.historique_actions[i][0]][1][self.historique_actions[i][1]] = 1
            else :
                self.mem_actions[self.historique_actions[i][0]][1][self.historique_actions[i][1]] = self.round_up(modification + self.mem_actions[self.historique_actions[i][0]][1][self.historique_actions[i][1]], 3)

            #Récupération des indices des autres actions possibles
            for k in range(len(self.mem_actions[self.historique_actions[i][0]])):
                if self.mem_actions[self.historique_actions[i][0]][0][k] != -1 :
                    liste_indice_actions.append(k)

            # Si liste indice action vide on a pas de proba a modifié
            if liste_indice_actions != []:
                # Parcours des actions non réalisée
                for indice in liste_indice_actions:
                    #Modification de la probabilité des actions non choisie a l'état i de l'historique en s'assurant de ne pas dépasser une valeur
                    if self.mem_actions[self.historique_actions[i][0]][1][self.historique_actions[i][1]]+ modification < 0 :
                        offset = 0 - self.mem_actions[self.historique_actions[i][0]][1][self.historique_actions[i][1]]
                        self.mem_actions[self.historique_actions[i][0]][1][self.historique_actions[i][1]] = 0
                    else :
                        self.mem_actions[self.historique_actions[i][0]][1][indice] = self.round_up(self.mem_actions[self.historique_actions[i][0]][1][indice] - ((modification - offset) / len(liste_indice_actions)),3)
            
            somme_prob = 0
            
            while somme_prob != 1:
                y = 0
                for y in range(0,3):
                    somme_prob += self.mem_actions[self.historique_actions[i][0]][1][y]
                    print("AHHHHHHHHHHHHHHHHHHHHHH", self.mem_actions[self.historique_actions[i][0]][1][y])
                    print("Somme for : ", somme_prob)
                
                indice_proba = random.randint(0,3)
                if self.mem_actions[self.historique_actions[i][0]][1][indice_proba]+(1-somme_prob) > 1 :
                    self.mem_actions[self.historique_actions[i][0]][1][indice_proba] -= 1 - somme_prob
                else :
                    self.mem_actions[self.historique_actions[i][0]][1][indice_proba] += 1 - somme_prob
            
            print("Nouvelles proba : ", self.mem_actions[self.historique_actions[i][0]][1])"""


