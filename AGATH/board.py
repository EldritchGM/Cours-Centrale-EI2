import numpy as np
from random import choice 
from time import time

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



def evaluate1(board):
    score_black = 0
    score_white = 0
    for i in range(size * size):
        if board[i] > 0:
            score_black += 1
        elif board[i] < 0:
            score_white -= 1
    return score_black-score_white

def evaluate2(board):
    score_black = len(legal_moves(board, black))
    score_white = - len(legal_moves(board, white))
    return score_black-score_white

def minimax(board, player, depth, evaluation):
    assert evaluation in [1,2]
    coup = None
    if depth == 0:
        if evaluation == 1:
            U = evaluate1(board)
        else:
            U = evaluate2(board)
    else:
        if player == black:
            v = - 100 # le score oscille entre - 64 et 64
            for move in legal_moves(board, black):
                rec = minimax(play(board, move, player), white, depth - 1, evaluation)[0]
                if rec >= v:
                    v = rec
                    coup = move
        else:
            v = 100
            for move in legal_moves(board, white):
                rec = minimax(play(board, move, player), black, depth - 1, evaluation)[0]
                if rec <= v:
                    v = rec
                    coup = move
        U = v
    return U, coup

def minimax_strategist(board, player, depth, evaluation):
    assert evaluation in [1,2]
    assert depth > 0
    then = time()
    coup = minimax(board, player, depth, evaluation)[1]
    now = time()
    print(f"Temps d'exécution minimax{evaluation} : {now - then}")
    return play(board, coup, player)

def minimax_tr(board, player, depth, evaluation, TR = {black: {}, white: {}}):
    assert evaluation in [1,2]
    coup = None
    if depth == 0:
        if evaluation == 1:
            U = evaluate1(board)
        else:
            U = evaluate2(board)
    else:
        if tuple(board) in TR[player].keys():
            if TR[player][tuple(board)]['depth'] >= depth:
                return TR[player][tuple(board)]['score'], TR[player][tuple(board)]['coup'], TR
        if player == black:
            v = - 100 # le score oscille entre - 64 et 64
            for move in legal_moves(board, black):
                rec_score, rec_move, TR = minimax_tr(play(board, move, player), white, depth - 1, evaluation, TR)
                if rec_score >= v:
                    v = rec_score
                    coup = move
        else:
            v = 100
            for move in legal_moves(board, white):
                rec_score, rec_move, TR = minimax_tr(play(board, move, player), black, depth - 1, evaluation, TR)
                if rec_score <= v:
                    v = rec_score
                    coup = move
        U = v
        TR[player][tuple(board)] = {'key': (player, board), 'depth': depth, 'score': U, 'coup': coup}

    return U, coup, TR

def minimax_tr_strategist(board, player, depth, evaluation, TR):
    assert evaluation in [1,2]
    assert depth > 0
    then = time()
    score, coup, TR = minimax_tr(board, player, depth, evaluation, TR)
    now = time()
    print(f"Temps d'exécution minimax{evaluation} : {now - then}s")
    return play(board, coup, player), TR

def alphabeta(board, player, depth, evaluation = 1, alpha = -100, beta = 100):
    coup = None
    if depth == 0:
        if evaluation == 1:
            U = evaluate1(board)
        elif evaluation == 2:
            U = evaluate2(board)
        else:
            raise ValueError("evaluation = 1 ou 2")
    else:
        if player == black:
            v = - 100 # le score oscille entre - 64 et 64
            for move in legal_moves(board, black):
                if alpha > beta: break
                rec = alphabeta(play(board, move, player), white, depth - 1, evaluation, alpha, beta)[0]
                if rec >= v:
                    v = rec
                    coup = move
                alpha = max(alpha, v)
        else:
            v = 100
            for move in legal_moves(board, white):
                if alpha > beta: break
                rec = alphabeta(play(board, move, player), black, depth - 1, evaluation, alpha, beta)[0]
                if rec <= v:
                    v = rec
                    coup = move
                beta = min(beta, v)
        U = v
    return U, coup

def alphabeta_strategist(board, player, depth, evaluation):
    assert evaluation in [1,2]
    assert depth > 0
    then = time()
    coup = alphabeta(board, player, depth, evaluation)[1]
    now = time()
    print(f"Temps d'exécution alphabeta{evaluation} : {now - then}")
    return play(board, coup, player)    

def alphabeta_tr(board, player, depth, evaluation, TR = {black: {}, white: {}}, alpha = -100, beta = 100):
    coup = None
    if depth == 0:
        if evaluation == 1:
            U = evaluate1(board)
        elif evaluation == 2:
            U = evaluate2(board)
        else:
            raise ValueError("evaluation = 1 ou 2")
    else:
        if tuple(board) in TR[player].keys():
            if TR[player][tuple(board)]['depth'] >= depth:
                return TR[player][tuple(board)]['score'], TR[player][tuple(board)]['coup'], TR
        if player == black:
            v = - 100 # le score oscille entre - 64 et 64
            for move in legal_moves(board, black):
                if alpha > beta: break
                rec_score, rec_move, TR = alphabeta_tr(play(board, move, player), white, depth - 1, evaluation, TR, alpha, beta)
                if rec_score >= v:
                    v = rec_score
                    coup = move
                alpha = max(alpha, v)
        else:
            v = 100
            for move in legal_moves(board, white):
                if alpha > beta: break
                rec_score, rec_move, TR = alphabeta_tr(play(board, move, player), black, depth - 1, evaluation, TR, alpha, beta)
                if rec_score <= v:
                    v = rec_score
                    coup = move
                beta = min(beta, v)
        U = v
        TR[player][tuple(board)] = {'key': (player, board), 'depth': depth, 'score': U, 'coup': coup}

    return U, coup, TR

def alphabeta_tr_strategist(board, player, depth, evaluation, TR):
    assert evaluation in [1,2]
    assert depth > 0
    then = time()
    score, coup, TR = alphabeta_tr(board, player, depth, evaluation, TR)
    now = time()
    print(f"Temps d'exécution alphabeta{evaluation} : {now - then}")
    return play(board, coup, player), TR

def random_playout(board, player):
    while not terminal(board):
        board = alea(board, player)
        player *= -1
    return winner(board)

def main():
    TR1 = {black: {}, white: {}}
    TR2 = {black: {}, white: {}}
    board = init_board()
    while not terminal(board):
        print_board(board)
        board, TR2 = alphabeta_tr_strategist(board, black, 6, 1, TR2)
        if terminal(board):
            break
        else:
            print_board(board)
            board, TR1 = minimax_tr_strategist(board, white, 6, 1, TR1)
    print_board(board)
    win = winner(board)
    if win == black:
        print("Black (O) wins!")
    elif win == white:
        print("White (X) wins!")
    else:
        print("That's a draw!")

class MCTS_tree():
    def __init__(self, father, board, player):
        self.father = father
        if father is not None: 
            father.sons.append(self)
        self.board = board
        self.player = player
        self.legal = legal_moves(board, player)
        self.sons = []
        self.nb_simu = 1
        self.gain = random_playout(board, player)

def mcts_run(player, origin, n):
    board = origin.board
    for move in origin.legal:
        if play(board, move, player) not in origin.sons:
            node = MCTS_tree(origin, play(board, move, player), player)
            father = origin
            while father is not None:
                father.gain += node.gain
                father.nb_simu += 1
                father = father.father
        else:
            son_UCB1_max = -100
            son_UCB1_maximizer = -1
            for son in origin.sons:
                son_UCB1 = (son.gain/son.nb_simu) + sqrt(2*log(n)/son.nb_simu)
                if son_UCB1 >= son_UCB1_max:
                    son_UCB1_max = son_UCB1
                    son_UCB1_maximizer = son
            mcts_run(player, son_UCB1_maximizer, n)







if __name__ == "__main__":
    main()

