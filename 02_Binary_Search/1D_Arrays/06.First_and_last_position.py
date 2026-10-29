# QUESTION:
# Find the first and last positions of target in a sorted array.
# Return [-1, -1] if target is absent.

# APPROACH:
# Use binary search to find the first occurrence and the last
# occurrence independently.

def search_range(nums: list[int], target: int) -> list[int]:
    def find_first() -> int:
        left, right = 0, len(nums) - 1
        answer = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                if nums[mid] == target:
                    answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer

    def find_last() -> int:
        left, right = 0, len(nums) - 1
        answer = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] <= target:
                if nums[mid] == target:
                    answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer

    return [find_first(), find_last()]


# CODE:
# print(search_range([5, 7, 7, 8, 8, 10], 8))  # [3, 4]

# TIME COMPLEXITY = O(log N)
# SPACE COMPLEXITY = O(1), excluding output
