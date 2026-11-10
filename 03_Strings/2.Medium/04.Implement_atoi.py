# QUESTION:
# Implement my_atoi(s), which converts a string into a
# 32-bit signed integer.
#
# Rules:
# 1. Ignore leading spaces.
# 2. Read an optional '+' or '-' sign.
# 3. Read consecutive digits until a non-digit is encountered.
# 4. Return 0 if no digits are found.
# 5. Clamp the result to the 32-bit signed integer range.
#
# APPROACH:
# 1. Skip leading spaces.
# 2. Determine the sign.
# 3. Process consecutive digits.
# 4. Stop when a non-digit is encountered.
# 5. Clamp the result between -2^31 and 2^31 - 1.


def my_atoi(s: str) -> int:
    INT_MIN = -(2 ** 31)
    INT_MAX = (2 ** 31) - 1

    i = 0
    n = len(s)

    # Skip leading spaces.
    while i < n and s[i] == ' ':
        i += 1

    # Handle optional sign.
    sign = 1

    if i < n and s[i] in '+-':
        if s[i] == '-':
            sign = -1
        i += 1

    # Convert consecutive digits.
    result = 0

    while i < n and s[i].isdigit() and s[i].isascii():
        digit = ord(s[i]) - ord('0')

        result = result * 10 + digit

        # Clamp while processing to prevent unnecessary growth.
        if sign == 1 and result > INT_MAX:
            return INT_MAX

        if sign == -1 and result > 2 ** 31:
            return INT_MIN

        i += 1

    return max(INT_MIN, min(INT_MAX, sign * result))


# CODE:
# print(my_atoi("42"))                  # 42
# print(my_atoi("   -42"))              # -42
# print(my_atoi("4193 with words"))     # 4193
# print(my_atoi("words and 987"))       # 0
# print(my_atoi("-91283472332"))        # -2147483648
# print(my_atoi("91283472332"))         # 2147483647
# print(my_atoi("+1"))                  # 1
# print(my_atoi("+-12"))                # 0


# TIME COMPLEXITY = O(N)
# At most one traversal of the string.
#
# SPACE COMPLEXITY = O(1)
# Only a constant number of variables are used.
