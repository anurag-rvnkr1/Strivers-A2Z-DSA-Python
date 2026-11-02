# QUESTION:
# Place m cows in given stall positions such that the minimum
# distance between any two cows is maximized.
# Example: positions = [1, 2, 3, 4, 7], m = 3 -> 3

# APPROACH:
# Sort stall positions.
# Binary search the minimum distance.
# Greedily place each next cow in the earliest available stall
# at least that distance away from the previous cow.

def aggressive_cows(stalls: list[int], cows: int) -> int:
    if not stalls or cows <= 0 or cows > len(stalls):
        return -1

    if cows == 1:
        return 0

    stalls = sorted(stalls)

    def can_place(distance: int) -> bool:
        placed = 1
        last_position = stalls[0]

        for position in stalls[1:]:
            if position - last_position >= distance:
                placed += 1
                last_position = position

                if placed >= cows:
                    return True

        return False

    left, right = 1, stalls[-1] - stalls[0]
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        if can_place(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer


# CODE:
# print(aggressive_cows([1, 2, 3, 4, 7], 3))  # 3

# TIME COMPLEXITY = O(N log N + N log D)
# SPACE COMPLEXITY = O(N) for the sorted copy
# D = maximum possible distance between stalls
