def player(board):
    """
    Returns player who has the next turn on a board.
    """
    i = 0
    j = 0
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

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    i = 0
    actions = set()
    while i < 3:
        j = 0
        while j < 3:
            if board[i][j] == EMPTY:
                actions.add((i,j))
            j += 1
        i += 1
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    updated_board = board
    i = action[0]
    j = action[1]
    if board[i][j] != EMPTY:
        raise Exception("You can not place your move on a field that's not empty!")
    if player(board) == "X":
        updated_board[i][j] = "X"
    elif player(board) == "O":
        updated_board[i][j] = "O"

    return updated_board

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


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            if board[i][j] == EMPTY:
                return False
            j += 1
        i += 1
    return True

    # raise NotImplementedError
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def max_value(board):
        if terminal(board):
            return
        v = -2
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    def min_value(board):
        if terminal(board):
            return None
        v = 2
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v

    if terminal(board):
        return None
    if player(board) == "X":
        max_value(board)
    elif player(board) == 'O':
        min_value(board)


EMPTY = None
board = [[EMPTY, "X", "X"],
         ["O", "X", "O"],
         ["O", EMPTY, "X"]]

print(minimax(board))