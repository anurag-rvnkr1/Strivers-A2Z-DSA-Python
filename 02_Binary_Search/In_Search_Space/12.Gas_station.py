# QUESTION:
# Add k gas stations between existing stations to minimize
# the maximum distance between adjacent stations.
# Return the minimized maximum distance.
# Example: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 9
# Output: 0.5

# APPROACH:
# Binary search the answer over a floating-point distance.
# For a candidate maximum distance d, calculate how many
# additional stations are required in every existing gap.
# Narrow the range until the required precision is reached.

def minimize_max_distance(
    stations: list[int], k: int, precision: float = 1e-6
) -> float:
    if len(stations) < 2 or k < 0:
        raise ValueError("At least two stations and non-negative k are required")

    stations = sorted(stations)
    gaps = [
        stations[i] - stations[i - 1]
        for i in range(1, len(stations))
    ]

    if any(gap <= 0 for gap in gaps):
        raise ValueError("Station positions must be distinct")

    def required_stations(distance: float) -> int:
        required = 0

        for gap in gaps:
            # Small tolerance avoids floating-point boundary overcounting.
            required += max(0, math.ceil(gap / distance - 1e-12) - 1)

            if required > k:
                return required

        return required

    left, right = 0.0, max(gaps)

    while right - left > precision:
        mid = (left + right) / 2

        if required_stations(mid) <= k:
            right = mid
        else:
            left = mid

    return right


# CODE:
# import math
# print(f"{minimize_max_distance([1,2,3,4,5,6,7,8,9,10], 9):.2f}")
# Output: 0.50

# TIME COMPLEXITY = O(N * log(D / precision))
# SPACE COMPLEXITY = O(N) for the gaps list
# D = maximum existing gap
