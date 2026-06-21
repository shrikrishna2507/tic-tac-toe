# ========================================
# Tic-Tac-Toe: Two-Player Console Game
# Author: [Your Name]
# Date: December 2025
# Tech: Python, VS Code, Git
# ========================================

def create_board():
    """Create and return an empty 3x3 board."""
    return [[" " for _ in range(3)] for _ in range(3)]


def display_board(board):
    """Display the current state of the board."""
    print("\n")
    print("  Col  1     2     3")
    print("       |     |     ")
    for i, row in enumerate(board):
        print(f"Row {i+1}  {row[0]}  |  {row[1]}  |  {row[2]}")
        if i < 2:
            print("     _____|_____|_____")
            print("          |     |     ")
    print("       |     |     ")
    print("\n")


def get_player_move(board, player):
    """Prompt the current player for a valid move and return (row, col)."""
    while True:
        try:
            print(f"Player {player}'s turn.")
            row = int(input("  Enter row (1-3): ")) - 1
            col = int(input("  Enter column (1-3): ")) - 1

            if row not in range(3) or col not in range(3):
                print("   Invalid input! Row and column must be between 1 and 3.\n")
                continue

            if board[row][col] != " ":
                print("   That cell is already taken! Try again.\n")
                continue

            return row, col

        except ValueError:
            print("   Please enter numbers only.\n")


def make_move(board, row, col, player):
    """Place the player's mark on the board."""
    board[row][col] = player


def check_winner(board, player):
    """
    Check if the given player has won.
    Winning conditions: any row, column, or diagonal fully marked by player.
    """
    # Check all rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check all columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check main diagonal (top-left to bottom-right)
    if all(board[i][i] == player for i in range(3)):
        return True

    # Check anti-diagonal (top-right to bottom-left)
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def check_draw(board):
    """Return True if the board is full and no winner (draw condition)."""
    return all(board[row][col] != " " for row in range(3) for col in range(3))


def switch_player(current_player):
    """Switch turn between X and O."""
    return "O" if current_player == "X" else "X"


def play_again():
    """Ask players if they want to play another round."""
    choice = input("Do you want to play again? (yes/no): ").strip().lower()
    return choice in ("yes", "y")


def display_scores(scores):
    """Display current scores."""
    print("\n Scoreboard:")
    print(f"  Player X: {scores['X']} wins")
    print(f"  Player O: {scores['O']} wins")
    print(f"  Draws    : {scores['Draw']}\n")


def main():
    """Main function to run the Tic-Tac-Toe game loop."""
    print("=" * 40)
    print("   Welcome to Tic-Tac-Toe! 🎮")
    print("=" * 40)
    print("  Two players take turns: X goes first.")
    print("  Enter row and column numbers (1-3).")
    print("=" * 40)

    scores = {"X": 0, "O": 0, "Draw": 0}

    while True:
        board = create_board()
        current_player = "X"
        game_over = False

        while not game_over:
            display_board(board)
            row, col = get_player_move(board, current_player)
            make_move(board, row, col, current_player)

            if check_winner(board, current_player):
                display_board(board)
                print(f" Player {current_player} wins! Congratulations!\n")
                scores[current_player] += 1
                game_over = True

            elif check_draw(board):
                display_board(board)
                print(" It's a draw! Well played by both!\n")
                scores["Draw"] += 1
                game_over = True

            else:
                current_player = switch_player(current_player)

        display_scores(scores)

        if not play_again():
            print("\nThanks for playing! Goodbye! \n")
            break


if __name__ == "__main__":
    main()
