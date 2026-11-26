# QUESTION:
# Given an m x n character grid and a word,
# determine whether the word exists in the grid.
#
# The word can be constructed from adjacent cells
# horizontally or vertically.
# A cell cannot be used more than once in a path.
#
# Example:
# board = [
#   ["A", "B", "C", "E"],
#   ["S", "F", "C", "S"],
#   ["A", "D", "E", "E"]
# ]
# word = "ABCCED"
# Output: True
#
# APPROACH:
# 1. Try starting from every cell matching the first character.
# 2. Explore four directions recursively.
# 3. Mark a visited cell temporarily.
# 4. Restore the cell after exploring.
# 5. Return True when every character is matched.


def exist(board: list[list[str]], word: str) -> bool:
    if not word:
        return True

    if not board or not board[0]:
        return False

    rows = len(board)
    cols = len(board[0])

    if len(word) > rows * cols:
        return False

    def solve(r: int, c: int, index: int) -> bool:
        if index == len(word):
            return True

        if (
            r < 0 or r >= rows
            or c < 0 or c >= cols
            or board[r][c] != word[index]
        ):
            return False

        # Mark current cell as visited.
        char = board[r][c]
        board[r][c] = "#"

        found = (
            solve(r - 1, c, index + 1)
            or solve(r + 1, c, index + 1)
            or solve(r, c - 1, index + 1)
            or solve(r, c + 1, index + 1)
        )

        # Restore original character.
        board[r][c] = char

        return found

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0]:
                if solve(r, c, 0):
                    return True

    return False


# CODE:
# board = [
#     ["A", "B", "C", "E"],
#     ["S", "F", "C", "S"],
#     ["A", "D", "E", "E"]
# ]
#
# print(exist(board, "ABCCED"))  # True
# print(exist(board, "SEE"))     # True
# print(exist(board, "ABCB"))    # False
#
# The original board is restored after every search.


# TIME COMPLEXITY = O(M * N * 3^L)
# M,N = grid dimensions; L = word length.
# After the first step, at most three unvisited directions
# remain at each step.
#
# SPACE COMPLEXITY = O(L)
# Recursive call stack.
