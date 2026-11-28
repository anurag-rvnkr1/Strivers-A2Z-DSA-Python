# QUESTION:
# Given a 32-bit unsigned integer num and an integer i,
# perform the following operations:
#
# 1. Get the i-th bit.
# 2. Set the i-th bit.
# 3. Clear the i-th bit.
#
# Bit positions use 1-based indexing from the LSB.
#
# Example:
# Input: num = 70, i = 3
# Output: 1 70 66
#
# APPROACH:
# 1. Convert the 1-based position to a 0-based position.
# 2. Create a mask using 1 << position.
# 3. Get bit: num & mask.
# 4. Set bit: num | mask.
# 5. Clear bit: num & ~mask.

def bit_manipulation(num: int, i: int) -> tuple[int, int, int]:
    if num < 0 or i < 1 or i > 32:
        raise ValueError("Expected unsigned 32-bit num and bit position 1-32")

    position = i - 1
    mask = 1 << position

    # Get the i-th bit.
    get_bit = 1 if num & mask else 0

    # Set the i-th bit.
    set_bit = num | mask

    # Clear the i-th bit.
    clear_bit = num & ~mask

    return get_bit, set_bit, clear_bit

# CODE:
# print(bit_manipulation(70, 3))
# Output: (1, 70, 66)
#
# print(bit_manipulation(10, 2))
# Output: (1, 10, 8)
#
# print(bit_manipulation(8, 1))
# Output: (0, 9, 8)

# TIME COMPLEXITY = O(1)
# SPACE COMPLEXITY = O(1)
