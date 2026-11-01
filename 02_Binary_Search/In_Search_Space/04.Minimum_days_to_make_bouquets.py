# QUESTION:
# Each bouquet needs k adjacent flowers.
# Given bloomDay and the required number of bouquets m,
# return the minimum number of days needed.
# Return -1 if it is impossible.
# Example: bloomDay = [1, 10, 3, 10, 2], m = 3, k = 1 -> 3

# APPROACH:
# Binary search the number of days between minimum and maximum
# bloom days. For each candidate day, count bouquets formed
# from consecutive flowers that have bloomed.

def min_days(bloom_day: list[int], m: int, k: int) -> int:
    n = len(bloom_day)

    if m <= 0 or k <= 0:
        return 0
    if m * k > n:
        return -1

    def can_make(day: int) -> bool:
        bouquets = 0
        consecutive = 0

        for bloom in bloom_day:
            if bloom <= day:
                consecutive += 1

                if consecutive == k:
                    bouquets += 1
                    consecutive = 0
            else:
                consecutive = 0

            if bouquets >= m:
                return True

        return False

    left, right = min(bloom_day), max(bloom_day)

    while left <= right:
        mid = (left + right) // 2

        if can_make(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left


# CODE:
# print(min_days([1, 10, 3, 10, 2], 3, 1))  # 3

# TIME COMPLEXITY = O(N * log D)
# SPACE COMPLEXITY = O(1)
# D = maximum bloom day - minimum bloom day + 1
