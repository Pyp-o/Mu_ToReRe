from plateau import *
from agent import *
from memToCSV import *

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

        #si l'agent noir ne peut plus jouer, il faut terminer la partie
        if game == 0:
            break

        game = agent_blanc.play(plateau)
        plateau.update_plateau(agent_noir, agent_blanc)

        count_tour += 1

    print("fin de partie")
    # On reinitialise la position des pions pour relancer une partie
    
def load_agent(agent_noir):
    try :
        #on peut stocker la memoire d'etat sans traitement
        agent_noir.mem_etat = load_mem("etat.csv")  # load etats
        print("mem_etat", agent_noir.mem_etat)

        #on va devoir concatener la position et les probas en gardant la correspondance des indices
        position = load_mem("position.csv")  # load actions
        proba = load_mem("proba.csv")  # load probas

        # permet d'aavoir la même longueur pour chaque mémoire chargée
        if len(proba) != len(position):
            position.append([])

        #donne la forme necessaire au tableau pour entrer les valeurs des probas et des actions possibles
        for i in range(0, len(position)):
            agent_noir.mem_actions.append([[i], [i+1]])


        for i in range(0, len(position)):
            agent_noir.mem_actions[i][0] = position[i]
            agent_noir.mem_actions[i][1] = proba[i]

        print("load successful")
        return 1
    except:
        return 0


if __name__ == "__main__":
    agent_noir = agent('*')
    agent_blanc = agent('o')
    plateau = plateau()

    #charge la memoire pré-existante NE PAS UTILISER WORK IN PROGRESS
    #load_agent(agent_noir)

    nb_game = 0
    while nb_game < 20 :
        launch_game(plateau, agent_noir, agent_blanc)
        plateau.new_game(agent_noir, agent_blanc)
        nb_game += 1

    save_mem(agent_noir.mem_actions, "mem_action")   #save actions et probas
    save_mem(agent_noir.mem_etat, "mem_etat")          #save etat'

