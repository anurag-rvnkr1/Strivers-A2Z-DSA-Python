# QUESTION:
# Allocate N books among M students in contiguous order.
# Every student must receive at least one book.
# Minimize the maximum number of pages assigned to any student.
# Return -1 if allocation is impossible.
# Example: pages = [12, 34, 67, 90], students = 2 -> 113

# APPROACH:
# Binary search the maximum pages allowed per student.
# Greedily allocate contiguous books and count students required.
# The allocation is valid when required students <= M.
# Since every student must receive at least one book,
# requiring <= M groups can be split into exactly M non-empty groups
# when M <= N.

def allocate_books(pages: list[int], students: int) -> int:
    if not pages or students <= 0 or students > len(pages):
        return -1

    def can_allocate(limit: int) -> bool:
        required_students = 1
        current_pages = 0

        for page_count in pages:
            if current_pages + page_count > limit:
                required_students += 1
                current_pages = page_count
            else:
                current_pages += page_count

            if required_students > students:
                return False

        return True

    left, right = max(pages), sum(pages)

    while left <= right:
        mid = (left + right) // 2

        if can_allocate(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left


# CODE:
# print(allocate_books([12, 34, 67, 90], 2))  # 113

# TIME COMPLEXITY = O(N * log S)
# SPACE COMPLEXITY = O(1)
# S = sum of all pages
