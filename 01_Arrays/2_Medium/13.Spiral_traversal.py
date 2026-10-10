"""
QUESTION:-

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input:
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Output:
[1, 2, 3, 6, 9, 8, 7, 4, 5]

Example 2:

Input:
[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

Output:
[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
"""

"""
APPROACH:-

Maintain four boundaries:

-> top
-> bottom
-> left
-> right

At every iteration:

1. Traverse the top row from left to right.
2. Move top downward.
3. Traverse the right column from top to bottom.
4. Move right leftward.
5. If rows remain, traverse the bottom row from right to left.
6. Move bottom upward.
7. If columns remain, traverse the left column from bottom to top.
8. Move left rightward.

Continue until the boundaries cross.

The boundary checks are important for avoiding duplicate elements in
single-row or single-column matrices.
"""

# CODE:-

def spiral_order(matrix: list[list[int]]) -> list[int]:
    if not matrix or not matrix[0]:
        return []

    result = []

    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:

        # Traverse top row.
        for col in range(left, right + 1):
            result.append(matrix[top][col])

        top += 1

        # Traverse right column.
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])

        right -= 1

        # Traverse bottom row.
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])

            bottom -= 1

        # Traverse left column.
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])

            left += 1

    return result


# TIME COMPLEXITY = O(M × N)
# SPACE COMPLEXITY = O(M × N) for the output
