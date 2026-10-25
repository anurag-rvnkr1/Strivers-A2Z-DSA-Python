# QUESTION:
# Count subarrays whose bitwise XOR equals k.
# Example: nums = [1, 2, 3, 2], k = 2 -> 3

# APPROACH:
# Use prefix XOR and a frequency dictionary.
# If prefix_xor ^ k was seen earlier, those occurrences
# identify subarrays whose XOR equals k.

def subarrays_with_xor_k(nums: list[int], k: int) -> int:
    prefix_xor = 0
    count = 0
    xor_frequency = {0: 1}

    for num in nums:
        prefix_xor ^= num
        count += xor_frequency.get(prefix_xor ^ k, 0)
        xor_frequency[prefix_xor] = xor_frequency.get(prefix_xor, 0) + 1

    return count


# CODE:
# print(subarrays_with_xor_k([1, 2, 3, 2], 2))  # 3

# TIME COMPLEXITY = O(N) average
# SPACE COMPLEXITY = O(N)
