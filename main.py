from plateau import *

# '*' pions noirs
# 'o' pions blancs
# '.' case vide

# lance et met fin à la partie
def launch_game(plateau, agent_noir, agent_blanc):
    game = 1
    count_tour = 1
    plateau.update_plateau(agent_noir, agent_blanc)
    while game == 1:
        print("tour :", count_tour)
        game = agent_noir.play(plateau)
        plateau.update_plateau(agent_noir, agent_blanc)

        if game == 0:
            return 0

        game = agent_blanc.play(plateau)
        plateau.update_plateau(agent_noir, agent_blanc)

        count_tour += 1

if __name__ == "__main__":
    agent_noir = agent('*')
    agent_blanc = agent('o')
    plateau = plateau()

    launch_game(plateau, agent_noir, agent_blanc)