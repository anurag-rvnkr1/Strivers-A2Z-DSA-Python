# QUESTION:
# Given a Roman numeral string s, convert it into an integer.
#
# APPROACH:
# 1. Store the integer value of each Roman symbol.
# 2. Traverse the string from left to right.
# 3. If the current symbol has a greater value than the next
#    symbol, subtract the current value.
# 4. Otherwise, add the current value.
# 5. Return the calculated integer.


def roman_to_int(s: str) -> int:
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0

    for i in range(len(s)):
        if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
            result -= values[s[i]]
        else:
            result += values[s[i]]

    return result


# CODE:
# print(roman_to_int("III"))       # 3
# print(roman_to_int("LVIII"))     # 58
# print(roman_to_int("MCMXCIV"))   # 1994
# print(roman_to_int("IX"))        # 9


# TIME COMPLEXITY = O(N)
# Every character is visited once.
#
# SPACE COMPLEXITY = O(1)
# The Roman symbol mapping has a fixed size of seven.
