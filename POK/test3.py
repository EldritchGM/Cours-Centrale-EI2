import cards
import combinaison2 as combinaison
import random
import time

paquet = []
for symbol in cards.symbols[1:]:
    for color in cards.colors:
        paquet.append(cards.card(symbol, color))


def tirage(nb_joueurs):
    random.shuffle(paquet)

    board = paquet[0:5]


    joueurs = [paquet[(5 + 2 * i):(7 + 2 * i)] for i in range(nb_joueurs)]

    combinaison_list = []

    for joueur in range(nb_joueurs):
        combinaison_list.append([])
        combinaison_list[joueur].append(board)
        for i in range(2):
            for j in range(5):
                new_combinaison = [joueurs[joueur][i]] + board
                new_combinaison.remove(board[j])
                combinaison_list[joueur].append(new_combinaison)
        for i in range(5):
            for j in range(i+1,5):
                new_combinaison = joueurs[joueur] + board
                new_combinaison.remove(board[i])
                new_combinaison.remove(board[j])
                combinaison_list[joueur].append(new_combinaison)


    lists_combi = []
    best_combi = []
    for joueur in range(nb_joueurs):
        lists_combi.append([])
        for main in combinaison_list[joueur]:
            combi = combinaison.combinaison(main)
            lists_combi[joueur].append(combi)
        best_combi.append(max(lists_combi[joueur]))

    
    best_combi_overall = max(best_combi)
    winner = best_combi.index(best_combi_overall)
    other_combi = best_combi
    other_combi.pop(winner)
    #print(best_combi_overall)
    for combi in other_combi:
        if combi == best_combi_overall:
            return 0
    return (winner + 1)


nb_joueurs = 6
compteur = {}
for combi in range(nb_joueurs + 1):
    compteur[combi] = 0

nb_tirages = 5000
now = time.time()
for i in range(nb_tirages):
    compteur[tirage(nb_joueurs)] += 1
then = time.time()

print(compteur)
print(then - now)