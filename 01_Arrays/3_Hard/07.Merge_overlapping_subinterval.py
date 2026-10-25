# QUESTION:
# Merge all overlapping intervals.
# Example: [[1, 3], [2, 6], [8, 10], [15, 18]]
# Output: [[1, 6], [8, 10], [15, 18]]

# APPROACH:
# Sort intervals by their start values.
# Merge an interval with the last result interval when they overlap.

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda interval: interval[0])
    merged = []

    for start, end in intervals:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return merged


# CODE:
# print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))

# TIME COMPLEXITY = O(N log N)
# SPACE COMPLEXITY = O(N), including the result
