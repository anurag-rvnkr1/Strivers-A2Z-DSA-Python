# QUESTION:
# Merge two sorted arrays in-place without using extra array space.
# nums1 has length m + n, with its first m elements valid.
# Store the merged result in nums1.

# APPROACH:
# Start from the end of both arrays and fill nums1 backwards.
# This prevents overwriting elements that have not been processed.

def merge(
    nums1: list[int], m: int, nums2: list[int], n: int
) -> None:
    i = m - 1
    j = n - 1
    write = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[write] = nums1[i]
            i -= 1
        else:
            nums1[write] = nums2[j]
            j -= 1
        write -= 1

    while j >= 0:
        nums1[write] = nums2[j]
        j -= 1
        write -= 1


# CODE:
# a = [1, 2, 3, 0, 0, 0]
# merge(a, 3, [2, 5, 6], 3)
# print(a)  # [1, 2, 2, 3, 5, 6]

# TIME COMPLEXITY = O(M + N)
# SPACE COMPLEXITY = O(1)
