# QUESTION:
# An array contains numbers from 1 to n, with one number repeated
# and another missing. Return [repeating, missing].
# Example: [3, 1, 3] -> [3, 2]

# APPROACH:
# Use the expected sum and expected sum of squares to derive
# the repeating and missing numbers from two equations.

def find_repeating_and_missing(nums: list[int]) -> list[int]:
    n = len(nums)

    expected_sum = n * (n + 1) // 2
    expected_square_sum = n * (n + 1) * (2 * n + 1) // 6

    actual_sum = sum(nums)
    actual_square_sum = sum(num * num for num in nums)

    difference = expected_sum - actual_sum       # missing - repeating
    square_difference = expected_square_sum - actual_square_sum

    total = square_difference // difference      # missing + repeating

    missing = (difference + total) // 2
    repeating = total - missing

    return [repeating, missing]


# CODE:
# print(find_repeating_and_missing([3, 1, 3]))  # [3, 2]

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
