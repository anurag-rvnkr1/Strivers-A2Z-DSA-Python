# QUESTION:
# Given n and m, find the integer nth root of m.
# Return -1 if no integer root exists.
# Example: n = 3, m = 27 -> 3
# Example: n = 3, m = 9 -> -1

# APPROACH:
# Binary search for a value whose nth power equals m.
# Stop multiplication early when the product exceeds m.

def compare_power(base: int, exponent: int, target: int) -> int:
    """
    Returns:
        -1 if base ** exponent < target
         0 if base ** exponent == target
         1 if base ** exponent > target
    """
    product = 1

    for _ in range(exponent):
        product *= base

        if product > target:
            return 1

    if product == target:
        return 0

    return -1


def nth_root(n: int, m: int) -> int:
    if n <= 0 or m < 0:
        return -1

    if m in (0, 1):
        return m

    left, right = 1, m

    while left <= right:
        mid = (left + right) // 2
        result = compare_power(mid, n, m)

        if result == 0:
            return mid
        elif result < 0:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# CODE:
# print(nth_root(3, 27))  # 3
# print(nth_root(3, 9))   # -1

# TIME COMPLEXITY = O(N * log M)
# SPACE COMPLEXITY = O(1)
