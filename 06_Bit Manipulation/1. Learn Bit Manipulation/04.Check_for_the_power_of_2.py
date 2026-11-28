# QUESTION:
# Given an integer n, determine whether it is a power of 2.
#
# Examples:
# Input: n = 1   Output: True
# Input: n = 16  Output: True
# Input: n = 6   Output: False
#
# APPROACH:
# A positive power of two contains exactly one set bit.
#
# 1. Reject numbers less than or equal to zero.
# 2. Check n & (n - 1).
# 3. If the result is zero, n is a power of two.

def is_power_of_two(n: int) -> bool:
    if n <= 0:
        return False

    return (n & (n - 1)) == 0

# CODE:
# print(is_power_of_two(1))    # True
# print(is_power_of_two(16))   # True
# print(is_power_of_two(6))    # False
# print(is_power_of_two(0))    # False
# print(is_power_of_two(1024)) # True

# TIME COMPLEXITY = O(1)
# SPACE COMPLEXITY = O(1)
