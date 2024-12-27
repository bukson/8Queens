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

def find_solution() -> Board :
    def _find_solution(board:Board, queens_left: int) ->Board | None:
        if queens_left == 0:
            print([i for l in board for (i, v) in enumerate(l) if v != 0])
            return board
        possible_queens_board = get_possible_queens_placement(board)
        possible_queen_fields =  get_queen_positions(possible_queens_board)
        for field in possible_queen_fields:
            board[field[0]][field[1]] = 1
            maybe_solution = _find_solution(board, queens_left - 1)
            if maybe_solution is not None:
                return maybe_solution
            board[field[0]][field[1]] = 0
    board = get_board()
    return _find_solution(board, 8)

def find_solutions(unique: bool = False) -> list[Board]:
    solutions = []
    def _find_solutions(board:Board, queens_left: int) -> None:
        if queens_left == 0:
            # print([i for l in board for (i,v) in enumerate(l) if v != 0])
            if not unique:
                solutions.append(deepcopy(board))
            else:
                is_new_board_unique = is_board_in_set(board, solutions)
                if is_new_board_unique:
                    solutions.append(deepcopy(board))
            return
        possible_queens_board = get_possible_queens_placement(board)
        chosen_row = 8-queens_left
        for i in range(8):
            if possible_queens_board[chosen_row][i] == 1:
                board[chosen_row][i] = 1
                _find_solutions(board, queens_left - 1)
                board[chosen_row][i] = 0
        return



    board = get_board()
    _find_solutions(board, 8)
    return solutions

def get_column_indexes(board:Board) -> list[int]:
    return  [i for l in board for (i,v) in enumerate(l) if v != 0]

def rotate_board_clockwise(board: Board) -> Board   :
    return [[board[7 - row][col] for row in range(8)] for col in range(8)]

def mirror_board(board: Board) -> Board :
    return [[board[col][7-row] for row in range(8)] for col in range(8)]

def is_board_in_set(board: Board, board_set: list[Board]) -> bool:
    rotated_board = deepcopy(board)
    for i in range(4):
        rotated_board = rotate_board_clockwise(rotated_board)
        if rotated_board in board_set:
            return False
        rotated_mirrored_board = mirror_board(rotated_board)
        if rotated_mirrored_board in board_set:
            return False
    return True