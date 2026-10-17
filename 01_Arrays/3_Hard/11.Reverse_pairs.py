# QUESTION:
# Count pairs (i, j) such that i < j and nums[i] > 2 * nums[j].
# Example: [1, 3, 2, 3, 1] -> 2

# APPROACH:
# Use merge sort. After recursively sorting both halves,
# count cross-half reverse pairs with a moving pointer,
# then merge the halves.

def reverse_pairs(nums: list[int]) -> int:
    def merge_sort(left: int, right: int) -> int:
        if left >= right:
            return 0

        mid = (left + right) // 2
        count = merge_sort(left, mid)
        count += merge_sort(mid + 1, right)

        j = mid + 1
        for i in range(left, mid + 1):
            while j <= right and nums[i] > 2 * nums[j]:
                j += 1
            count += j - (mid + 1)

        merged = []
        i, j = left, mid + 1

        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                merged.append(nums[i])
                i += 1
            else:
                merged.append(nums[j])
                j += 1

        merged.extend(nums[i:mid + 1])
        merged.extend(nums[j:right + 1])
        nums[left:right + 1] = merged

        return count

    return merge_sort(0, len(nums) - 1)


# CODE:
# print(reverse_pairs([1, 3, 2, 3, 1]))  # 2

# TIME COMPLEXITY = O(N log N)
# SPACE COMPLEXITY = O(N)
