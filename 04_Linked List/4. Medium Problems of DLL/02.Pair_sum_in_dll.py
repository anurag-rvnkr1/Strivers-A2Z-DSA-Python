# QUESTION:
# Given a sorted doubly linked list and an integer target,
# find all pairs of nodes whose sum equals the target.
#
# Return the pairs as a list of [first, second].
#
# Example:
# Input:  1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8
# Target: 7
#
# Output: [[1, 6], [2, 5]]
#
# APPROACH:
# Use the two-pointer technique.
#
# 1. Initialize left at the head.
# 2. Find the tail and initialize right at the tail.
# 3. Calculate left.data + right.data.
# 4. If the sum equals target, record the pair.
# 5. If the sum is smaller, move left forward.
# 6. If the sum is larger, move right backward.
# 7. Stop when the pointers meet or cross.


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None


def find_pairs_with_given_sum(
    target: int,
    head: Node | None
) -> list[list[int]]:

    if head is None:
        return []

    left = head
    right = head

    # Find the tail.
    while right.next:
        right = right.next

    pairs = []

    while left is not right and left.prev is not right:
        current_sum = left.data + right.data

        if current_sum == target:
            pairs.append([left.data, right.data])

            left = left.next
            right = right.prev

        elif current_sum < target:
            left = left.next

        else:
            right = right.prev

    return pairs


# CODE:
# head = Node(1)
# values = [2, 4, 5, 6, 8]
# current = head
#
# for value in values:
#     new_node = Node(value)
#     current.next = new_node
#     new_node.prev = current
#     current = new_node
#
# print(find_pairs_with_given_sum(7, head))
# Output: [[1, 6], [2, 5]]
#
# print(find_pairs_with_given_sum(10, head))
# Output: [[2, 8], [4, 6]]
#
# print(find_pairs_with_given_sum(20, head))
# Output: []


# TIME COMPLEXITY = O(N)
# Finding the tail takes O(N).
# The two pointers together traverse at most O(N) nodes.
#
# SPACE COMPLEXITY = O(1) auxiliary space.
# The returned pairs require O(P) output space,
# where P is the number of matching pairs.
