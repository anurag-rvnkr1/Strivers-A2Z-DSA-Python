# QUESTION:
# Given a 0-indexed rowIndex, return that row of Pascal's Triangle.
# Example: rowIndex = 3 -> [1, 3, 3, 1]

# APPROACH:
# Generate each binomial coefficient from the previous one.
# This avoids calculating factorials.

def get_row(row_index: int) -> list[int]:
    row = [1] * (row_index + 1)
    coefficient = 1

    for col in range(1, row_index + 1):
        coefficient = coefficient * (row_index - col + 1) // col
        row[col] = coefficient

    return row


# CODE:
# print(get_row(3))  # [1, 3, 3, 1]

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(N)
