# QUESTION:
# Given a number n and a bit position k, determine
# whether the k-th bit is set or not.
#
# Bit positions use 0-based indexing from the LSB.
#
# Example:
# Input: n = 4, k = 0
# Output: False
#
# APPROACH:
# 1. Create a mask using 1 << k.
# 2. Perform bitwise AND between n and the mask.
# 3. If the result is non-zero, the bit is set.

def check_kth_bit(n: int, k: int) -> bool:
    if k < 0:
        raise ValueError("Bit position cannot be negative")

    return (n & (1 << k)) != 0

# CODE:
# print(check_kth_bit(4, 0))   # False
# print(check_kth_bit(4, 2))   # True
# print(check_kth_bit(10, 1))  # True
# print(check_kth_bit(10, 0))  # False

# TIME COMPLEXITY = O(1)
# SPACE COMPLEXITY = O(1)
