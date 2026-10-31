# QUESTION:
# Search for a target in a matrix where:
# 1. Every row is sorted in ascending order.
# 2. The first element of each row is greater than
#    the last element of the previous row.
# Return True if found, otherwise False.

# APPROACH:
# Treat the matrix as a single sorted 1D array.
# Convert a 1D index into matrix coordinates:
# row = mid // cols, col = mid % cols.

def search_matrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        value = matrix[mid // cols][mid % cols]

        if value == target:
            return True
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# CODE:
# matrix = [
#     [1, 3, 5, 7],
#     [10, 11, 16, 20],
#     [23, 30, 34, 60]
# ]
# print(search_matrix(matrix, 3))  # True

# TIME COMPLEXITY = O(log(R * C))
# SPACE COMPLEXITY = O(1)
