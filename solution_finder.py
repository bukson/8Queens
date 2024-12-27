from copy import deepcopy
Board = list[list[int]]
Field = list[int]

def get_board(default_value=0) -> Board:
    board = list()
    for i in range(8):
        board.append([default_value] * 8)
    return board

def get_queen_positions(board: Board) -> list[Field]:
    result = []
    for y in range(8):
        for x in range(8):
            if board[y][x] == 1:
                result.append([y, x])
    return result

def is_valid_field(field: Field) -> bool:
    return 0 <= field[0] < 8 and 0 <= field[1] < 8

def get_possible_queens_placement(board: Board) -> list[Field]:
    placement_board = get_board(default_value=1)
    queen_positions = get_queen_positions(board)
    for queen_position in queen_positions:
        for y in range(8):
            placement_board[y][queen_position[1]] = 0
        for x in range(8):
            placement_board[queen_position[0]][x] = 0
        # + +
        ghost_queen_position = deepcopy(queen_position)
        while is_valid_field(ghost_queen_position):
            placement_board[ghost_queen_position[0]][ghost_queen_position[1]] = 0
            ghost_queen_position[0] += 1
            ghost_queen_position[1] += 1
        # + -
        ghost_queen_position = deepcopy(queen_position)
        while is_valid_field(ghost_queen_position):
            placement_board[ghost_queen_position[0]][ghost_queen_position[1]] = 0
            ghost_queen_position[0] += 1
            ghost_queen_position[1] -= 1
        # - +
        ghost_queen_position = deepcopy(queen_position)
        while is_valid_field(ghost_queen_position):
            placement_board[ghost_queen_position[0]][ghost_queen_position[1]] = 0
            ghost_queen_position[0] -= 1
            ghost_queen_position[1] += 1
        # - -
        ghost_queen_position = deepcopy(queen_position)
        while is_valid_field(ghost_queen_position):
            placement_board[ghost_queen_position[0]][ghost_queen_position[1]] = 0
            ghost_queen_position[0] -= 1
            ghost_queen_position[1] -= 1
    return placement_board

def find_solution(board:Board, queens_left: int) ->Board | None:
    if queens_left == 0:
        return board
    possible_queens_board = get_possible_queens_placement(board)
    possible_queen_fields =  get_queen_positions(possible_queens_board)
    for field in possible_queen_fields:
        board_copy = deepcopy(board)
        board_copy[field[0]][field[1]] = 1
        maybe_solution = find_solution(board_copy, queens_left - 1)
        if maybe_solution is not None:
            return maybe_solution