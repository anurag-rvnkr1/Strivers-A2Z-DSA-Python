# QUESTION:
# Place N queens on an N x N chessboard such that
# no two queens attack each other.
#
# Return all distinct valid board configurations.
#
# Example:
# Input: n = 4
# Output:
# [
#   [".Q..", "...Q", "Q...", "..Q."],
#   ["..Q.", "Q...", "...Q", ".Q.."]
# ]
#
# APPROACH:
# 1. Place exactly one queen in each column.
# 2. Check whether the chosen row and both diagonals are safe.
# 3. Track occupied rows and diagonals using sets.
# 4. Place a queen and recursively process the next column.
# 5. Remove the queen and restore the sets during backtracking.


def solve_n_queens(n: int) -> list[list[str]]:
    if n <= 0:
        return []

    board = [["."] * n for _ in range(n)]

    used_rows = set()
    used_main_diagonals = set()  # row - col
    used_anti_diagonals = set()  # row + col

    result = []

    def solve(col: int) -> None:
        if col == n:
            result.append(
                ["".join(row) for row in board]
            )
            return

        for row in range(n):
            main_diag = row - col
            anti_diag = row + col

            if (
                row in used_rows
                or main_diag in used_main_diagonals
                or anti_diag in used_anti_diagonals
            ):
                continue

            # Place queen.
            board[row][col] = "Q"
            used_rows.add(row)
            used_main_diagonals.add(main_diag)
            used_anti_diagonals.add(anti_diag)

            solve(col + 1)

            # Backtrack.
            board[row][col] = "."
            used_rows.remove(row)
            used_main_diagonals.remove(main_diag)
            used_anti_diagonals.remove(anti_diag)

    solve(0)

    return result


# CODE:
# print(solve_n_queens(1))
# Output: [["Q"]]
#
# print(solve_n_queens(4))
# Output: two valid board configurations.
#
# print(solve_n_queens(2))  # []


# TIME COMPLEXITY = O(N!)
# Backtracking explores row placements with conflict pruning.
#
# SPACE COMPLEXITY = O(N^2)
# Board storage, plus O(N) recursion and tracking sets.
