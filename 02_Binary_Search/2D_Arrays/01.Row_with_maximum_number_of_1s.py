# QUESTION:
# Given a binary matrix where every row is sorted,
# return the 0-based index of the first row containing
# the maximum number of 1s. Return -1 if no 1 exists.

# APPROACH:
# Start at the top-right corner.
# If the current value is 1, move left and record the row.
# If it is 0, move down to the next row.
# Each move eliminates one row or one column.

def row_with_max_1s(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        return -1

    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1
    answer = -1

    while row < rows and col >= 0:
        if matrix[row][col] == 1:
            answer = row
            col -= 1
        else:
            row += 1

    return answer


# CODE:
# matrix = [
#     [0, 1, 1, 1],
#     [0, 0, 1, 1],
#     [1, 1, 1, 1],
#     [0, 0, 0, 0]
# ]
# print(row_with_max_1s(matrix))  # 2

# TIME COMPLEXITY = O(R + C)
# SPACE COMPLEXITY = O(1)
