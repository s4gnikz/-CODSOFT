import math

# Display the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check for win
def check_win(board, player):
    # Rows, columns, diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([row[i] == player for row in board]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_draw(board):
    return all([cell != ' ' for row in board for cell in row])

# Minimax Algorithm
def minimax(board, depth, is_maximizing):
    if check_win(board, "O"):
        return 1
    if check_win(board, "X"):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

# AI Move
def ai_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Human Move
def human_move(board):
    while True:
        try:
            row = int(input("Enter row (0,1,2): "))
            col = int(input("Enter column (0,1,2): "))
            if board[row][col] == " ":
                return (row, col)
            else:
                print("Cell already filled! Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter numbers 0, 1, or 2.")

# Game Loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("You are X, AI is O.")
    print_board(board)
    while True:
        # Human turn
        row, col = human_move(board)
        board[row][col] = "X"
        print_board(board)
        if check_win(board, "X"):
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        # AI turn
        print("AI is making a move...")
        move = ai_move(board)
        board[move[0]][move[1]] = "O"
        print_board(board)
        if check_win(board, "O"):
            print("AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
