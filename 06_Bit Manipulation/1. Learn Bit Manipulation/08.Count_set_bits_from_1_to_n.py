# QUESTION:
# Given an integer N, find the total number of set bits
# in the binary representations of all integers from 1 to N.
#
# Example:
# Input: N = 4
# Output: 5
#
# Explanation:
# 1 -> 001 -> 1 set bit
# 2 -> 010 -> 1 set bit
# 3 -> 011 -> 2 set bits
# 4 -> 100 -> 1 set bit
# Total = 5
#
# APPROACH:
# 1. Find the largest power of 2 less than or equal to N.
# 2. Let x be its exponent, so power = 2^x.
# 3. Count set bits contributed by complete ranges:
#       x * 2^(x-1)
# 4. Count the leading set bits in the remaining range:
#       N - 2^x + 1
# 5. Recursively count set bits from 1 to N - 2^x.
# 6. Return the sum.

def count_set_bits(n: int) -> int:
    if n <= 0:
        return 0

    if n == 1:
        return 1

    # Find the greatest power of 2 <= n.
    x = n.bit_length() - 1
    power = 1 << x

    # Count set bits from 1 to 2^x - 1.
    bits_before = x * (1 << (x - 1))

    # Count occurrences of the highest bit.
    highest_bit_count = n - power + 1

    # Count set bits in the remaining numbers.
    remaining = n - power

    return (
        bits_before
        + highest_bit_count
        + count_set_bits(remaining)
    )

# CODE:
# print(count_set_bits(4))    # 5
# print(count_set_bits(10))   # 17
# print(count_set_bits(17))   # 35
# print(count_set_bits(0))    # 0
# print(count_set_bits(1))    # 1

# TIME COMPLEXITY = O(log N)
# Each recursive call removes the highest power of two,
# so there are O(log N) calls.
#
# SPACE COMPLEXITY = O(log N)
# Recursive call stack.
