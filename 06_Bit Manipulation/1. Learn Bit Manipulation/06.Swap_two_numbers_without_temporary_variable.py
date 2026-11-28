# QUESTION:
# Given two numbers a and b, swap their values without
# using a temporary variable.
#
# Example:
# Input: a = 13, b = 9
# Output: 9 13
#
# APPROACH:
# Use XOR operations.
#
# 1. a = a ^ b
# 2. b = a ^ b
# 3. a = a ^ b
#
# XOR has the property:
# x ^ x = 0
# x ^ 0 = x

def swap_numbers(a: int, b: int) -> tuple[int, int]:
    a = a ^ b
    b = a ^ b
    a = a ^ b

    return a, b

# CODE:
# print(swap_numbers(13, 9))  # (9, 13)
# print(swap_numbers(5, 5))   # (5, 5)
# print(swap_numbers(0, 7))   # (7, 0)
# print(swap_numbers(-3, 8))  # (8, -3)

# TIME COMPLEXITY = O(1)
# SPACE COMPLEXITY = O(1)
