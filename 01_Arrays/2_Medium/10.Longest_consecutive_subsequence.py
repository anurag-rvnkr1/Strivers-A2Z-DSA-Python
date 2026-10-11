"""
QUESTION:-

Given an unsorted array of integers nums, return the length of the
longest consecutive elements sequence.

Example 1:
Input:
nums = [100, 4, 200, 1, 3, 2]

Output:
4

Explanation:
The longest consecutive sequence is:
[1, 2, 3, 4]

Example 2:
Input:
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

Output:
9
"""

"""
APPROACH:-

-> Store all numbers in a set.
-> A number is the beginning of a sequence only when:
      num - 1
   does not exist in the set.
-> Starting from such a number, keep checking:
      num + 1
      num + 2
      ...
-> Track the longest sequence.

Using a set allows average O(1) lookup.

This is the optimal approach for LeetCode 128.
"""

# CODE:-

def longest_consecutive(nums: list[int]) -> int:
    numbers = set(nums)
    longest = 0

    for num in numbers:
        # Start only when num begins a sequence.
        if num - 1 not in numbers:
            current = num
            length = 1

            while current + 1 in numbers:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


# TIME COMPLEXITY = O(N) average
# SPACE COMPLEXITY = O(N)
