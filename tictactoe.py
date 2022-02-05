"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    i = 0
    x = 0
    O = 0
    while i < 3:
        j = 0
        while j < 3:
            if board[i][j] == "X":
                x += 1
            elif board[i][j] == "O":
                O += 1
            else:
                pass
            j += 1
        i += 1
    if x > O:
        return "O"
    elif O == x:
        return "X"
    else:
        return "Game Over"

    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    i = 0
    possible_actions = set()
    while i < 3:
        j = 0
        while j < 3:
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
            j += 1
        i += 1
    return possible_actions

    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    updated_board = copy.deepcopy(board)

    updated_board[action[0]][action[1]] = player(board)
    return updated_board

    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if board[0][0] == board[0][1] == board[0][2] or board[0][0] == board[1][0] == board[2][0] or board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    elif board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]
    else:
        return None

    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    i = 0
    if winner(board) == None and len(actions(board)) > 0:
        while i < 3:
            j = 0
            while j < 3:
                if board[i][j] == EMPTY:
                    return False
                j += 1
            i += 1
    else:
        return True

    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == "X":
            return 1
        elif winner(board) == "O":
            return -1
        else:
            return 0

    #raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def max_value(board):
        if terminal(board):
            return utility(board), None
        v = -2
        move = None
        for action in actions(board):
            aux, act = min_value(result(board, action))
            if aux > v:
                v = aux
                move = action
                if v == 1:
                    return v, move
        return v, move

    def min_value(board):
        if terminal(board):
            return utility(board), None
        v = 2
        move = None
        for action in actions(board):
            aux, act = max_value(result(board, action))
            if aux < v:
                v = aux
                move = action
                if v == -1:
                    return v, move
        return v, move

    if terminal(board):
        return None
    else:
        if player(board) == "X":
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move



    #raise NotImplementedError
