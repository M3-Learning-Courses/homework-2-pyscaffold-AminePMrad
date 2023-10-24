import pytest
from io import StringIO
import sys
from tic_tac_toe.tic_tac_toe import print_board, check_winner, is_draw, main

def test_print_board():
    board = [["X", "O", "X"], [" ", "X", "O"], ["O", "X", " "]]
    expected_output = "X | O | X\n---------\n  | X | O\n---------\nO | X |  \n---------\n"
    output = StringIO()
    sys.stdout = output
    print_board(board)
    sys.stdout = sys.__stdout__
    assert output.getvalue() == expected_output

def test_check_winner():
    # Test when X wins in the first row
    board_x_win_row = [
        ["X", "X", "X"],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    assert check_winner(board_x_win_row, "X") is True
# Test when X wins in the second row
    board_x_win_row = [
        [" ", " ", " "],
        ["X", "X", "X"],
        [" ", " ", " "]
    ]
    assert check_winner(board_x_win_row, "X") is True
    # Test when X wins in the third row
    board_x_win_row = [
        [" ", " ", " "],
        [" ", " ", " "],
        ["X", "X", "X"]
    ]
    assert check_winner(board_x_win_row, "X") is True
    
# Test when X wins in the first col
    board_x_win_col = [
        ["X", " ", " "],
        ["X", " ", " "],
        ["X", " ", " "]
    ]
    assert check_winner(board_x_win_col, "X") is True

    # Test when X wins in the second col
    board_x_win_col = [
        [" ", "X", " "],
        [" ", "X", " "],
        [" ", "X", " "]
    ]
    assert check_winner(board_x_win_col, "X") is True

    # Test when X wins in the third col
    board_x_win_col = [
        [" ", " ", "X"],
        [" ", " ", "X"],
        [" ", " ", "X"]
    ]
    assert check_winner(board_x_win_col, "X") is True

    # Test when X wins in the first diag
    board_x_win_diag = [
        ["X", " ", " "],
        [" ", "X", " "],
        [" ", " ", "X"]
    ]
    assert check_winner(board_x_win_diag, "X") is True

    # Test when X wins in the second diag
    board_x_win_diag = [
        [" ", " ", "X"],
        [" ", "X", " "],
        ["X", " ", " "]
    ]
    assert check_winner(board_x_win_diag, "X") is True

    # Test when O wins in the first row
    board_O_win_row = [
        ["O", "O", "O"],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    assert check_winner(board_O_win_row, "O") is True
# Test when O wins in the second row
    board_O_win_row = [
        [" ", " ", " "],
        ["O", "O", "O"],
        [" ", " ", " "]
    ]
    assert check_winner(board_O_win_row, "o") is True
    # Test when O wins in the third row
    board_O_win_row = [
        [" ", " ", " "],
        [" ", " ", " "],
        ["O", "O", "O"]
    ]
    assert check_winner(board_O_win_row, "O") is True
    
# Test when O wins in the first col
    board_O_win_col = [
        ["O", " ", " "],
        ["O", " ", " "],
        ["O", " ", " "]
    ]
    assert check_winner(board_O_win_col, "O") is True

    # Test when O wins in the second col
    board_O_win_col = [
        [" ", "O", " "],
        [" ", "O", " "],
        [" ", "O", " "]
    ]
    assert check_winner(board_O_win_col, "O") is True

    # Test when O wins in the third col
    board_O_win_col = [
        [" ", " ", "O"],
        [" ", " ", "O"],
        [" ", " ", "O"]
    ]
    assert check_winner(board_O_win_col, "O") is True

    # Test when O wins in the first diag
    board_O_win_diag = [
        ["O", " ", " "],
        [" ", "O", " "],
        [" ", " ", "O"]
    ]
    assert check_winner(board_O_win_diag, "O") is True

    # Test when O wins in the second diag
    board_O_win_diag = [
        [" ", " ", "O"],
        [" ", "O", " "],
        ["O", " ", " "]
    ]
    assert check_winner(board_O_win_diag, "O") is True

    # Test when there is no winner
    board_no_winner = [
        ["X", "O", "X"],
        ["X", "O", "O"],
        ["O", "X", "X"]
    ]
    assert check_winner(board_no_winner, "O") is False

def test_is_draw():
    board = [["X", "O", "X"], ["O", "X", "X"], ["X", "X", "O"]]
    assert is_draw(board)

def test_game():
    user_input = ["0", "0", "0", "1", "1", "1", "0", "2", "2", "0"]
    expected_output = "Player X's turn\nPlayer O's turn\nPlayer X's turn\nPlayer O's turn\nPlayer X's turn\nPlayer X wins!\n"
    output = StringIO()
    input_str = '\n'.join(user_input) + '\n'
    sys.stdout = output
    sys.stdin = StringIO(input_str)
    main()
    sys.stdout = sys.__stdout__
    sys.stdin = sys.__stdin__

if __name__ == '__main__':
    pytest.main([__file__])
