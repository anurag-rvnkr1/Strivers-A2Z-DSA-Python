# QUESTION:
# Ship packages in their given order within a specified number
# of days. Find the minimum ship capacity needed.
# Example: weights = [1,2,3,4,5,6,7,8,9,10], days = 5 -> 15

# APPROACH:
# Binary search ship capacity between max(weights) and sum(weights).
# For each capacity, greedily load packages in order and count days.

def ship_within_days(weights: list[int], days: int) -> int:
    if not weights or days <= 0:
        return -1

    def can_ship(capacity: int) -> bool:
        used_days = 1
        current_load = 0

        for weight in weights:
            if current_load + weight > capacity:
                used_days += 1
                current_load = 0

            current_load += weight

            if used_days > days:
                return False

        return True

    left, right = max(weights), sum(weights)

    while left <= right:
        mid = (left + right) // 2

        if can_ship(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left


# CODE:
# print(ship_within_days([1,2,3,4,5,6,7,8,9,10], 5))  # 15

# TIME COMPLEXITY = O(N * log S)
# SPACE COMPLEXITY = O(1)
# S = sum of all package weights
