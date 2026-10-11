"""
QUESTION:-

Given an m x n integer matrix, if an element is 0, set its entire row
and column to 0.

The operation must be performed in-place.

Example 1:
Input:
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

Output:
[
    [1, 0, 1],
    [0, 0, 0],
    [1, 0, 1]
]

Example 2:
Input:
matrix = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]

Output:
[
    [0, 0, 0, 0],
    [0, 4, 5, 0],
    [0, 3, 1, 0]
]
"""

"""
APPROACH:-

Use the first row and first column as marker storage.

-> Check whether the first row originally contains a zero.
-> Check whether the first column originally contains a zero.
-> For every zero outside the first row/column:
      matrix[i][0] = 0
      matrix[0][j] = 0
-> Use these markers to zero the appropriate rows and columns.
-> Finally process the first row and first column separately.

This avoids using additional row/column arrays.

This is the optimal O(1) extra-space solution for LeetCode 73.
"""

# CODE:-

def set_zeroes(matrix: list[list[int]]) -> None:
    rows = len(matrix)
    cols = len(matrix[0])

    first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
    first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

    # Use first row and first column as markers.
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Zero marked rows.
    for i in range(1, rows):
        if matrix[i][0] == 0:
            for j in range(1, cols):
                matrix[i][j] = 0

    # Zero marked columns.
    for j in range(1, cols):
        if matrix[0][j] == 0:
            for i in range(1, rows):
                matrix[i][j] = 0

    # Process first row.
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0

    # Process first column.
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0


# TIME COMPLEXITY = O(M × N)
# SPACE COMPLEXITY = O(1)
