import cards
import combinaison2 as combinaison
import random

paquet = []
for symbol in cards.symbols[1:]:
    for color in cards.colors:
        paquet.append(cards.card(symbol, color))
random.shuffle(paquet)


board = paquet[0:5]
en_main = paquet[5:7]

print(board)
print(en_main)

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
main_combi = {}
for main in combinaison_list:
    #print("\n===============================================================================")
    #print(main)
    combi = combinaison.combinaison(main)
    #print(combi)
    list_combi.append(combi)

print("\n===============================================================================")
best_combi = max(list_combi)
print(best_combi.main)
print(best_combi)