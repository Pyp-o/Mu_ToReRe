from plateau import *
from agent import *

# '*' pions noirs
# 'o' pions blancs
# '.' case vide

# lance et met fin à la partie
def launch_game(plateau, agent_noir, agent_blanc):
    game = 1
    nb_game = 1
    count_tour = 1
    plateau.update_plateau(agent_noir, agent_blanc)
    while nb_game < 100 :
        count_tour = 1
        while game == 1:
            print("tour :", count_tour)
            game = agent_noir.play(plateau)
            plateau.update_plateau(agent_noir, agent_blanc)

            #si l'agent noir ne peut plus jouer, il faut terminer la partie
            if game == 0:
                break

            game = agent_blanc.play(plateau)
            plateau.update_plateau(agent_noir, agent_blanc)

            count_tour += 1

        print("fin de partie")
        # On reinitialise la position des pions pour relancer une partie
        plateau.new_game(agent_noir, agent_blanc)
        plateau.update_plateau(agent_noir, agent_blanc)
        nb_game += 1
        game = 1
    


if __name__ == "__main__":
    agent_noir = agent('*')
    agent_blanc = agent('o')
    plateau = plateau()

    launch_game(plateau, agent_noir, agent_blanc)