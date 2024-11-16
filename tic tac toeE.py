# Create the board with 9 empty spaces
board = [" "] * 9

# Function to print the board
def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])
    print()

# Function to handle player's move
def player_move(player):
    while True:
        # Ask the player to enter a move
        choice = input(f"Player {player}, enter your move (1-9): ")
        
        # Check if the input is a valid number
        if choice.isdigit():
            choice = int(choice)  # Convert the input to an integer
            
            # Check if the input is between 1 and 9
            if 1 <= choice <= 9:
                # Check if the spot is empty
                if board[choice - 1] == " ":
                    board[choice - 1] = player  # Place the player's symbol on the board
                    break  # Exit the loop
                else:
                    print("That spot is taken! Try another one.")
            else:
                print("Please choose a number between 1 and 9.")
        else:
            print("Invalid input! Please enter a number.")

# Function to check if a player has won
def check_winner(player):
    # List of winning combinations
    winning_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    
    # Check each winning combination
    for combo in winning_combos:
        if board[combo[0]] == player and board[combo[1]] == player and board[combo[2]] == player:
            return True  # Return True if player has a winning combination
    
    return False  # Return False if no winning combination is found

# Function to check if the board is full (draw)
def check_draw():
    return " " not in board  # Return True if there are no empty spaces left

# Main function to run the game
def play_game():
    current_player = "X"  # Start with player "X"
    
    # Game loop
    while True:
        print_board()  # Show the board
        player_move(current_player)  # Current player makes a move

        # Check if the current player has won
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        
        # Check if it's a draw
        if check_draw():
            print_board()
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()
