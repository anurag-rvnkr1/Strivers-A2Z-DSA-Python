"""
QUESTION:-

A permutation is an arrangement of the elements of an array.

Given an array nums, find its next lexicographically greater permutation.

If no greater permutation exists, rearrange the array into the lowest
possible order.

The modification must be performed in-place.

Example 1:
Input:
nums = [1, 2, 3]

Output:
[1, 3, 2]

Example 2:
Input:
nums = [3, 2, 1]

Output:
[1, 2, 3]
"""

"""
APPROACH:-

Step 1:
-> Find the first index from the right where:
      nums[i] < nums[i + 1]
-> This is the breakpoint.

Step 2:
-> If a breakpoint exists, find the first element from the right that is
   greater than nums[i].
-> Swap them.

Step 3:
-> Reverse everything after the breakpoint.

If no breakpoint exists, the array is completely descending.
Reversing the entire array produces the smallest permutation.

This is the optimal O(N) / O(1) solution for LeetCode 31.
"""

# CODE:-

def next_permutation(nums: list[int]) -> None:
    n = len(nums)

    if n <= 1:
        return

    # Step 1: Find breakpoint.
    breakpoint = -1

    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            breakpoint = i
            break

    # Step 2: Find the next greater element and swap.
    if breakpoint != -1:
        for i in range(n - 1, breakpoint, -1):
            if nums[i] > nums[breakpoint]:
                nums[i], nums[breakpoint] = (
                    nums[breakpoint],
                    nums[i]
                )
                break

    # Step 3: Reverse the suffix.
    left = breakpoint + 1
    right = n - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
