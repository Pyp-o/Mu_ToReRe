from pion import *
import random



class agent():
    def __init__(self, symbole_pion):
        #mémoire des états vus et des actions faites lors de la dernière partie jouée
        self.mem_etat=[]
        self.mem_actions=[]
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
        index = -1 #l'index d'un tableau ne peut être négatif, on s'assure de ne pas avoir de problème pour détecter un nouvel état
        for i in range(len(self.mem_etat)):
            if plateau.get_state_plateau == self.mem_etat[i]:
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
            case_vide = self.tab_pions[i].voisins(plateau)
            self.action_possible.append(case_vide)
            self.deplacement_possible = 1

        #si aucune action n'est possible, la partie est perdue
        Nactions = 0
        print("self.action_possible", self.action_possible)
        for i in range(len(self.action_possible)):
            if self.action_possible[i] == [] :
                Nactions +=1
        print("Nactions", Nactions)
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
    def deplacement(self, etat):
        prob=0.0
        choix=0

        #si l'etat est nouveau on récupère la dernière valeur entrée dans le tableau
        if etat==-1:
            etat = len(self.mem_etat)-1

        for i in range(0,4):
            #print("self.mem_actions[etat][1][i]", self.mem_actions[etat][1][i])
            if (self.mem_actions[etat][0][i]!=[]):
                if (self.mem_actions[etat][1][i]+(random.randrange(-10,10)/10))>prob:
                    prob=self.mem_actions[etat][1][i]
                    choix=i
                    print("choix in for loop", choix)

        """print("choix",choix)
        print("mem etat", self.mem_etat)
        print("mem actions", self.mem_actions[etat][0][choix])"""
        #try:
        print("self.mem_actions[etat][0]", self.mem_actions[etat][0])
        print("choix", choix)
        try:
            self.tab_pions[choix].position = self.mem_actions[etat][0][choix][0]
            self.historique_actions.append([etat, choix])
            self.action_possible=[]
        except:
            self.action_possible = []
            print("")








        ############ ancienne fonction de déplacement ############

        """# effectue un choix dans le tableau d'actions possibles
        def deplacement(self, index):
            index_random = random.randrange(len(self.action_possible))
            # tant que l'on a pas un indice indcant une position correcte
            while (self.action_possible[index_random] == []):
                index_random = random.randrange(len(self.action_possible))

            self.action_possible[index_random][0] le dernier [0] permet d'extraire la valeur du tableau et d'éviter des bugs par la suite
            n'est pas gênant, une seule position ne peut être contenu dans ce tableau

            self.tab_pions[index_random].position = self.action_possible[index_random][0]
            self.action_possible = []"""