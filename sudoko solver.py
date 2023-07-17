def is_safe(board, row, col, num):
    # Check row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check 3x3 box
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False

    return True


def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None, None


def solve_sudoku(board):
    row, col = find_empty_cell(board)

    # If no empty cell found, the puzzle is solved
    if row is None and col is None:
        return True

    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num

            # Recursively try to solve the puzzle with the current number
            if solve_sudoku(board):
                return True

            # If the current number doesn't lead to a solution, backtrack and try the next one
            board[row][col] = 0

    # If no valid number is found, then the puzzle is unsolvable
    return False


# Example Sudoku board (0 represents an empty cell)
example_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(example_board):
    for row in example_board:
        print(row)
else:
    print("No solution exists for the given Sudoku puzzle.")
