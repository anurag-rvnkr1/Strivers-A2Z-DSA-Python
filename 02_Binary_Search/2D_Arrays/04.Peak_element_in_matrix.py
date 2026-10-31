# QUESTION:
# Find any peak element in a 2D matrix.
# A peak is strictly greater than its left, right,
# top, and bottom neighbors.
# Return its position as [row, col].
# The matrix has no equal adjacent cells and is
# surrounded by an outer boundary of -1.

# APPROACH:
# Binary search over columns.
# For each middle column, find its maximum element.
# If it is greater than its vertical neighbors, it is a peak.
# Otherwise, move toward the side with the larger vertical neighbor.

def find_peak_grid(matrix: list[list[int]]) -> list[int]:
    if not matrix or not matrix[0]:
        return [-1, -1]

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, cols - 1

    while left <= right:
        mid_col = (left + right) // 2

        # Find the maximum element in this column.
        max_row = max(range(rows), key=lambda r: matrix[r][mid_col])
        value = matrix[max_row][mid_col]

        left_value = matrix[max_row][mid_col - 1] if mid_col > 0 else float("-inf")
        right_value = (
            matrix[max_row][mid_col + 1]
            if mid_col < cols - 1
            else float("-inf")
        )

        if value > left_value and value > right_value:
            return [max_row, mid_col]

        if left_value > value:
            right = mid_col - 1
        else:
            left = mid_col + 1

    return [-1, -1]


# CODE:
# matrix = [[1, 4], [3, 2]]
# print(find_peak_grid(matrix))  # [0, 1]

# TIME COMPLEXITY = O(R * log C)
# SPACE COMPLEXITY = O(1)
