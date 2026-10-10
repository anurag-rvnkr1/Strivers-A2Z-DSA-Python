"""
QUESTION:-

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees clockwise.

The rotation must be performed in-place.

Example 1:

Input:
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Output:
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]

Example 2:

Input:
[
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]

Output:
[
    [15, 13, 2, 5],
    [14, 3, 4, 1],
    [12, 6, 8, 9],
    [16, 7, 10, 11]
]
"""

"""
APPROACH:-

A 90-degree clockwise rotation can be achieved using two operations:

Step 1:
-> Transpose the matrix.
-> Swap matrix[i][j] with matrix[j][i].

Step 2:
-> Reverse every row.

Example:

Original:
1 2 3
4 5 6
7 8 9

After transpose:
1 4 7
2 5 8
3 6 9

After reversing each row:
7 4 1
8 5 2
9 6 3

This is the optimal in-place solution for LeetCode 48.
"""

# CODE:-

def rotate_matrix(matrix: list[list[int]]) -> None:
    n = len(matrix)

    # Step 1: Transpose.
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = (
                matrix[j][i],
                matrix[i][j]
            )

    # Step 2: Reverse every row.
    for row in matrix:
        row.reverse()


# TIME COMPLEXITY = O(N²)
# SPACE COMPLEXITY = O(1)
