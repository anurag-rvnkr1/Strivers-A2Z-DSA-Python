# QUESTION:
# Count pairs (i, j) where i < j and nums[i] > nums[j].
# Example: [2, 4, 1, 3, 5] -> 3

# APPROACH:
# Use merge sort. During merging, when a right-side value
# is smaller than the current left-side value, it forms
# inversions with every remaining element in the left half.

def count_inversions(nums: list[int]) -> int:
    def merge_sort(left: int, right: int) -> int:
        if left >= right:
            return 0

        mid = (left + right) // 2
        inversions = merge_sort(left, mid)
        inversions += merge_sort(mid + 1, right)

        merged = []
        i, j = left, mid + 1

        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                merged.append(nums[i])
                i += 1
            else:
                merged.append(nums[j])
                inversions += mid - i + 1
                j += 1

        merged.extend(nums[i:mid + 1])
        merged.extend(nums[j:right + 1])
        nums[left:right + 1] = merged

        return inversions

    return merge_sort(0, len(nums) - 1)


# CODE:
# print(count_inversions([2, 4, 1, 3, 5]))  # 3

# TIME COMPLEXITY = O(N log N)
# SPACE COMPLEXITY = O(N)
