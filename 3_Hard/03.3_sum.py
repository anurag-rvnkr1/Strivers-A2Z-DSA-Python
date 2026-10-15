# QUESTION:
# Return all unique triplets whose sum is zero.
# Example: [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]

# APPROACH:
# Sort the array, fix one element, and use two pointers
# to locate the other two elements. Skip duplicates.

def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


# CODE:
# print(three_sum([-1, 0, 1, 2, -1, -4]))

# TIME COMPLEXITY = O(N^2)
# SPACE COMPLEXITY = O(1) auxiliary, excluding output
