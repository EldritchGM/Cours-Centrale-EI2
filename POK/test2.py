import cards
import combinaison2 as combinaison
import random
import time

paquet = []
for symbol in cards.symbols[1:]:
    for color in cards.colors:
        paquet.append(cards.card(symbol, color))


def tirage():
    random.shuffle(paquet)


    board = paquet[0:5]
    en_main = paquet[5:7]


    combinaison_list = []
    combinaison_list.append(board)
    for i in range(2):
        for j in range(5):
            new_combinaison = [en_main[i]] + board
            new_combinaison.remove(board[j])
            combinaison_list.append(new_combinaison)
    for i in range(5):
        for j in range(i+1,5):
            new_combinaison = en_main + board
            new_combinaison.remove(board[i])
            new_combinaison.remove(board[j])
            combinaison_list.append(new_combinaison)


    list_combi = []
    for main in combinaison_list:
        combi = combinaison.combinaison(main)
        list_combi.append(combi)

    best_combi = max(list_combi)
    return best_combi.combinaison

compteur = {}
for combi in combinaison.mains_du_poker:
    compteur[combi] = 0

nb_tirages = 100000
now = time.time()
for i in range(nb_tirages):
    compteur[tirage()] += 1
then = time.time()

for combi in combinaison.mains_du_poker:
    compteur[combi] = f"{100*compteur[combi]/nb_tirages}%"
print(compteur)
print(then - now)