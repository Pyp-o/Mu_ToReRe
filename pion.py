class pion():
    def __init__(self, symbole_pion, position):
        self.position = position
        self.tab_action = []
        self.tab_voisin = []

        if symbole_pion == 'o':
            self.pion_adverse = '*'
        else :
            self.pion_adverse = 'o'

    def voisins(self, plateau):
        state_plateau = plateau.get_state_plateau()
        tab_position = -1
        #en utilisant une liste pour représenter le tableau de jeu, il faut utiliser des tests différents pour la position des pions
        #pion au centre
        if self.position == 8 :
            for i in range (len(state_plateau)):
                if state_plateau[i] == '.' :
                    tab_position=i
                    #une seule position est disponible, on la retourne dès qu'on l'a trouvée
                    return tab_position
            return tab_position

        #pions sur le cercle extérieur, sauf en bout de liste
        elif self.position > 0 and self.position < 7:
            if state_plateau[self.position-1] == '.' :
                tab_position=self.position-1
            if state_plateau[self.position+1]== '.' :
                tab_position=self.position+1
                
            if state_plateau[self.position-1] == self.pion_adverse  or state_plateau[self.position+1]== self.pion_adverse:
                if state_plateau[8] == '.' :
                    tab_position=8
                return tab_position
            return tab_position

        #pion en premiere position de liste
        elif self.position == 0 :
            if state_plateau[7] == '.' :
                tab_position=7
            if state_plateau[1]== '.' :
                tab_position=1

            if state_plateau[7] == self.pion_adverse or state_plateau[1] == self.pion_adverse:
                if state_plateau[8] == '.' :
                    tab_position=8
                return tab_position
            return tab_position

        #pion en derniere position de liste
        elif self.position == 7 :
            if state_plateau[0] == '.' :
                tab_position=0
            if state_plateau[6]== '.' :
                tab_position=6
            if state_plateau[0] == self.pion_adverse or state_plateau[6] == self.pion_adverse :
                if state_plateau[8] == '.' :
                    tab_position=8
                return tab_position
            return tab_position