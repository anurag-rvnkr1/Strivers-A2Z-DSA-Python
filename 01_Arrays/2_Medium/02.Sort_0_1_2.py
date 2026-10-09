"""
QUESTION:-

Given an array nums containing n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent.

Use:
0 -> Red
1 -> White
2 -> Blue

The final order must be:
0, 0, ..., 1, 1, ..., 2, 2, ...

Example 1:
Input: nums = [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]

Example 2:
Input: nums = [2, 0, 1]
Output: [0, 1, 2]
"""

"""
APPROACH:-

Use the Dutch National Flag algorithm.

-> low  = position where the next 0 should go.
-> mid  = current element being processed.
-> high = position where the next 2 should go.

If nums[mid] == 0:
-> Swap nums[low] and nums[mid].
-> Increment low and mid.

If nums[mid] == 1:
-> Simply increment mid.

If nums[mid] == 2:
-> Swap nums[mid] and nums[high].
-> Decrement high.
-> Do NOT increment mid because the swapped value still needs processing.

This is the optimal in-place solution for LeetCode 75.
"""

# CODE:-

def sort_colors(nums: list[int]) -> None:
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1

        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
