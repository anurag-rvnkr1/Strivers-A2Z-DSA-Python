"""
QUESTION:-
Given an array and a target value, search for the target using linear search.
Return its index if found; otherwise return -1.

Example:
Input:  arr = [10, 20, 30, 40], target = 30
Output: 2
"""

"""
APPROACH:-
-> Traverse the array from left to right.
-> Compare each element with the target.
-> Return the index immediately when the target is found.
-> If the traversal ends without a match, return -1.

This is the fundamental linear-search pattern and works without requiring
the array to be sorted.
"""

# CODE:-

def linear_search(arr: list[int], target: int) -> int:
    """Return the first index of target in arr, or -1 if absent."""
    for i, num in enumerate(arr):
        if num == target:
            return i

    return -1


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
