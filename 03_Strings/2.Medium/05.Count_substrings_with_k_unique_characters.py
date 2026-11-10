# QUESTION:
# Given a string s, count all possible substrings having
# exactly k distinct characters.
#
# APPROACH:
# 1. Count substrings containing at most k distinct characters.
# 2. Use a sliding window and a frequency dictionary.
# 3. Shrink the window whenever distinct characters exceed k.
# 4. The number of substrings with exactly k distinct characters is:
#
#    at_most_k(k) - at_most_k(k - 1)
#
# This avoids generating every substring separately.


def at_most_k_distinct(s: str, k: int) -> int:
    if k < 0:
        return 0

    frequency = {}
    left = 0
    count = 0

    for right in range(len(s)):
        char = s[right]
        frequency[char] = frequency.get(char, 0) + 1

        # Shrink window if distinct characters exceed k.
        while len(frequency) > k:
            left_char = s[left]
            frequency[left_char] -= 1

            if frequency[left_char] == 0:
                del frequency[left_char]

            left += 1

        # Every substring ending at right and starting
        # between left and right is valid.
        count += right - left + 1

    return count


def substr_count(s: str, k: int) -> int:
    if k <= 0:
        return 0

    return (
        at_most_k_distinct(s, k)
        - at_most_k_distinct(s, k - 1)
    )


# CODE:
# print(substr_count("aba", 2))       # 3
# print(substr_count("abaaca", 1))    # 7
# print(substr_count("abc", 3))       # 1
# print(substr_count("aaaa", 1))      # 10
# print(substr_count("abc", 4))       # 0


# TIME COMPLEXITY = O(N)
# Two sliding-window traversals, each taking O(N).
#
# SPACE COMPLEXITY = O(K)
# Frequency dictionary stores at most K + 1 distinct characters
# during window processing.
