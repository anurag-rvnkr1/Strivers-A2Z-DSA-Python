# QUESTION:
# Given a string s, sort it in decreasing order based on the
# frequency of its characters.
#
# APPROACH:
# 1. Count the frequency of every character using Counter.
# 2. Sort characters by their frequency in descending order.
# 3. Repeat each character according to its frequency.


from collections import Counter


def frequency_sort(s: str) -> str:
    frequency = Counter(s)

    sorted_chars = sorted(
        frequency.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return "".join(
        char * count for char, count in sorted_chars
    )


# CODE:
# print(frequency_sort("tree"))       # "eert" or "eetr"
# print(frequency_sort("cccaaa"))     # "cccaaa" or "aaaccc"
# print(frequency_sort("Aabb"))       # "bbAa" or "bbaA"


# TIME COMPLEXITY = O(N + K log K)
# N = length of string, K = number of distinct characters.
#
# SPACE COMPLEXITY = O(K + N)
# Frequency map and sorted result/output string.
