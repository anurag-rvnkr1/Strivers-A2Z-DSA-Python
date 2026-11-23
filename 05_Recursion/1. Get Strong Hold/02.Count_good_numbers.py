# QUESTION:
# A digit string is good if:
# 1. Digits at even indices are even: 0, 2, 4, 6, 8.
# 2. Digits at odd indices are prime: 2, 3, 5, 7.
#
# Given an integer n, return the number of good digit strings
# of length n modulo 10^9 + 7.
#
# Examples:
# Input: n = 1   Output: 5
# Input: n = 4   Output: 400
# Input: n = 50  Output: 564908303
#
# APPROACH:
# 1. Even positions have 5 possible digits.
# 2. Odd positions have 4 possible digits.
# 3. Recursively calculate the number of possibilities.
# 4. Use modular exponentiation to avoid large intermediate values.
#
# The implementation uses fast recursive power calculation.


MOD = 10**9 + 7


def power(base: int, exponent: int) -> int:
    # Base case.
    if exponent == 0:
        return 1

    half = power(base, exponent // 2)
    result = (half * half) % MOD

    if exponent % 2 == 1:
        result = (result * base) % MOD

    return result


def count_good_numbers(n: int) -> int:
    if n <= 0:
        return 0

    even_positions = (n + 1) // 2
    odd_positions = n // 2

    return (
        power(5, even_positions)
        * power(4, odd_positions)
    ) % MOD


# CODE:
# print(count_good_numbers(1))   # 5
# print(count_good_numbers(4))   # 400
# print(count_good_numbers(50))  # 564908303
# print(count_good_numbers(0))   # 0


# TIME COMPLEXITY = O(log N)
# Two recursive modular exponentiation calculations.
#
# SPACE COMPLEXITY = O(log N)
# Recursive call stack.
