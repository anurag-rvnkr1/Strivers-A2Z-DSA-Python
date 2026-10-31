# QUESTION:
# Search for a target in a matrix where every row and
# every column is sorted in ascending order.
# Return True if found, otherwise False.

# APPROACH:
# Start from the top-right corner.
# If the current value is greater than target, move left.
# If it is smaller, move down.
# Each move eliminates a row or column.

def search_matrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1

    while row < rows and col >= 0:
        value = matrix[row][col]

        if value == target:
            return True
        elif value > target:
            col -= 1
        else:
            row += 1

    return False


# CODE:
# matrix = [
#     [1, 4, 7, 11, 15],
#     [2, 5, 8, 12, 19],
#     [3, 6, 9, 16, 22],
#     [10, 13, 14, 17, 24],
#     [18, 21, 23, 26, 30]
# ]
# print(search_matrix(matrix, 5))   # True
# print(search_matrix(matrix, 20))  # False

# TIME COMPLEXITY = O(R + C)
# SPACE COMPLEXITY = O(1)
