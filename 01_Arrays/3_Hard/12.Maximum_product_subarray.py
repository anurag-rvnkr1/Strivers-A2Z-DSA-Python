# QUESTION:
# Find the contiguous subarray with the largest product
# and return that product.
# Example: [2, 3, -2, 4] -> 6

# APPROACH:
# Track the maximum and minimum products ending at each index.
# A negative number can turn the minimum product into the maximum,
# so swap the two values when the current number is negative.

def max_product(nums: list[int]) -> int:
    if not nums:
        raise ValueError("nums must not be empty")

    max_ending = min_ending = answer = nums[0]

    for num in nums[1:]:
        if num < 0:
            max_ending, min_ending = min_ending, max_ending

        max_ending = max(num, max_ending * num)
        min_ending = min(num, min_ending * num)
        answer = max(answer, max_ending)

    return answer


# CODE:
# print(max_product([2, 3, -2, 4]))  # 6
# print(max_product([-2, 0, -1]))    # 0

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
