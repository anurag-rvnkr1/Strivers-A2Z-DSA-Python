# QUESTION:
# Given a valid parentheses string s, return its maximum nesting depth.
#
# APPROACH:
# 1. Maintain a counter for currently opened parentheses.
# 2. Increment it whenever '(' is encountered.
# 3. Update the maximum depth after every opening parenthesis.
# 4. Decrement it whenever ')' is encountered.


def max_depth(s: str) -> int:
    opened = 0
    maximum_depth = 0

    for char in s:
        if char == '(':
            opened += 1
            maximum_depth = max(maximum_depth, opened)

        elif char == ')':
            opened -= 1

    return maximum_depth


# CODE:
# print(max_depth("(1+(2*3)+((8)/4))+1"))  # 3
# print(max_depth("(1)+((2))+(((3)))"))    # 3
# print(max_depth("1+(2*3)/(2-1)"))        # 1
# print(max_depth("1"))                   # 0


# TIME COMPLEXITY = O(N)
# Each character is visited exactly once.
#
# SPACE COMPLEXITY = O(1)
# Only two variables are used.
