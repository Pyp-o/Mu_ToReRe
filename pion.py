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
        tab_position = []
        state_plateau = plateau.get_state_plateau()
        #print(state_plateau)
        #print(self.position)

        if self.position == 8 :
            for i in range (len(state_plateau)):
                if state_plateau[i] == '.' :
                    tab_position.append(i)
            return tab_position

        elif self.position > 0 and self.position < 7:
            if state_plateau[self.position-1] == '.' :
                tab_position.append(self.position-1)
            if state_plateau[self.position+1]== '.' :
                tab_position.append(self.position+1)
                
            if state_plateau[self.position-1] == self.pion_adverse  or state_plateau[self.position+1]== self.pion_adverse:
                if state_plateau[8] == '.' :
                    tab_position.append(8)
                return tab_position
            return tab_position

        if self.position == 0 :
            if state_plateau[7] == '.' :
                tab_position.append(7)
            if state_plateau[1]== '.' :
                tab_position.append(1)

            if state_plateau[7] == self.pion_adverse or state_plateau[1] == self.pion_adverse:
                if state_plateau[8] == '.' :
                    tab_position.append(8)
                return tab_position
            return tab_position

        if self.position == 7 :
            if state_plateau[0] == '.' :
                tab_position.append(0)
            if state_plateau[6]== '.' :
                tab_position.append(6)
            if state_plateau[0] == self.pion_adverse or state_plateau[6] == self.pion_adverse :
                if state_plateau[8] == '.' :
                    tab_position.append(8)
                return tab_position
            return tab_position