# QUESTION:
# Implement atoi using recursion.
# Convert a string into an integer without using built-in
# integer conversion functions.
#
# Return -1 if the string contains invalid characters.
#
# Examples:
# Input: "123"    Output: 123
# Input: "21a"    Output: -1
# Input: "-456"   Output: -456
#
# APPROACH:
# 1. Recursively process the string from right to left.
# 2. Convert each digit using its ASCII value.
# 3. If a character is not a digit, return an invalid marker.
# 4. Handle the optional negative sign separately.
# 5. Return the converted integer.


def get_number(i: int, s: str) -> int:
    # Base case.
    if i < 0:
        return 0

    # Handle the optional negative sign.
    if i == 0 and s[i] == '-':
        return 0

    # Convert character to digit.
    digit = ord(s[i]) - ord('0')

    if digit < 0 or digit > 9:
        return -1

    previous = get_number(i - 1, s)

    if previous == -1:
        return -1

    return previous * 10 + digit


def atoi_recursive(s: str) -> int:
    if not s:
        return -1

    # Remove the sign before recursive conversion.
    if s[0] == '-':
        if len(s) == 1:
            return -1

        result = get_number(len(s) - 1, s)

        return -result if result != -1 else -1

    if s[0] == '+':
        if len(s) == 1:
            return -1

        return get_number(len(s) - 1, s)

    return get_number(len(s) - 1, s)


# CODE:
# print(atoi_recursive("123"))    # 123
# print(atoi_recursive("21a"))    # -1
# print(atoi_recursive("-456"))   # -456
# print(atoi_recursive("+789"))   # 789
# print(atoi_recursive("0"))     # 0
# print(atoi_recursive(""))      # -1
# print(atoi_recursive("-"))     # -1


# TIME COMPLEXITY = O(N)
# Each character is processed once.
#
# SPACE COMPLEXITY = O(N)
# Recursive call stack.
