import numpy as np
from random import choice 

size = 8

black = 1
white = -1
empty = 0

pass_move = size * size

# directions, dans le sens direct, en commençant par la droite
directions = (1, 1 - size, -size, -1 - size, -1, -1 + size, size, 1 + size)

# renvoie le signe de x
def sign(x):
    return int(x > 0) - int(x < 0)

# limites d'itération en fonction de la direction, dans le sens direct, en commençant par la droite
limits = [[(size - 1 - j, min(i, size - 1 - j), i, min(i, j), j, min(size - 1 - i, j), size - 1 - i, min(size - 1 - i, size - 1 - j))
            for j in range(size)] for i in range(size)]

# indique s'il y a des pions à retourner dans une direction donnée
# player est la couleur de celui qui joue
# limit est la limite à ne pas dépasser afin de ne pas sortir du plateau
def check1D(board, position, player, direction, limit):
    k = 1
    position += direction
    while k <= limit and board[position] == -player:
        position += direction
        k = k + 1

    # Il faut qu'il y ait eu au moins un pion adverse
    return (k > 1 and k <= limit and board[position] == player)

# Calcule le suivant dans une direction donnée 
# player est la couleur de celui qui joue
# limit est la limite à ne pas dépasser afin de ne pas sortir du plateau
# On suppose qu'on doit effectivement retourner des pions dans cette direction
# i. e. check1D a été appelé avant
def play1D(board, position, player, direction, limit):
    k = 1
    position += direction
    while k <= limit and board[position] == -player:
        board[position] = player
        position += direction
        k = k + 1

# Calcule le successeur en place, obtenu en ajoutant un pion de player
# sur la position donnée
def play_(board, position, player):
    if position != pass_move:
        # La position en 2D
        i = position // size   
        j = position % size

        # La case jouée
        board[position] = player

        # Retourne les pions dans toutes les directions
        for direction, limit in zip(directions, limits[i][j]):
            if check1D(board, position, player, direction, limit):
                play1D(board, position, player, direction, limit) 

# Successeur avec copie
def play(board, position, player):
    r = np.copy(board)
    play_(r, position, player)

    return r

# Intialise le plateau
def init_board():
    # Crée et initialise tout à vide
    b = np.array([empty for k in range(size*size)])

    # Place les quatre premiers pions
    b[3 * size + 3] = white
    b[4 * size + 4] = white
    b[3 * size + 4] = black
    b[4 * size + 3] = black

    return b

# Affiche le plateau
def print_board(board):
    # Numéros de colonne
    print("  ", end='')
    for i in range(size):
        print(f'{i + 1}', end=' ')
    print()

    for i in range(size):
        # Affiche le numéro de la ligne
        print(f'{size - i}', end=' ')
        for j in range(size):
            # Contenu de la case
            p = board[i * size + j]

            if p == empty:
                print(".", end = ' ')
            elif p == black:
                print("O", end = ' ')
            elif p == white:
                print("X", end = ' ')
            else:
                print("?", end = ' ')

        # Réaffiche le numéro de la ligne
        print(f'{size - i}')

    # Numéros de colonne à nouveau
    print("  ", end='')
    for i in range(size):
        print(f'{i + 1}', end=' ')
    print()
    print("-------------------")


# Trouve les coups légaux pour le joueur player
def legal_moves(board, player):
    L = []
    for p in range(size * size):
        # Il faut au moins que la case soit vide
        if board[p] == empty:
            # On cherche au moins une direction dans laquelle c'est valide
            i = p // size
            j = p % size
            
            lims = limits[i][j]

            valid = False
            n = 0
            while n < 8 and not valid:
                valid = check1D(board, p, player, directions[n], lims[n]) 
                n = n + 1

            # Valide, on enregistre
            if valid:
                L.append(p)

    # Pas de coup à jouer: il faut passer
    if not L:
        L.append(pass_move)

    return L

# Vérifie si la partie est finie
# Similaire à legal_moves mais on teste les deux joueurs
# pour chaque case
def terminal(board):
    r = True
    p = 0
    while p < size * size and r:
        # Il faut au moins que la case soit vide
        if board[p] == empty:
            # On cherche au moins une direction dans laquelle c'est valide
            i = p // size
            j = p % size

            lims = limits[i][j]

            n = 0
            while n < 8 and r:
                # check1D nous dit si on peut jouer dans cette direction
                # si on peut alors la position n'est pas terminale
                r = not (check1D(board, p, black, directions[n], lims[n])
                    or check1D(board, p, white, directions[n], lims[n])) 
                n = n + 1

        p = p +1

    return r

# Trouve le joueur qui a le plus de pions
def winner(board):
    score = 0
    for i in range(size * size):
        score += board[i]

    return sign(score)

def human(board, player):
    LEGAL = legal_moves(board, player)
    IN = (-1, -1)
    while IN not in LEGAL:
        line = input("Enter line number: ")
        column = input("Enter column number: ")
        IN = (line, column)
    return play(board, IN, player)

def alea(board, player):
    LEGAL = legal_moves(board, player)
    IN = choice(LEGAL)
    return play(board, IN, player)

# b1 = init_board()
# print_board(b1)
# L = legal_moves(b1, white)
# L2 = map(lambda x: (size - x//size, x%size + 1), L)
# b2 = play(b1, L[0], white)
# print_board(b2)
# print(terminal(b2))
# print(winner(b2))

def main():
    board = init_board()
    while not terminal(board):
        print_board(board)
        board = alea(board, black)
        if terminal(board):
            break
        else:
            print_board(board)
            board = alea(board, white)
    print_board(board)
    if winner(board) == black:
        print("Black (O) wins!")
    else:
        print("White (X) wins!")

if __name__ == "__main__":
    main()