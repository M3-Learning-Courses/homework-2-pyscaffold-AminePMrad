# Define a function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Define a function to check if a player has won
def check_winner(board, player):
    # Check rows and columns for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals for a win
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Define a function to check if the game is a draw
def is_draw(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# Define the main game loop
def main():
    # Initialize the empty Tic-Tac-Toe board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        # Prompt the current player to enter a row and column
        row = int(input("Enter the row (0, 1, 2): "))
        col = int(input("Enter the column (0, 1, 2): "))

        # Check if the move is valid
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        # Place the player's symbol on the board
        board[row][col] = current_player

        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        # Check if the game is a draw
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch to the other player
        current_player = "O" if current_player == "X" else "X"

# Run the game if the script is executed
if __name__ == "__main__":
    main()
