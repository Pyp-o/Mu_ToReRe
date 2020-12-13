import csv

def save_mem(array, text="mem_etat"):
    #ici on ne stockera que la memoire des etats, des actions et des probas associées
    if text=="mem_action":
        #on va séparer les actions des probabilités afin de faciliter l'exportation au format CSV
        position = []
        proba = []
        for i in range(0,len(array)):
            position.append(array[i][0])
            proba.append(array[i][1])
        #on stocke les actions et les probas dans des fichiers CSV
        with open("position.csv", "w") as f:
            wr = csv.writer(f)
            wr.writerows(position)
        with open("proba.csv", "w") as f:
            wr = csv.writer(f)
            wr.writerows(proba)
    #si l'on stocke l'etat dans un CSV
    elif text=="mem_etat":
        with open("etat.csv", "w") as f:
            wr = csv.writer(f)
            wr.writerows(array)


def load_mem(file):
    tab = []
    with open(file, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = csv.reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)

        #lors de l'exportation au format CSV, des listes vides s'interposent entre chaque index, on s'en debarasse donc
        for i in range(len(list_of_rows)):
            if list_of_rows[i] != []:
                tab.append(list_of_rows[i])

        #au formati CSV, les valeurs sont stockées sous forme de string, on les caste pour obtenir le format voulu
        for i in range(0, len(tab)):
            for j in range(0, len(tab[i])):
                if file == "proba.csv":
                    tab[i][j] = float(tab[i][j])
                elif file == "position.csv":
                    tab[i][j] = int(tab[i][j])

        return tab


#permet de faire des tests de save and load de la memoire
"""mem_action = [[[8, -1, -1, 8], [0.5, 0.0, 0.0, 0.5]], [[-1, -1, -1, 4], [0.0, 0.0, 0.0, 1.0]], [[-1, -1, -1, 5], [0.0, 0.0, 0.0, 1.0]], [[8, -1, 8, 8], [0.3333333333333333, 0.0, 0.3333333333333333, 0.3333333333333333]], [[-1, -1, 3, -1], [0.0, 0.0, 1.0, 0.0]], [[-1, -1, 4, 4], [0.0, 0.0, 0.5, 0.5]]]
mem_etat = [['*', '*', '*', '.', 'o', 'o', 'o', 'o', '*'], ['*', '*', '*', 'o', '*', 'o', 'o', 'o', '.'], ['*', '*', '*', 'o', '.', '*', 'o', 'o', 'o'], ['*', '*', '.', '*', 'o', '*', 'o', 'o', 'o'], ['*', '*', 'o', '.', 'o', '*', 'o', 'o', '*'], ['*', '*', '*', 'o', 'o', '*', 'o', 'o', '.'], ['*', '*', '*', 'o', '*', '.', 'o', 'o', 'o'], ['*', '*', '.', 'o', '*', 'o', 'o', 'o', '*'], ['*', '*', 'o', '*', '*', 'o', 'o', 'o', '.'], ['*', '*', 'o', '*', '.', '*', 'o', 'o', 'o'], ['.', '*', 'o', '*', 'o', '*', 'o', 'o', '*'], ['o', '*', 'o', '*', 'o', '*', 'o', '*', '.'], ['o', '*', 'o', '*', 'o', '*', '*', '.', 'o'], ['o', '*', 'o', '.', 'o', '*', '*', 'o', '*'], ['o', '*', 'o', 'o', '*', '.', '*', 'o', '*'], ['.', '*', '*', '*', 'o', 'o', 'o', 'o', '*'], ['o', '*', '*', '*', 'o', 'o', 'o', '*', '.'], ['*', '*', '*', '*', 'o', 'o', 'o', '.', 'o'], ['o', '*', '*', '.', 'o', '*', 'o', '*', 'o'], ['o', '*', '*', 'o', '*', '.', 'o', '*', 'o'], ['o', '*', '*', 'o', '*', 'o', '*', '.', 'o'], ['*', '.', '*', 'o', '*', 'o', '*', 'o', 'o'], ['*', 'o', '.', 'o', '*', 'o', '*', 'o', '*'], ['*', '*', 'o', 'o', '*', 'o', '*', 'o', '.'], ['*', '*', 'o', '*', '.', 'o', '*', 'o', 'o'], ['.', '*', 'o', '*', 'o', 'o', '*', 'o', '*'], ['o', '*', 'o', '*', 'o', 'o', '.', '*', '*'], ['*', '*', 'o', '*', 'o', '*', 'o', '.', 'o'], ['*', '.', 'o', '*', 'o', '*', 'o', 'o', '*'], ['*', 'o', '*', '*', 'o', '*', 'o', 'o', '.'], ['*', 'o', '*', '.', 'o', '*', 'o', 'o', '*'], ['*', 'o', '*', 'o', '*', '*', 'o', 'o', '.'], ['.', '*', '*', 'o', '*', '*', 'o', 'o', 'o'], ['*', '.', '*', '*', 'o', 'o', 'o', '*', 'o'], ['*', 'o', '*', '.', 'o', 'o', 'o', '*', '*'], ['*', 'o', '*', 'o', '*', 'o', 'o', '*', '.'], ['*', 'o', '*', 'o', '.', '*', 'o', '*', 'o'], ['*', 'o', '.', '*', 'o', '*', 'o', '*', 'o'], ['.', '*', 'o', '*', 'o', '*', 'o', '*', 'o'], ['o', '*', 'o', '*', 'o', '*', 'o', '.', '*'], ['o', '*', 'o', '*', 'o', '.', '*', 'o', '*'], ['o', '*', 'o', '*', '*', 'o', '*', 'o', '.'], ['*', '.', 'o', '*', '*', 'o', '*', 'o', 'o'], ['.', 'o', 'o', '*', '*', 'o', '*', 'o', '*'], ['o', 'o', 'o', '*', '*', 'o', '*', '*', '.'], ['*', 'o', 'o', '*', '*', 'o', '*', '.', 'o'], ['*', 'o', 'o', '*', '.', 'o', '*', 'o', '*'], ['*', 'o', 'o', '*', 'o', '*', '.', 'o', '*'], ['*', 'o', 'o', '*', 'o', '*', 'o', '*', '.'], ['*', 'o', '*', '.', 'o', '*', 'o', '*', 'o'], ['*', 'o', '.', 'o', 'o', '*', 'o', '*', '*'], ['*', '*', 'o', 'o', 'o', '*', 'o', '*', '.'], ['*', '*', 'o', 'o', 'o', '*', '*', '.', 'o'], ['.', '*', 'o', 'o', 'o', '*', '*', 'o', '*'], ['o', '*', 'o', 'o', 'o', '*', '*', '*', '.'], ['o', '.', '*', 'o', 'o', '*', '*', '*', 'o'], ['*', 'o', '*', 'o', 'o', '*', '*', '.', 'o'], ['*', 'o', '.', 'o', 'o', '*', '*', 'o', '*'], ['o', '*', '*', 'o', 'o', '*', '*', 'o', '.'], ['o', '*', '*', 'o', 'o', '*', '.', '*', 'o'], ['o', '*', '.', 'o', 'o', '*', 'o', '*', '*'], ['o', '*', 'o', '*', '*', '.', 'o', '*', 'o'], ['o', '*', 'o', '*', '*', 'o', '*', '.', 'o'], ['o', '*', 'o', '.', '*', 'o', '*', 'o', '*'], ['o', '*', '*', 'o', '*', 'o', '*', 'o', '.'], ['o', '*', '*', 'o', '*', 'o', '.', '*', 'o'], ['o', '*', '*', 'o', '.', '*', 'o', '*', 'o'], ['o', '*', '.', '*', 'o', '*', 'o', '*', 'o'], ['o', '*', 'o', '*', 'o', '.', 'o', '*', '*'], ['o', '*', 'o', '*', '*', 'o', 'o', '*', '.'], ['o', '*', '*', '.', '*', 'o', '*', 'o', 'o'], ['o', '*', '*', 'o', '.', 'o', '*', 'o', '*'], ['o', '*', '*', '*', 'o', 'o', '*', 'o', '.'], ['o', '*', '*', '*', 'o', 'o', '.', '*', 'o'], ['.', '*', '*', 'o', 'o', '*', 'o', 'o', '*'], ['o', '*', '*', 'o', 'o', '*', 'o', '*', '.'], ['o', '*', '*', 'o', '.', 'o', 'o', '*', '*'], ['o', '*', '*', '.', '*', 'o', 'o', '*', 'o']]

position = load_mem("position.csv")     #load actions 
proba = load_mem("proba.csv")           #load probas
etat = load_mem("etat.csv")             #load etats
print("position", position)
print("taille", len(position))
print("proba", proba)
print("taille", len(proba))
print("etat", etat)
print("taille", len(etat))"""

