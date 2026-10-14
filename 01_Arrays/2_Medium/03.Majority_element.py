"""
QUESTION:-

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than floor(n / 2)
times.

You may assume that the majority element always exists.

Example 1:
Input: nums = [3, 2, 3]
Output: 3

Example 2:
Input: nums = [2, 2, 1, 1, 1, 2, 2]
Output: 2
"""

"""
APPROACH:-

Use the Boyer-Moore Voting Algorithm.

-> Maintain a candidate and a vote count.
-> If the current element equals the candidate, increase the count.
-> Otherwise, decrease the count.
-> When the count becomes zero, choose the current element as the new candidate.
-> Because the majority element occurs more than n/2 times, it will remain
   as the final candidate.

This gives an optimal O(N) time and O(1) space solution.
"""

# CODE:-

def majority_element(nums: list[int]) -> int:
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
