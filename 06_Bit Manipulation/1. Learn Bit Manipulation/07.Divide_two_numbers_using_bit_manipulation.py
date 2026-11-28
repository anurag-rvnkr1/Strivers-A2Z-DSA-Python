# QUESTION:
# Given dividend and divisor, calculate the integer quotient
# without using multiplication, division or modulo operators
# in the algorithm.
#
# The quotient is truncated toward zero.
#
# Example:
# Input: dividend = 10, divisor = 3
# Output: 3
#
# Input: dividend = 7, divisor = -2
# Output: -3
#
# APPROACH:
# 1. Handle division by zero.
# 2. Determine the sign of the result.
# 3. Convert both numbers to positive values.
# 4. Use left shifts to find the largest multiple
#    of divisor that fits into dividend.
# 5. Subtract that multiple and update the quotient.
# 6. Restore the sign.
# 7. Clamp to signed 32-bit integer bounds.

def divide_two_integers(dividend: int, divisor: int) -> int:
    INT_MIN = -(2 ** 31)
    INT_MAX = (2 ** 31) - 1

    if divisor == 0:
        raise ZeroDivisionError("Division by zero")

    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    negative = (dividend < 0) != (divisor < 0)

    a = abs(dividend)
    b = abs(divisor)

    quotient = 0

    while a >= b:
        shift = 0

        while a >= (b << (shift + 1)):
            shift += 1

        quotient += 1 << shift
        a -= b << shift

    if negative:
        quotient = -quotient

    return max(INT_MIN, min(INT_MAX, quotient))

# CODE:
# print(divide_two_integers(10, 3))    # 3
# print(divide_two_integers(7, -2))    # -3
# print(divide_two_integers(-7, 2))    # -3
# print(divide_two_integers(16, 4))    # 4
# print(divide_two_integers(1, 2))     # 0
# print(divide_two_integers(-7, -2))  # 3
# print(divide_two_integers(-(2**31), -1))  # 2147483647

# TIME COMPLEXITY = O((log N)^2)
# There are O(log N) subtraction rounds and each round
# finds a shift using O(log N) comparisons in this version.
#
# SPACE COMPLEXITY = O(1)
# Only constant extra variables are used.
