# '*' pions noirs
# 'o' pions blancs
# '.' cae vide

def affichage_plateau(state_plateau):
    print("    "+str(state_plateau[2])+"    ")
    print("  "+str(state_plateau[1])+"   "+str(state_plateau[3])+"  ")
    print(str(state_plateau[0])+"   "+str(state_plateau[8])+"   "+str(state_plateau[4]))
    print("  "+str(state_plateau[7])+"   "+str(state_plateau[5])+"  ")
    print("    "+str(state_plateau[6])+"    ")

if __name__ == "__main__":
    state_plateau=['*','*','*','*','o','o','o','o','.']
    affichage_plateau(state_plateau)