# QUESTION:
# Given a non-negative integer N, set its rightmost unset bit.
# If all bits are already set in its binary representation,
# return N unchanged.
#
# Examples:
# Input: N = 6
# Binary: 110
# Output: 7
# Binary: 111
#
# Input: N = 15
# Binary: 1111
# Output: 15
#
# APPROACH:
# 1. Check whether N + 1 is a power of two.
# 2. If yes, all bits from the least significant bit
#    through the highest set bit are already set.
# 3. Otherwise, use N | (N + 1) to set the rightmost
#    unset bit.

def set_rightmost_unset_bit(n: int) -> int:
    if n < 0:
        raise ValueError("N must be non-negative")

    if (n + 1) & n == 0:
        return n

    return n | (n + 1)

# CODE:
# print(set_rightmost_unset_bit(6))   # 7
# print(set_rightmost_unset_bit(15))  # 15
# print(set_rightmost_unset_bit(10))  # 11
# print(set_rightmost_unset_bit(0))   # 1
# print(set_rightmost_unset_bit(8))   # 9

# TIME COMPLEXITY = O(1)
# SPACE COMPLEXITY = O(1)
