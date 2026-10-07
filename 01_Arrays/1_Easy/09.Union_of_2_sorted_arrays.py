"""
QUESTION:-
Given two sorted arrays, find their union containing every distinct element
from both arrays.

Example:
Input:
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3]

Output:
[1, 2, 3, 4, 5]

Another example:
arr1 = [2, 2, 3, 4, 5]
arr2 = [1, 1, 2, 3, 4]

Output:
[1, 2, 3, 4, 5]
"""

"""
APPROACH:-
-> Use two pointers, one for each sorted array.
-> Add the smaller value to the result.
-> When both values are equal, add it only once and advance both pointers.
-> Skip duplicates while advancing either pointer.
-> Append the remaining distinct values from the unfinished array.

Because both inputs are sorted, every element is processed only once.
"""

# CODE:-

def find_union(arr1: list[int], arr2: list[int]) -> list[int]:
    """Return the sorted union of two sorted arrays without duplicates."""
    i = 0
    j = 0
    ans: list[int] = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            value = arr1[i]
            i += 1
        elif arr2[j] < arr1[i]:
            value = arr2[j]
            j += 1
        else:
            value = arr1[i]
            i += 1
            j += 1

        if not ans or ans[-1] != value:
            ans.append(value)

    while i < len(arr1):
        value = arr1[i]
        i += 1

        if not ans or ans[-1] != value:
            ans.append(value)

    while j < len(arr2):
        value = arr2[j]
        j += 1

        if not ans or ans[-1] != value:
            ans.append(value)

    return ans


# TIME COMPLEXITY = O(N + M)
# SPACE COMPLEXITY = O(N + M) for the output
