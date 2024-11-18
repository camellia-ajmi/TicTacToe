# Function to create an empty board
def create_board():
    return [" " for _ in range(9)]

# Function to display the board
def display_board(board):
    print("\n")  # Add space
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("-" * 9)
    print("\n")  # Add space 

# Function to place a symbol
def place_symbol(board, position, symbol):
    if board[position - 1] == " ":  # Check if the box is empty
        board[position - 1] = symbol
        return True
    else:
        print("This box is already occupied. Try another one.")
        return False

# Function to check if a player has won
def check_winner(board, symbol):
    winning_combinations = [
        [0, 1, 2],  # Rows
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],  # Columns
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],  # Diagonals
        [2, 4, 6]
    ]
    for combination in winning_combinations:
        if all(board[i] == symbol for i in combination):
            return True
    return False

# Function to check if the board is full
def is_full(board):
    return all(box != " " for box in board)

# Main function to play the game
def play_tic_tac_toe():
    # Asking for player names
    player1 = input("Enter the name of Player 1 (X): ")
    player2 = input("Enter the name of Player 2 (O): ")
    players = [(player1, "X"), (player2, "O")]
    turn = 0
    board = create_board()

    print("\nWelcome to Tic-Tac-Toe!")
    print(f"{player1} will be X and {player2} will be O.")
    display_board(board)

    while True:
        current_player_name, current_symbol = players[turn % 2]
        print(f"{current_player_name}'s turn ({current_symbol}).")

        try:
            # Prompt player for their move
            position = int(input(f"{current_player_name}, choose a box (1-9): "))

            # Validate the input range
            if position < 1 or position > 9:
                print("Please enter a valid box number between 1 and 9.")
                continue

            # Place the symbol if valid
            if place_symbol(board, position, current_symbol):
                display_board(board)

                # Check if the current player has won
                if check_winner(board, current_symbol):
                    print(f"Congratulations, {current_player_name}! You win!")
                    break

                # Check if the board is full
                if is_full(board):
                    print("It's a draw! The board is full.")
                    break

                # Move to the next turn
                turn += 1
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# Main loop to ask if the user wants to play again
while True:
    play_tic_tac_toe()
    again = input("Do you want to play again? (yes or no): ")
    if again.lower() != "yes":
        print("Thanks for playing! Goodbye!")
        break

# end of code 
#MAYA code
#add 
