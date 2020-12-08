from agent import *

class plateau():
    def __init__(self):
        self.state_plateau = ['.','.','.','.','.','.','.','.','.']
        self.game = 0


    def get_state_plateau(self):
        return self.state_plateau

    def affichage_plateau(self):
        print("    "+str(self.state_plateau[2])+"    ")
        print("  "+str(self.state_plateau[1])+"   "+str(self.state_plateau[3])+"  ")
        print(str(self.state_plateau[0])+"   "+str(self.state_plateau[8])+"   "+str(self.state_plateau[4]))
        print("  "+str(self.state_plateau[7])+"   "+str(self.state_plateau[5])+"  ")
        print("    "+str(self.state_plateau[6])+"    ")
        print("")

    # met a jour le plateau en allant chercher tous les pions des agents et leur position.
    def update_plateau(self, agent_noir, agent_blanc):
        #reset plateau
        self.state_plateau=['.','.','.','.','.','.','.','.','.']
        for i in range(0, 4):
            self.state_plateau[agent_noir.tab_pions[i].position] = agent_noir.symbole_pion
            self.state_plateau[agent_blanc.tab_pions[i].position] = agent_blanc.symbole_pion
        self.affichage_plateau()