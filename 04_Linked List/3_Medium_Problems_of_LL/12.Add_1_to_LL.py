# QUESTION:
# A number is represented by a linked list where each node
# contains one digit. Add 1 to the represented number.
#
# Example:
# Input: 1 -> 2 -> 9
# Output: 1 -> 3 -> 0
#
# APPROACH:
# 1. Reverse the linked list.
# 2. Add 1 starting from the least significant digit.
# 3. Propagate carry while required.
# 4. If carry remains, create a new node.
# 5. Reverse the list again.


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


def reverse_list(head: Node | None) -> Node | None:
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


def add_one(head: Node | None) -> Node | None:
    if head is None:
        return Node(1)

    head = reverse_list(head)

    current = head
    carry = 1
    previous = None

    while current and carry:
        total = current.data + carry

        current.data = total % 10
        carry = total // 10

        previous = current
        current = current.next

    if carry:
        previous.next = Node(carry)

    return reverse_list(head)


# CODE:
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(9)
#
# head = add_one(head)
#
# current = head
# while current:
#     print(current.data, end=" ")
#     current = current.next
# Output: 1 3 0
#
# head = Node(9)
# head.next = Node(9)
# head.next.next = Node(9)
#
# head = add_one(head)
# Output: 1 0 0 0


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
# The list is reversed in place.
