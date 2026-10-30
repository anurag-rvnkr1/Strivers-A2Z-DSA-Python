# QUESTION:
# Given a non-negative integer x, return the floor of its square root.
# Example: x = 5 -> 2

# APPROACH:
# Binary search for the largest integer whose square is <= x.
# Compare using mid <= x // mid to avoid multiplication overflow
# in languages with fixed-width integers.

def floor_sqrt(x: int) -> int:
    if x < 0:
        raise ValueError("x must be non-negative")

    left, right = 0, x
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        if mid == 0 or mid <= x // mid:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer


# CODE:
# print(floor_sqrt(5))   # 2
# print(floor_sqrt(16))  # 4

# TIME COMPLEXITY = O(log X)
# SPACE COMPLEXITY = O(1)
