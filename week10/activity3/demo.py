"""
Demo script for Tic-Tac-Toe game
Shows a sample game session
"""

from tic_tac_toe import TicTacToeGame, Board, Player

def demo_game():
    """Demonstrate the game functionality."""
    print("=== Tic-Tac-Toe Game Demo ===")
    print()
    
    # Create a game instance
    game = TicTacToeGame()
    
    # Add players
    game.add_player("Alice", "X")
    game.add_player("Bob", "O")
    
    print("Players added: Alice (X) and Bob (O)")
    print()
    
    # Demonstrate board display
    print("Empty board:")
    game.board.display()
    
    # Make some moves
    print("Making moves...")
    game.board.make_move(1, 1, "X")  # Alice's move
    print("After Alice's move (1,1):")
    game.board.display()
    
    game.board.make_move(0, 0, "O")  # Bob's move
    print("After Bob's move (0,0):")
    game.board.display()
    
    game.board.make_move(1, 0, "X")  # Alice's move
    print("After Alice's move (1,0):")
    game.board.display()
    
    game.board.make_move(0, 1, "O")  # Bob's move
    print("After Bob's move (0,1):")
    game.board.display()
    
    game.board.make_move(1, 2, "X")  # Alice's move
    print("After Alice's move (1,2):")
    game.board.display()
    
    # Check for winner
    winner = game.board.check_winner()
    if winner:
        winner_name = "Alice" if winner == "X" else "Bob"
        print(f"🎉 {winner_name} wins with 3 in a row!")
    else:
        print("No winner yet...")
    
    print("\n=== Demo Complete ===")
    print("To play the full interactive game, run: python tic_tac_toe.py")

if __name__ == "__main__":
    demo_game()
