# QUESTION:
# Solve a 9 x 9 Sudoku puzzle by filling empty cells.
#
# Rules:
# 1. Every row contains digits 1 through 9 exactly once.
# 2. Every column contains digits 1 through 9 exactly once.
# 3. Every 3 x 3 box contains digits 1 through 9 exactly once.
# 4. Empty cells are represented by ".".
#
# APPROACH:
# 1. Find an empty cell.
# 2. Try digits from 1 to 9.
# 3. Check row, column and 3 x 3 box constraints.
# 4. Place a valid digit and recursively solve the board.
# 5. If the recursive call fails, restore the cell.
# 6. Return True when all cells are filled.


def solve_sudoku(board: list[list[str]]) -> bool:
    if len(board) != 9 or any(len(row) != 9 for row in board):
        raise ValueError("Sudoku board must be 9 x 9")

    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    # Initialize constraint sets and validate initial entries.
    for r in range(9):
        for c in range(9):
            value = board[r][c]

            if value == ".":
                continue

            if value not in "123456789":
                raise ValueError("Cells must contain digits 1-9 or '.'")

            box = (r // 3) * 3 + (c // 3)

            if (
                value in rows[r]
                or value in cols[c]
                or value in boxes[box]
            ):
                raise ValueError("Invalid Sudoku starting board")

            rows[r].add(value)
            cols[c].add(value)
            boxes[box].add(value)

    empty_cells = [
        (r, c)
        for r in range(9)
        for c in range(9)
        if board[r][c] == "."
    ]

    def solve(index: int) -> bool:
        if index == len(empty_cells):
            return True

        r, c = empty_cells[index]
        box = (r // 3) * 3 + (c // 3)

        for digit in "123456789":
            if (
                digit in rows[r]
                or digit in cols[c]
                or digit in boxes[box]
            ):
                continue

            # Place digit.
            board[r][c] = digit
            rows[r].add(digit)
            cols[c].add(digit)
            boxes[box].add(digit)

            if solve(index + 1):
                return True

            # Backtrack.
            board[r][c] = "."
            rows[r].remove(digit)
            cols[c].remove(digit)
            boxes[box].remove(digit)

        return False

    return solve(0)


# CODE:
# board = [
#     list("53..7...."),
#     list("6..195..."),
#     list(".98....6."),
#     list("8...6...3"),
#     list("4..8.3..1"),
#     list("7...2...6"),
#     list(".6....28."),
#     list("...419..5"),
#     list("....8..79")
# ]
#
# solved = solve_sudoku(board)
# print(solved)  # True
#
# for row in board:
#     print("".join(row))


# TIME COMPLEXITY = O(9^E)
# E = number of initially empty cells.
# Constraint checks are O(1) on average using sets.
#
# SPACE COMPLEXITY = O(E)
# Empty-cell list and recursive call stack.
# Constraint sets use O(81) space, which is constant for 9x9 Sudoku.
