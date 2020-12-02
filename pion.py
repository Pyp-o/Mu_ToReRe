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
        #print(state_plateau)
        #print(self.position)
        if self.position == 8 :
            for i in range (len(state_plateau)):
                if state_plateau[i] == self.pion_adverse :
                    self.tab_voisin.append(1)
                else :
                    self.tab_voisin.append(0)
            #print("premier if :", self.tab_voisin)
            return self.tab_voisin

        elif self.position > 0 and self.position < 7:
            if state_plateau[self.position-1] == self.pion_adverse :
                self.tab_voisin.append(1)
            if state_plateau[self.position+1]== self.pion_adverse :
                self.tab_voisin.append(1)
            if state_plateau[8] == self.pion_adverse :
                self.tab_voisin.append(1)
            #print("deuxieme if :", self.tab_voisin)
            return self.tab_voisin

        if self.position == 0 :
            if state_plateau[7] == self.pion_adverse :
                self.tab_voisin.append(1)
            if state_plateau[1] == self.pion_adverse :
                self.tab_voisin.append(1)
            if state_plateau[8] == self.pion_adverse :
                self.tab_voisin.append(1)
            #print("troisieme if :", self.tab_voisin)
            return self.tab_voisin

        if self.position == 7 :
            if state_plateau[0] == self.pion_adverse :
                self.tab_voisin.append(1)
            if state_plateau[6] == self.pion_adverse :
                self.tab_voisin.append(1)
            if state_plateau[8] == self.pion_adverse :
                self.tab_voisin.append(1)
            #print("4ieme if :", self.tab_voisin)
            return self.tab_voisin