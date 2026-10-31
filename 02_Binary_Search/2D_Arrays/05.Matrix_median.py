# QUESTION:
# Given a row-wise sorted matrix with an odd number
# of rows and columns, find the median of all elements.

# APPROACH:
# Binary search over the possible value range.
# For each middle value, count how many matrix elements
# are less than or equal to it using binary search in
# each sorted row.
# Find the smallest value whose count reaches the median position.

from bisect import bisect_right


def matrix_median(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        raise ValueError("Matrix must not be empty")

    rows, cols = len(matrix), len(matrix[0])

    if any(len(row) != cols for row in matrix):
        raise ValueError("Matrix must be rectangular")

    low = min(row[0] for row in matrix)
    high = max(row[-1] for row in matrix)
    required = (rows * cols + 1) // 2

    while low <= high:
        mid = (low + high) // 2

        count = sum(bisect_right(row, mid) for row in matrix)

        if count < required:
            low = mid + 1
        else:
            high = mid - 1

    return low


# CODE:
# matrix = [
#     [1, 3, 5],
#     [2, 6, 9],
#     [3, 6, 9]
# ]
# print(matrix_median(matrix))  # 5

# TIME COMPLEXITY = O(R * log C * log V)
# SPACE COMPLEXITY = O(1) auxiliary
# V = maximum matrix value - minimum matrix value + 1
