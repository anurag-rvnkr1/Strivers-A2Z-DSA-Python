# QUESTION:
# Given an integer N, determine whether it is odd or even.
#
# APPROACH:
# 1. Check the least significant bit using N & 1.
# 2. If the result is 1, the number is odd.
# 3. Otherwise, the number is even.

def odd_even(n: int) -> str:
    if n & 1:
        return "odd"

    return "even"

# CODE:
# print(odd_even(1))    # odd
# print(odd_even(10))   # even
# print(odd_even(15))   # odd
# print(odd_even(100))  # even
# print(odd_even(0))    # even

# TIME COMPLEXITY = O(1)
# SPACE COMPLEXITY = O(1)
