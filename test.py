import pytest

from solution_finder import get_board, get_possible_queens_placement, find_solution


def test_possible_queens_placement():
    board = get_board()
    board[1][3] = 1
    possible_queens_placements = get_possible_queens_placement(board)
    assert possible_queens_placements[4][0] == 0

def test_find_solution():
    board = get_board()
    solution = find_solution(board, 8)
    column_indexes = [i for l in solution for (i,v) in enumerate(l) if v != 0]
    assert column_indexes == [0, 4, 7, 5, 2, 6, 1, 3]
