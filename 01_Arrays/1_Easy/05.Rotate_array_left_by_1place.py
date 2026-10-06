"""
QUESTION:-
Given an array ARR containing N elements, rotate the array left by one place.
The first element moves to the last position.

Example:
Input:  ARR = [1, 2, 3, 4, 5]
Output: [2, 3, 4, 5, 1]
"""

"""
APPROACH:-
-> Store the first element temporarily.
-> Shift every remaining element one position to the left.
-> Put the stored first element at the last position.
-> Return the modified array.

This is an in-place rotation.
"""

# CODE:-

def rotate_left_by_one(arr: list[int]) -> list[int]:
    """Rotate arr one position to the left in-place."""
    if len(arr) <= 1:
        return arr

    first = arr[0]

    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]

    arr[-1] = first

    return arr


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
