from Data.GameScreen import *


# AI move
def AI():
    best_score = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = 'X'
                move_score = minimax(board, False) ######
                board[i][j] = ''

                if move_score > best_score:
                    best_score = move_score
                    best_move = (i, j)

    if best_move:
        board[best_move[0]][best_move[1]] = 'X'

# Minimax Search
def minimax(board, is_maximizing):
    scores = {'O': -1, 'X': 1, 'tie': 0}

    winner = check_winner()
    if winner:
        return scores[winner]

    if is_board_full():
        return scores['tie']

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'X'
                    eval = minimax(board, False)
                    board[i][j] = ''
                    max_eval = max(max_eval, eval)
        return max_eval

    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'O'
                    eval = minimax(board, True)
                    board[i][j] = ''
                    min_eval = min(min_eval, eval)
        return min_eval


# Functions
def draw_grid():
    
    for i in range(1, 3): # Vertical lines
        pygame.draw.line(screen, LINE_COLOR, (i * WIDTH // 3, 0), (i * WIDTH // 3, HEIGHT), LINE_WIDTH)
    
    
    for i in range(1, 3): # Horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (0, i * HEIGHT // 3), (WIDTH, i * HEIGHT // 3), LINE_WIDTH)

def draw_symbols():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'O':
                draw_circle(row, col)
            elif board[row][col] == 'X':
                draw_cross(row, col)

def draw_circle(row, col):
    center_x = col * WIDTH // 3 + WIDTH // 6
    center_y = row * HEIGHT // 3 + HEIGHT // 6
    pygame.draw.circle(screen, CIRCLE_COLOR, (center_x, center_y), WIDTH // 6 *(3/4), LINE_WIDTH)

def draw_cross(row, col):
    x1 = col * WIDTH // 3 + WIDTH // 15
    y1 = row * HEIGHT // 3 + HEIGHT // 15
    x2 = (col + 1) * WIDTH // 3 - WIDTH // 15
    y2 = (row + 1) * HEIGHT // 3 - HEIGHT // 15
    pygame.draw.line(screen, CROSS_COLOR, (x1, y1), (x2, y2), LINE_WIDTH)
    pygame.draw.line(screen, CROSS_COLOR, (x1, y2), (x2, y1), LINE_WIDTH)

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '':
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    return None

def is_board_full():
    for row in range(3):
        for col in range(3):
            if board[row][col] == '':
                return False
    return True