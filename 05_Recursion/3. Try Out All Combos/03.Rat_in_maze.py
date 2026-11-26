# QUESTION:
# A rat starts at (0, 0) in an N x N maze.
# It must reach (N-1, N-1).
#
# 1 represents an open cell.
# 0 represents a blocked cell.
#
# Allowed directions: U, D, L, R.
# Return all valid paths in lexicographical order.
#
# Example:
# maze = [
#   [1, 0, 0, 0],
#   [1, 1, 0, 1],
#   [1, 1, 0, 0],
#   [0, 1, 1, 1]
# ]
#
# Output: ["DDRDRR", "DRDDRR"]
#
# APPROACH:
# 1. Begin at the source cell.
# 2. Explore all four possible directions.
# 3. Do not visit blocked or already visited cells.
# 4. Mark the current cell during recursion.
# 5. Restore the cell during backtracking.
# 6. Save the path when the destination is reached.


def find_path(maze: list[list[int]]) -> list[str]:
    n = len(maze)

    if n == 0 or len(maze[0]) != n:
        return []

    if maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
        return []

    result = []
    path = []

    directions = [
        (-1, 0, "U"),
        (1, 0, "D"),
        (0, -1, "L"),
        (0, 1, "R")
    ]

    def solve(r: int, c: int) -> None:
        if r == n - 1 and c == n - 1:
            result.append("".join(path))
            return

        # Mark current cell visited.
        maze[r][c] = 0

        for dr, dc, move in directions:
            nr = r + dr
            nc = c + dc

            if (
                0 <= nr < n
                and 0 <= nc < n
                and maze[nr][nc] == 1
            ):
                path.append(move)
                solve(nr, nc)
                path.pop()

        # Restore original cell.
        maze[r][c] = 1

    solve(0, 0)

    return sorted(result)


# CODE:
# maze = [
#     [1, 0, 0, 0],
#     [1, 1, 0, 1],
#     [1, 1, 0, 0],
#     [0, 1, 1, 1]
# ]
#
# print(find_path(maze))
# Output: ["DDRDRR", "DRDDRR"]
#
# print(find_path([[1, 0], [0, 1]]))  # []


# TIME COMPLEXITY = Exponential
# A loose upper bound is O(4^(N*N)).
# The number of valid paths can itself be exponential.
#
# SPACE COMPLEXITY = O(N*N) auxiliary recursion depth
# Excluding the output paths.
