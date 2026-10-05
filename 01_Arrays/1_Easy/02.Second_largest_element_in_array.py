"""
QUESTION:-
Given an array Arr of size N, find the second largest distinct element.

Example:
Input:  Arr = [12, 35, 1, 10, 34, 1]
Output: 34

Explanation:
The largest element is 35 and the second largest distinct element is 34.
"""

"""
APPROACH:-
-> Keep two variables: largest and second_largest.
-> When a new largest value is found, move the old largest to second_largest.
-> Otherwise, update second_largest when the current value is distinct and larger.
-> Return second_largest.

Using float("-inf") avoids the limitation of the original C++ version, which
does not handle arrays containing only negative values correctly.
"""

# CODE:-

def second_largest(arr: list[int]) -> int:
    """Return the second largest distinct element in arr."""
    if len(arr) < 2:
        raise ValueError("arr must contain at least two elements")

    largest = float("-inf")
    second = float("-inf")

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num

    if second == float("-inf"):
        raise ValueError("arr must contain at least two distinct elements")

    return int(second)


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
