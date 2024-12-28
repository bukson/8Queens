import pytest

from solution_finder import get_board, get_possible_queens_placement, find_solution, find_solutions, get_column_indexes, \
    rotate_board_clockwise, mirror_board


def test_possible_queens_placement():
    board = get_board()
    board[1][3] = 1
    possible_queens_placements = get_possible_queens_placement(board)
    assert possible_queens_placements[4][0] == 0


def test_find_solution():
    solution = find_solution()
    column_indexes = get_column_indexes(solution)
    assert column_indexes == [0, 6, 4, 7, 1, 3, 5, 2]


@pytest.mark.parametrize("unique, expected_number", [(False, 92), (True, 12), ])
def test_find_solutions(unique, expected_number):
    non_unique_solutions = find_solutions(unique=unique)
    assert len(non_unique_solutions) == expected_number


def test_rotate_board_clockwise():
    board = [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [9, 10, 11, 12, 13, 14, 15, 16],
        [17, 18, 19, 20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29, 30, 31, 32],
        [33, 34, 35, 36, 37, 38, 39, 40],
        [41, 42, 43, 44, 45, 46, 47, 48],
        [49, 50, 51, 52, 53, 54, 55, 56],
        [57, 58, 59, 60, 61, 62, 63, 64],
    ]
    expected_board = [
        [57, 49, 41, 33, 25, 17, 9, 1],
        [58, 50, 42, 34, 26, 18, 10, 2],
        [59, 51, 43, 35, 27, 19, 11, 3],
        [60, 52, 44, 36, 28, 20, 12, 4],
        [61, 53, 45, 37, 29, 21, 13, 5],
        [62, 54, 46, 38, 30, 22, 14, 6],
        [63, 55, 47, 39, 31, 23, 15, 7],
        [64, 56, 48, 40, 32, 24, 16, 8]
    ]
    assert rotate_board_clockwise(board) == expected_board


def test_mirror_board():
    board = get_board()
    board[1] = [0, 0, 0, 1, 0, 0, 0, 0]
    board[5] = [0, 0, 0, 0, 0, 1, 0, 0]
    mirrored_board = mirror_board(board)
    assert mirrored_board[0] == board[0]
    assert mirrored_board[1] == [0, 0, 0, 0, 1, 0, 0, 0]
    assert mirrored_board[5] == [0, 0, 1, 0, 0, 0, 0, 0]
