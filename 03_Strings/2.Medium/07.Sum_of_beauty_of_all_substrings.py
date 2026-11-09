# QUESTION:
# The beauty of a substring is the difference between:
#   Maximum frequency of a character
#   Minimum non-zero frequency of a character
#
# Calculate the sum of beauty values of all substrings of s.
#
# APPROACH:
# 1. Fix the starting index of a substring.
# 2. Expand the substring one character at a time.
# 3. Maintain character frequencies using a dictionary.
# 4. Calculate the maximum and minimum non-zero frequencies.
# 5. Add their difference to the total beauty sum.


def beauty_sum(s: str) -> int:
    total_beauty = 0
    n = len(s)

    for i in range(n):
        frequency = {}

        for j in range(i, n):
            char = s[j]
            frequency[char] = frequency.get(char, 0) + 1

            maximum_frequency = max(frequency.values())
            minimum_frequency = min(frequency.values())

            total_beauty += (
                maximum_frequency - minimum_frequency
            )

    return total_beauty


# CODE:
# print(beauty_sum("aabcb"))     # 5
# print(beauty_sum("aabcbaa"))   # 17
# print(beauty_sum("a"))         # 0
# print(beauty_sum("abc"))       # 0
# print(beauty_sum("aaaa"))      # 0


# TIME COMPLEXITY = O(N^2 * K)
# N = length of string, K = number of distinct characters.
# For each substring extension, frequency values are scanned.
# For lowercase English letters, K is bounded by 26,
# making this effectively O(N^2).
#
# SPACE COMPLEXITY = O(K)
# Frequency dictionary stores distinct characters.
