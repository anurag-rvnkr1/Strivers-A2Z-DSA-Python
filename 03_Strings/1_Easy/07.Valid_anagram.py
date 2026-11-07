# QUESTION:
# Given two strings s and t, determine whether t is an anagram of s.
# An anagram contains exactly the same characters with the same frequencies.
# Example: s = "anagram", t = "nagaram" -> True
# Example: s = "rat", t = "car" -> False

# APPROACH:
# Count the frequency of every character in s.
# Decrease the frequency for every character in t.
# If the lengths or character frequencies differ, return False.

from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    return Counter(s) == Counter(t)


# CODE:
# print(is_anagram("anagram", "nagaram"))  # True
# print(is_anagram("rat", "car"))          # False

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(K)
# K = number of distinct characters
