# QUESTION:
# Koko has piles of bananas and h hours to eat them.
# Find the minimum integer eating speed that allows her
# to finish all piles within h hours.
# Example: piles = [3, 6, 7, 11], h = 8 -> 4

# APPROACH:
# Binary search the eating speed from 1 to max(piles).
# For each speed, calculate total hours using ceiling division.

def min_eating_speed(piles: list[int], h: int) -> int:
    if not piles or h < len(piles):
        return -1

    left, right = 1, max(piles)

    while left <= right:
        mid = (left + right) // 2

        required_hours = sum(
            (pile + mid - 1) // mid for pile in piles
        )

        if required_hours <= h:
            right = mid - 1
        else:
            left = mid + 1

    return left


# CODE:
# print(min_eating_speed([3, 6, 7, 11], 8))  # 4

# TIME COMPLEXITY = O(N * log M)
# SPACE COMPLEXITY = O(1)
# M = maximum pile size
