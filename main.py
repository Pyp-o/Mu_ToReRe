# '*' pions noirs
# 'o' pions blancs
# '.' case vide

def affichage_plateau(state_plateau, round_number):
    print("------------------------------------------\nround number :", round_number)
    print("    "+str(state_plateau[2])+"\n"+
          "  "+str(state_plateau[1])+"   "+str(state_plateau[3])+"\n"+
          str(state_plateau[0])+"   "+str(state_plateau[8])+"   "+str(state_plateau[4])+"\n"+
          "  "+str(state_plateau[7])+"   "+str(state_plateau[5])+"\n"+
          "    "+str(state_plateau[6]))





if __name__ == "__main__":
    state_plateau=['*','*','*','*','o','o','o','o','.']
    affichage_plateau(state_plateau, 0)
