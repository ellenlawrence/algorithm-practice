def create_board():
    '''Initializes a new game board.'''

    board = [[0, 1, 2, 3, 4, 5, 6, 7, 8], 
        [1, '-', '-', '-', '-', '-', '-', '-', '-'], 
        [2, 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'], 
        [3, '-', '-', '-', '-', '-', '-', '-', '-'],
        [4, '-', '-', '-', '-', '-', '-', '-', '-'],
        [5, '-', '-', '-', '-', '-', '-', '-', '-'], 
        [6, '-', '-', '-', '-', '-', '-', '-', '-'], 
        [7, 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'], 
        [8, '-', '-', '-', '-', '-', '-', '-', '-']]
    return board

def display_board(board):
    '''Displays the current state of the board.'''

    print('\n'.join([' '.join([f'{item}' for item in row]) for row in board]))

def move_is_valid(board, player_num, current, future):
    '''Checks if the inputted coordinates would render a valid move. Still need
    to implement way to make sure that the player made the capturing move if it
    was available.'''

    try:
        x1 = int(current[0])
        y1 = int(current[3])
        x2 = int(future[0])
        y2 = int(future[3])
    except:
        return False

    if board[y1][x1] == 'w':
        if player_num % 2 != 0:
            return False
        if (y2 == y1 - 1) and ((x2 == x1 + 1) or (x2 == x1 - 1)) and (board[y2][x2] == 'b'):
            return True
        elif (y2 == y1 - 1) and (x2 == x1) and (board[y2][x2] == '-'):
            return True
        else:
            return False

    elif board[y1][x1] == 'b':
        if player_num % 2 == 0:
            return False
        if (y2 == y1 + 1) and ((x2 == x1 + 1) or (x2 == x1 - 1)) and (board[y2][x2] == 'w'):
            return True
        elif (y2 == y1 + 1) and (x2 == x1) and (board[y2][x2] == '-'):
            return True
        else:
            return False

    else:
        return False

def render_move(board, x1, y1, x2, y2):
    '''Renders the requested move to the board.'''

    if board[y1][x1] == 'w':
        board[y2][x2] = 'w'
        board[y1][x1] = '-'

    if board[y1][x1] == 'b':
        board[y2][x2] = 'b'
        board[y1][x1] = '-'

    return board

def game_over(board):
    '''Returns True when a pawn gets to the opposite end of the board. Still 
    need to implement way to check if there are no available moves.'''

    if 'w' in board[1]:
        return True

    elif 'b' in board[8]:
        return True

    else:
        return False



board = create_board()
display_board(board)
player_num = 0
w_old = 8
b_old = 8
w_new = 0
b_new = 0

while not game_over(board):

    if player_num % 2 == 0:
        print('White, it is your turn.')
    else:
        print('Black, it is your turn.')

    current_coords = input('Please type the coordinates of the piece you would like to move, in x, y format: ')
    move_to = input('Please type the coordinates of where you would like to move the piece to, in x, y format: ')

    while not move_is_valid(board, player_num, current_coords, move_to):
        current_coords = input('That move is invalid, please type the coordinates for a piece you would like to move, in x, y format: ')
        move_to = input('Please type the coordinates of where you would like to move the piece to, in x, y format: ')

    x1 = int(current_coords[0])
    y1 = int(current_coords[3])
    x2 = int(move_to[0])
    y2 = int(move_to[3])

    render_move(board, x1, y1, x2, y2)
    display_board(board)
    
    
    for row in board:
        for item in row:
            if item == 'w':
                w_new += 1
            if item == 'b':
                b_new += 1
    if (w_new == w_old) and (b_new == b_old):
        player_num += 1
    else:
        w_old = w_new
        b_old = b_new










