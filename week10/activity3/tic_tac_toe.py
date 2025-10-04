"""
Tic-Tac-Toe Game Implementation
A complete OOP implementation of the classic 3x3 Tic-Tac-Toe game.
"""


class Board:
    """Represents the game board and handles board operations."""

    def __init__(self):
        """Initialize an empty 3x3 board."""
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]
        self.size = 3

    def display(self):
        """Display the current state of the board."""
        print("\n  0   1   2")
        for i in range(self.size):
            print(f"{i} {self.grid[i][0]} | {self.grid[i][1]} | {self.grid[i][2]}")
            if i < self.size - 1:
                print("  ---------")
        print()

    def is_valid_move(self, row, col):
        """Check if a move is valid (within bounds and empty cell)."""
        if not (0 <= row < self.size and 0 <= col < self.size):
            return False
        return self.grid[row][col] == ' '

    def make_move(self, row, col, symbol):
        """Make a move on the board."""
        if self.is_valid_move(row, col):
            self.grid[row][col] = symbol
            return True
        return False

    def is_full(self):
        """Check if the board is full."""
        for row in self.grid:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def check_winner(self):
        """Check if there's a winner and return the winning symbol."""
        # Check rows
        for row in self.grid:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        # Check columns
        for col in range(self.size):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] != ' ':
                return self.grid[0][col]

        # Check diagonals
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != ' ':
            return self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != ' ':
            return self.grid[0][2]

        return None


class Player:
    """Represents a player in the game."""

    def __init__(self, name, symbol):
        """Initialize a player with name and symbol."""
        self.name = name
        self.symbol = symbol

    def get_move(self):
        """Get player's move input."""
        while True:
            try:
                move = input(f"{self.name} ({self.symbol}), enter your move (row,col): ")
                row, col = map(int, move.split(','))
                return row, col
            except ValueError:
                print("Invalid input! Please enter row,col (e.g., 1,2)")
            except (EOFError, KeyboardInterrupt):
                print("Input interrupted. Exiting...")
                raise

    def get_name(self):
        """Get player name."""
        return self.name

    def get_symbol(self):
        """Get player symbol."""
        return self.symbol


class TicTacToeGame:
    """Main game class that manages the Tic-Tac-Toe game."""

    def __init__(self):
        """Initialize the game with board and players."""
        self.board = Board()
        self.players = []
        self.current_player_index = 0

    def add_player(self, name, symbol):
        """Add a player to the game."""
        self.players.append(Player(name, symbol))

    def get_current_player(self):
        """Get the current player."""
        return self.players[self.current_player_index]

    def switch_player(self):
        """Switch to the next player."""
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play_turn(self):
        """Handle one turn of the game."""
        current_player = self.get_current_player()
        self.board.display()

        while True:
            try:
                row, col = current_player.get_move()
                if self.board.make_move(row, col, current_player.symbol):
                    break
                print("Invalid move! Cell is already occupied or out of bounds.")
            except (EOFError, KeyboardInterrupt):
                print("\nGame interrupted by user.")
                return False

        return True

    def check_game_over(self):
        """Check if the game is over and return the result."""
        winner = self.board.check_winner()
        if winner:
            return "winner", winner
        if self.board.is_full():
            return "draw", None
        return "continue", None

    def play_game(self):
        """Main game loop."""
        print("Welcome to Tic-Tac-Toe!")
        print("Enter moves as row,col (e.g., 1,2 for row 1, column 2)")

        # Setup players
        player1_name = input("Enter Player 1 name: ").strip() or "Player 1"
        player2_name = input("Enter Player 2 name: ").strip() or "Player 2"

        self.add_player(player1_name, 'X')
        self.add_player(player2_name, 'O')

        print(f"\n{player1_name} is X, {player2_name} is O")
        print("Let's start the game!")

        # Game loop
        while True:
            if not self.play_turn():
                return

            result, winner = self.check_game_over()

            if result == "winner":
                self.board.display()
                winner_name = next(p.name for p in self.players if p.symbol == winner)
                print(f"🎉 Congratulations {winner_name}! You won!")
                break
            if result == "draw":
                self.board.display()
                print("🤝 It's a draw! Well played both players!")
                break

            self.switch_player()

        self.play_again()

    def play_again(self):
        """Ask if players want to play again."""
        while True:
            choice = input("\nWould you like to play again? (y/n): ").lower().strip()
            if choice in ['y', 'yes']:
                self.reset_game()
                self.play_game()
                break
            if choice in ['n', 'no']:
                print("Thanks for playing! Goodbye!")
                break
            print("Please enter 'y' for yes or 'n' for no.")

    def reset_game(self):
        """Reset the game for a new round."""
        self.board = Board()
        self.current_player_index = 0


def main():
    """Main function to start the game."""
    try:
        game = TicTacToeGame()
        game.play_game()
    except (EOFError, KeyboardInterrupt):
        print("\n\nGame interrupted. Goodbye!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
