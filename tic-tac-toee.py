#Board
board = [" " for x in range(9)] 

# Function board
def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])
    
    print()  
    print(row1)
    print(row2)
    print(row3)
    print()

# Function for player move
def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
    print("Your turn, player {}".format(number))
    
    # Input validation
    choice = int(input("Enter your move (1-9): ").strip())
    if choice < 1 or choice > 9:
        print("Invalid choice. Please pick a number between 1 and 9.")
        return player_move(icon)
    
    if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        print("That space is already taken! Try again.")
        player_move(icon)

# Function to check for victory
def is_victory(icon):
    # Check rows, columns, and diagonals for a win
    return ((board[0] == icon and board[1] == icon and board[2] == icon) or
            (board[3] == icon and board[4] == icon and board[5] == icon) or
            (board[6] == icon and board[7] == icon and board[8] == icon) or
            (board[0] == icon and board[3] == icon and board[6] == icon) or
            (board[1] == icon and board[4] == icon and board[7] == icon) or
            (board[2] == icon and board[5] == icon and board[8] == icon) or
            (board[0] == icon and board[4] == icon and board[8] == icon) or
            (board[2] == icon and board[4] == icon and board[6] == icon))

# Function to check for a draw
def is_draw():
    return " " not in board

# Main game loop
while True:
    print_board()
    player_move("X")
    if is_victory("X"):
        print_board()
        print("X wins! Congratulations!")
        break
    elif is_draw():
        print_board()
        print("It's a draw!")
        break

    print_board()
    player_move("O")
    if is_victory("O"):
        print_board()
        print("O wins! Congratulations!")
        break
    elif is_draw():
        print_board()
        print("It's a draw!")
        break
