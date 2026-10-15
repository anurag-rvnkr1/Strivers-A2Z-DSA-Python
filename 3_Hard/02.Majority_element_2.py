# QUESTION:
# Return all elements appearing more than floor(n / 3) times.
# Example: [3, 2, 3] -> [3]

# APPROACH:
# Use the extended Boyer-Moore Voting Algorithm.
# At most two elements can appear more than n / 3 times.
# Verify the candidates with a second pass.

def majority_element(nums: list[int]) -> list[int]:
    candidate1 = candidate2 = None
    count1 = count2 = 0

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1

    result = []
    threshold = len(nums) // 3

    for candidate in (candidate1, candidate2):
        if candidate is not None and nums.count(candidate) > threshold:
            if candidate not in result:
                result.append(candidate)

    return result


# CODE:
# print(majority_element([3, 2, 3]))  # [3]

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1), excluding output
