# QUESTION:
# Sort a singly linked list in ascending order.
#
# APPROACH:
# Use merge sort because linked lists can be divided and merged
# efficiently without requiring array indexing.
#
# 1. Find the middle using slow and fast pointers.
# 2. Split the list into two halves.
# 3. Recursively sort both halves.
# 4. Merge the sorted halves.

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

def find_middle(head: Node) -> Node:
    slow = fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge(
    left: Node | None,
    right: Node | None
) -> Node | None:

    dummy = Node(0)
    tail = dummy

    while left and right:
        if left.data <= right.data:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next

        tail = tail.next

    tail.next = left if left else right

    return dummy.next

def sort_list(head: Node | None) -> Node | None:
    if head is None or head.next is None:
        return head

    middle = find_middle(head)

    right_head = middle.next
    middle.next = None

    left_sorted = sort_list(head)
    right_sorted = sort_list(right_head)

    return merge(left_sorted, right_sorted)

# CODE:
# head = Node(4)
# head.next = Node(2)
# head.next.next = Node(1)
# head.next.next.next = Node(3)
#
# head = sort_list(head)
#
# current = head
# while current:
#     print(current.data, end=" ")
#     current = current.next
# Output: 1 2 3 4

# TIME COMPLEXITY = O(N log N)
# SPACE COMPLEXITY = O(log N)
# Recursive merge-sort call stack.
