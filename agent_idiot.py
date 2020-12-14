from pion import *
import random
import numpy as np
import math

TAUX_APPRENTISSAGE = 0.1

class agent_idiot():
    def __init__(self, symbole_pion):
        #mémoire des états vus et des actions faites lors de la dernière partie jouée
        self.mem_etat=[]
        self.mem_actions=[]
        self.historique_actions = []

        #couleur des pions (symbole dans notre cas)
        self.tab_pions=[]
        self.symbole_pion=symbole_pion
        self.pion_adverse = ''

        #creation d'un tableau de 4 pions
        self.creation_pion()
        self.action_possible = []

        #possibilité de jouer (perdu ou non ?)
        self.deplacement_possible=0

        self.counter_essai = 0

    def creation_pion(self):
        i = 0
        pion_pos = 0
        if self.symbole_pion == '*':
            self.pion_adverse = 'o'
            pion_pos = 0
        elif self.symbole_pion == 'o':
            self.pion_adverse = '*'
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

        for i in range(len(self.mem_etat)):
            if plateau.get_state_plateau() == self.mem_etat[i]:
                index = i   #on recupere l'etat
        #si l'etat du plateau est inconnu
        if index==-1:
            # ajout de l'etat du plateau à la memoire eds etats
            self.mem_etat.append(plateau.get_state_plateau()) 
            #print( self.mem_actions)
            self.get_actions()
        game = self.decision(index)

        if game == 1 :
            return game
        elif game == 0 : 
            return game

    #en fonction du tableau de jeu, renvoie les actions possibles pour l'agent(règles connues)
    def get_actions(self):
            probabilite = 3
            liste_proba=[]
            somme_proba = 0
            for k in range(0,36):
                somme_proba += probabilite
                liste_proba.append(probabilite)
            for k in range(0,4):
                index = random.randint(0,35)
                if liste_proba[index] != 1:
                    liste_proba[index] = 1
                elif index < len(liste_proba) :
                    index += 1
                    liste_proba[index] = 1
                else : 
                    index -= 1
                    liste_proba[index] = 1
            self.mem_actions.append(liste_proba) 
            #print(self.mem_actions)
    
    def decision(self, etat):
        if etat==-1:
            #print("On rencontre un nouvel état.")
            etat = len(self.mem_etat)-1
        
        proba=[]
        liste_index=[]
        somme=0
        #print(len(self.mem_actions[etat]))
        for i in range(len(self.mem_actions[etat])):
            proba.append(self.mem_actions[etat][i]/100)
            somme += proba[i]
            liste_index.append(i)
        
        #print("Liste des probas :",self.mem_actions[etat] )
        #print("Somme proba : ", somme)
        case_visee = np.random.choice(liste_index, 1, p = proba)[0]
        id_pion = 0
        if case_visee >= 27 :
            case_visee = case_visee - 27
            id_pion = 3
        elif case_visee >= 18 :
            case_visee = case_visee - 18
            id_pion = 2
        elif case_visee >= 9 :
            case_visee = case_visee - 9
            id_pion = 1

        #print("case_visee = ", case_visee)
        #print("id_pions = ", id_pion)
        deplacement_fait = self.deplacement(id_pion, case_visee, etat)
        print("Déplacement vaut : ", deplacement_fait)
        if deplacement_fait == 1:
            return deplacement_fait 
        elif deplacement_fait == -1:
            return deplacement_fait

        
   

    #effectue un choix dans le tableau d'actions possibles
    def deplacement(self, id_pion, case_visee, etat):
        action_possible = self.verif_regle(id_pion,case_visee, etat)
        self.counter_essai += 1 
        if self.counter_essai < 100: 
            if action_possible:
                self.tab_pions[id_pion].position = case_visee
                self.counter_essai = 0
                return 1 
                #print("Nouvelle position du pions : ", self.tab_pions[id_pion].position)
                
            else :
                self.punition(id_pion, case_visee, etat)
                self.decision(etat)
        else :
            return -1

        
    def verif_regle(self, id_pion, case_visee, etat):
        etat_plateau = self.mem_etat[etat]
        #print("Plateau de l'état : ",etat_plateau)

        #Le pions essaie de rester sur place
        #print("Pions : ", self.tab_pions)
        if self.tab_pions[id_pion].position == case_visee or etat_plateau[case_visee] != '.':
            return 0

        #Le pion est au centre 
        if self.tab_pions[id_pion].position == 8 :
            #Il essaie d'aller sur une case vide 
            if etat_plateau[case_visee] == '.' :
                return 1

        #pions sur le cercle extérieur, sauf en bout de liste
        elif self.tab_pions[id_pion].position > 0 and self.tab_pions[id_pion].position < 7:
            if case_visee == 8 : 
                if (etat_plateau[self.tab_pions[id_pion].position-1] == self.pion_adverse or etat_plateau[self.tab_pions[id_pion].position+1]== self.pion_adverse):
                    return 1
            elif case_visee == self.tab_pions[id_pion].position-1 or case_visee == self.tab_pions[id_pion].position+1 :
                return 1
            else :
                return 0

        elif self.tab_pions[id_pion].position == 0:
            if case_visee == 8 :
                if (etat_plateau[7] == self.pion_adverse or etat_plateau[self.tab_pions[id_pion].position+1]== self.pion_adverse):
                    return 1
            elif case_visee == 7 or case_visee == self.tab_pions[id_pion].position+1 :
                return 1
            else :
                return 0 
        
        elif self.tab_pions[id_pion].position == 7:
            if case_visee == 8 :
                if (etat_plateau[self.tab_pions[id_pion].position-1] == self.pion_adverse or etat_plateau[0]== self.pion_adverse):
                    return 1
            elif case_visee == self.tab_pions[id_pion].position-1 or case_visee == 0 :
                return 1
            else :
                return 0
        
    def punition(self, id_pion, case_visee, etat):
        if id_pion == 0:
            action_choisie = case_visee
        elif case_visee == 0: 
            action_choisie = id_pion * 9
        else:
            action_choisie = id_pion*case_visee

        proba=[]
        liste_index=[]
        somme=0
        #print(len(self.mem_actions[etat]))
        for i in range(len(self.mem_actions[etat])):
            proba.append(self.mem_actions[etat][i]/100)
            somme += proba[i]
            liste_index.append(i)

        #print("Somme proba : ", somme)

        index_proba_aleatoire = np.random.choice(liste_index, 1, p = proba)[0]

        modification = int(self.mem_actions[etat][action_choisie]/2)
        #print("Modification : ", modification)
        if modification == 0 and self.mem_actions[etat][action_choisie] == 1 :
            modification = 1
        self.mem_actions[etat][action_choisie] -= modification

        if index_proba_aleatoire != action_choisie:
            self.mem_actions[etat][index_proba_aleatoire] += modification

        else : 
            index_proba_aleatoire += 1 
            self.mem_actions[etat][index_proba_aleatoire] += modification



    def recompense(self,gagné):
        #print("recompense")
        #On parcourt l'historique
        """for i in range(len(self.historique_actions)-1,-1,-1) :
            modification = int((i/len(self.historique_actions))*(TAUX_APPRENTISSAGE)*self.mem_actions[self.historique_actions[i][0]][1][self.historique_actions[i][1]])
            #print("iteration", i)
            #print("valeur de la modification", modification)
            #print("proba avant modif", self.mem_actions[self.historique_actions[i][0]][1])
            nb_action = 0

            for k in range(0,4):
              self.mem_actions[self.historique_actions[i][0]][1][k] = int(self.mem_actions[self.historique_actions[i][0]][1][k])

            for k in range(0,4):
                if  self.mem_actions[self.historique_actions[i][0]][1][k] < 0:
                    self.mem_actions[self.historique_actions[i][0]][1][k] = 0

            #print("proba castée", self.mem_actions[self.historique_actions[i][0]][1])

            #On compte le nombre d'actions possibles
            for y in range(len(self.mem_actions[self.historique_actions[i][0]][0])):
                if self.mem_actions[self.historique_actions[i][0]][0][y] != -1 and self.historique_actions[i][1] != y:
                    nb_action+=1

            if nb_action!=0:
                # Augmentation de la probba de l'action choisi a l'index i de l'historique
                if gagné==1:
                    self.mem_actions[self.historique_actions[i][0]][1][self.historique_actions[i][1]] += modification
                elif gagné==0:
                    self.mem_actions[self.historique_actions[i][0]][1][self.historique_actions[i][1]] -= modification

                #verification que la proba augmentée ne soit pas supérieure à 100
                offset=0
                if gagné==1:
                    if self.mem_actions[self.historique_actions[i][0]][1][self.historique_actions[i][1]] > 95 :
                        offset = self.mem_actions[self.historique_actions[i][0]][1][self.historique_actions[i][1]] - 95
                        self.mem_actions[self.historique_actions[i][0]][1][self.historique_actions[i][1]] = 95
                elif gagné==0:
                    if self.mem_actions[self.historique_actions[i][0]][1][self.historique_actions[i][1]] < 5 :
                        offset = 5 - self.mem_actions[self.historique_actions[i][0]][1][self.historique_actions[i][1]]
                        self.mem_actions[self.historique_actions[i][0]][1][self.historique_actions[i][1]] = 5

                # Parcours des proba des actions pour les diminuer
                for y in range(len(self.mem_actions[self.historique_actions[i][0]])):
                    if y != self.historique_actions[i][1] and self.mem_actions[self.historique_actions[i][0]][0][y] != -1  :
                        if gagné==1:
                            self.mem_actions[self.historique_actions[i][0]][1][y] -= int((modification - offset)/nb_action)
                        elif gagné==0:
                            self.mem_actions[self.historique_actions[i][0]][1][y] -= int((modification - offset) / nb_action)
                #print("proba Apres modif", self.mem_actions[self.historique_actions[i][0]][1])

                for k in range(0, 4):
                    if self.mem_actions[self.historique_actions[i][0]][1][k] < 0:
                        self.mem_actions[self.historique_actions[i][0]][1][k] = 0
                
                somme_proba = 0
                proba_max = 0
                proba_min = 100
                indice_proba_max = -1
                indice_proba_min = -1
                for y in range(len(self.mem_actions[self.historique_actions[i][0]][1])):
                    somme_proba += self.mem_actions[self.historique_actions[i][0]][1][y]

                if somme_proba != 100 :
                    #print("liste actions :", self.mem_actions[self.historique_actions[i][0]][1])
                    for y in range(len(self.mem_actions[self.historique_actions[i][0]][1])):
                        if self.mem_actions[self.historique_actions[i][0]][1][y] > 0 and self.mem_actions[self.historique_actions[i][0]][0][y] != -1:
                            #print("On a une action possible dont la proba n'est pas 0 :", self.mem_actions[self.historique_actions[i][0]][1][y])

                            # On cherche la plus grande proba
                            if self.mem_actions[self.historique_actions[i][0]][1][y] > proba_max and self.mem_actions[self.historique_actions[i][0]][1][y] < 100 and self.historique_actions[i][1] != y: 
                                proba_max = self.mem_actions[self.historique_actions[i][0]][1][y] 
                                indice_proba_max = y 
                                #print("proba max  = ", proba_max)
                                #print("Son index  = ", indice_proba_max)

                            # On cherche la plus petite proba
                            if self.mem_actions[self.historique_actions[i][0]][1][y] < proba_min and self.mem_actions[self.historique_actions[i][0]][1][y] > 0 :
                                proba_min = self.mem_actions[self.historique_actions[i][0]][1][y]
                                indice_proba_min = y 
                                #print("proba min  = ", proba_min)
                                #print("Son index  = ", indice_proba_min)
                    
                if indice_proba_max != -1 and somme_proba > 100 :
                    self.mem_actions[self.historique_actions[i][0]][1][indice_proba_max] -= int(somme_proba - 100)
                    #print("proba max  = ", proba_max)
                    #print("Son index  = ", indice_proba_max)
                    #print("On dépasse 100 : ", self.mem_actions[self.historique_actions[i][0]][1][indice_proba_max])

                if indice_proba_min != -1 and somme_proba < 100 :
                    self.mem_actions[self.historique_actions[i][0]][1][indice_proba_min] += int(100 - somme_proba)
                    #print("proba min  = ", proba_min)
                    #print("Son index  = ", indice_proba_min)
                    #print("On dépasse 100 : ", self.mem_actions[self.historique_actions[i][0]][1][indice_proba_min])
                
                #print("proba apres verif", self.mem_actions[self.historique_actions[i][0]][1])

            else :
                somme_proba = 0
                for y in range(len(self.mem_actions[self.historique_actions[i][0]][1])):
                    somme_proba += self.mem_actions[self.historique_actions[i][0]][1][y]
                if somme_proba == 0 :
                    for y in range(0,4):
                        if self.mem_actions[self.historique_actions[i][0]][0][y] != -1 :
                            self.mem_actions[self.historique_actions[i][0]][1][y] = 100"""
