"""
QUESTION:-

Given an array A of positive integers, find all the leaders in the array.

An element is a leader if it is greater than or equal to every element
to its right.

The rightmost element is always a leader.

Example:
Input:
A = [16, 17, 4, 3, 5, 2]

Output:
[17, 5, 2]

Explanation:
17 is greater than all elements to its right.
5 is greater than 2.
2 is the rightmost element and is always a leader.
"""

"""
APPROACH:-

-> Traverse the array from right to left.
-> Maintain the maximum element seen so far.
-> If the current element is greater than or equal to this maximum,
   it is a leader.
-> Add it to the result.
-> Update the maximum.
-> The leaders are found in reverse order, so reverse the result at the end.
"""

# CODE:-

def leaders(nums: list[int]) -> list[int]:
    if not nums:
        return []

    result = []
    maximum = nums[-1]

    result.append(maximum)

    for i in range(len(nums) - 2, -1, -1):
        if nums[i] >= maximum:
            result.append(nums[i])
            maximum = nums[i]

    result.reverse()

    return result


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(N) for the output
