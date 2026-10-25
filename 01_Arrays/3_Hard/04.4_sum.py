# QUESTION:
# Return all unique quadruplets whose sum equals target.
# Example: [1, 0, -1, 0, -2, 2], target = 0
# Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

# APPROACH:
# Sort the array, fix two elements, and use two pointers
# for the remaining pair. Skip duplicates at every level.

def four_sum(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left, right = j + 1, n - 1

            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < target:
                    left += 1
                else:
                    right -= 1

    return result


# CODE:
# print(four_sum([1, 0, -1, 0, -2, 2], 0))

# TIME COMPLEXITY = O(N^3)
# SPACE COMPLEXITY = O(1) auxiliary, excluding output
