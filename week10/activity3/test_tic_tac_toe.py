"""
Test script for Tic-Tac-Toe game
Tests various game scenarios and edge cases
"""

import sys
from io import StringIO
from unittest.mock import patch
from tic_tac_toe import Board, Player, TicTacToeGame


def test_board_creation():
    """Test board initialization."""
    print("Testing board creation...")
    board = Board()
    assert board.size == 3
    assert len(board.grid) == 3
    assert all(len(row) == 3 for row in board.grid)
    assert all(cell == ' ' for row in board.grid for cell in row)
    print("✓ Board creation test passed")


def test_valid_moves():
    """Test valid move detection."""
    print("Testing valid moves...")
    board = Board()
    
    # Test valid moves
    assert board.is_valid_move(0, 0) == True
    assert board.is_valid_move(1, 2) == True
    assert board.is_valid_move(2, 1) == True
    
    # Test invalid moves (out of bounds)
    assert board.is_valid_move(-1, 0) == False
    assert board.is_valid_move(0, -1) == False
    assert board.is_valid_move(3, 0) == False
    assert board.is_valid_move(0, 3) == False
    
    # Test occupied cells
    board.make_move(0, 0, 'X')
    assert board.is_valid_move(0, 0) == False
    print("✓ Valid moves test passed")


def test_win_detection():
    """Test win detection logic."""
    print("Testing win detection...")
    board = Board()
    
    # Test row win
    board.make_move(0, 0, 'X')
    board.make_move(0, 1, 'X')
    board.make_move(0, 2, 'X')
    assert board.check_winner() == 'X'
    
    # Reset board
    board = Board()
    
    # Test column win
    board.make_move(0, 0, 'O')
    board.make_move(1, 0, 'O')
    board.make_move(2, 0, 'O')
    assert board.check_winner() == 'O'
    
    # Reset board
    board = Board()
    
    # Test diagonal win
    board.make_move(0, 0, 'X')
    board.make_move(1, 1, 'X')
    board.make_move(2, 2, 'X')
    assert board.check_winner() == 'X'
    
    # Reset board
    board = Board()
    
    # Test anti-diagonal win
    board.make_move(0, 2, 'O')
    board.make_move(1, 1, 'O')
    board.make_move(2, 0, 'O')
    assert board.check_winner() == 'O'
    
    print("✓ Win detection test passed")


def test_draw_detection():
    """Test draw detection."""
    print("Testing draw detection...")
    board = Board()
    
    # Fill board without winner (proper draw scenario)
    moves = [
        (0, 0, 'X'), (0, 1, 'O'), (0, 2, 'X'),
        (1, 0, 'O'), (1, 1, 'X'), (1, 2, 'O'),
        (2, 0, 'O'), (2, 1, 'X'), (2, 2, 'O')
    ]
    
    for row, col, symbol in moves:
        board.make_move(row, col, symbol)
    
    assert board.is_full() == True
    assert board.check_winner() == None
    print("✓ Draw detection test passed")


def test_player_creation():
    """Test player creation."""
    print("Testing player creation...")
    player = Player("Alice", "X")
    assert player.name == "Alice"
    assert player.symbol == "X"
    print("✓ Player creation test passed")


def test_game_initialization():
    """Test game initialization."""
    print("Testing game initialization...")
    game = TicTacToeGame()
    assert len(game.players) == 0
    assert game.current_player_index == 0
    
    game.add_player("Player1", "X")
    game.add_player("Player2", "O")
    assert len(game.players) == 2
    assert game.get_current_player().name == "Player1"
    
    game.switch_player()
    assert game.get_current_player().name == "Player2"
    print("✓ Game initialization test passed")


def test_input_validation():
    """Test input validation with mock inputs."""
    print("Testing input validation...")
    player = Player("TestPlayer", "X")
    
    # Test valid input
    with patch('builtins.input', return_value="1,2"):
        row, col = player.get_move()
        assert row == 1
        assert col == 2
    
    # Test invalid input format
    with patch('builtins.input', side_effect=["invalid", "1,2"]):
        row, col = player.get_move()
        assert row == 1
        assert col == 2
    
    print("✓ Input validation test passed")


def run_all_tests():
    """Run all tests."""
    print("Running Tic-Tac-Toe Game Tests")
    print("=" * 40)
    
    try:
        test_board_creation()
        test_valid_moves()
        test_win_detection()
        test_draw_detection()
        test_player_creation()
        test_game_initialization()
        test_input_validation()
        
        print("\n" + "=" * 40)
        print("🎉 All tests passed! The game is working correctly.")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return False
    
    return True


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
