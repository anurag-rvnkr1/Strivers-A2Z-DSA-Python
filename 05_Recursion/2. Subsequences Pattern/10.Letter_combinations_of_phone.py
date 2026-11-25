# QUESTION:
# Given a string containing digits from 2 to 9,
# return all possible letter combinations represented
# by those digits on a telephone keypad.
#
# Example:
# Input: "23"
# Output:
# ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
#
# APPROACH:
# 1. Create a mapping from digits to corresponding letters.
# 2. Process each digit recursively.
# 3. Try every letter mapped to the current digit.
# 4. Backtrack after each recursive call.
# 5. Store a combination after processing all digits.


def letter_combinations(digits: str) -> list[str]:
    if not digits:
        return []

    mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    if any(digit not in mapping for digit in digits):
        raise ValueError("Digits must be between 2 and 9")

    result = []
    current = []

    def solve(index: int) -> None:
        if index == len(digits):
            result.append("".join(current))
            return

        for char in mapping[digits[index]]:
            current.append(char)
            solve(index + 1)
            current.pop()

    solve(0)

    return result


# CODE:
# print(letter_combinations("23"))
# Output:
# ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
#
# print(letter_combinations("2"))  # ["a", "b", "c"]
# print(letter_combinations(""))   # []


# TIME COMPLEXITY = O(3^N * 4^M * L)
# N = digits mapping to 3 letters.
# M = digits mapping to 4 letters.
# L = total number of digits; each output combination has length L.
#
# SPACE COMPLEXITY = O(L) auxiliary recursion/current combination.
# Output storage is O(3^N * 4^M * L).
