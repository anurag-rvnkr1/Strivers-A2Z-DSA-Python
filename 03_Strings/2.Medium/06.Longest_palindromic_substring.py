# QUESTION:
# Given a string s, find the longest palindromic substring.
#
# A palindrome reads the same forward and backward.
#
# APPROACH:
# 1. Every palindrome has either one center (odd length)
#    or two centers (even length).
# 2. Expand outward from each possible center.
# 3. Whenever matching characters are found, update the
#    longest palindrome.
# 4. Return the longest palindromic substring.


def longest_palindrome(s: str) -> str:
    if not s:
        return ""

    start = 0
    max_length = 1

    def expand_from_center(left: int, right: int) -> None:
        nonlocal start, max_length

        while (
            left >= 0
            and right < len(s)
            and s[left] == s[right]
        ):
            current_length = right - left + 1

            if current_length > max_length:
                start = left
                max_length = current_length

            left -= 1
            right += 1

    for i in range(len(s)):
        # Odd-length palindrome.
        expand_from_center(i, i)

        # Even-length palindrome.
        expand_from_center(i, i + 1)

    return s[start:start + max_length]


# CODE:
# print(longest_palindrome("babad"))   # "bab" or "aba"
# print(longest_palindrome("cbbd"))    # "bb"
# print(longest_palindrome("a"))       # "a"
# print(longest_palindrome("racecar")) # "racecar"
# print(longest_palindrome("abc"))     # "a", "b", or "c"


# TIME COMPLEXITY = O(N^2)
# There are 2N possible centers and each expansion can take O(N).
#
# SPACE COMPLEXITY = O(1) auxiliary space
# The algorithm uses constant extra variables.
# The returned substring requires output space.
