# QUESTION:
# Find the longest common prefix among an array of strings.
# Return an empty string if no common prefix exists.
# Example: ["flower", "flow", "flight"] -> "fl"

# APPROACH:
# Sort the strings lexicographically.
# Compare the first and last strings.
# Their common prefix is the common prefix of the entire array.

def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""

    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]

    i = 0

    while i < min(len(first), len(last)) and first[i] == last[i]:
        i += 1

    return first[:i]


# CODE:
# print(longest_common_prefix(["flower", "flow", "flight"]))  # "fl"
# print(longest_common_prefix(["dog", "racecar", "car"]))     # ""

# TIME COMPLEXITY = O(N log N * M)
# SPACE COMPLEXITY = O(N * M) for the sorted copy
# N = number of strings, M = maximum string length
