def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    board = [" "] * 9
    current_player = "X"
    moves = 0

    while moves < 9:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            if board[move] != " ":
                print("Position already taken. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        
        board[move] = current_player
        moves += 1

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return
        
        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("It's a tie!")

# Call the function to play
tic_tac_toe()
