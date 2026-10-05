"""
QUESTION:-
Given an array A[] of size n, find the largest element in the array.

Example:
Input:  A = [1, 8, 7, 56, 90]
Output: 90

Explanation:
The largest element is 90.
"""

"""
APPROACH:-
-> Initialize the answer with the first element.
-> Traverse the remaining elements.
-> Update the answer whenever a larger element is found.
-> Return the answer.

The same approach is used for the LeetCode-style problem where the function
receives an array and returns its maximum value.
"""

# CODE:-

def largest(arr: list[int]) -> int:
    """Return the largest element in arr."""
    if not arr:
        raise ValueError("arr must contain at least one element")

    ans = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > ans:
            ans = arr[i]

    return ans


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
