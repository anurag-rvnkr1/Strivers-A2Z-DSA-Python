# QUESTION:
# Determine whether a singly linked list is a palindrome.
#
# APPROACH:
# 1. Find the middle using slow and fast pointers.
# 2. Reverse the second half of the linked list.
# 3. Compare the first and second halves.
# 4. Restore the original list before returning.
#
# This implementation preserves the input list structure.


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


def is_palindrome(head: Node | None) -> bool:
    if head is None or head.next is None:
        return True

    slow = fast = head

    # Find the end of the first half.
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half.
    second_half = reverse_list(slow.next)
    slow.next = second_half

    first = head
    second = second_half
    result = True

    while second:
        if first.data != second.data:
            result = False
            break

        first = first.next
        second = second.next

    # Restore the original linked list.
    slow.next = reverse_list(second_half)

    return result


# CODE:
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(2)
# head.next.next.next = Node(1)
#
# print(is_palindrome(head))  # True
#
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
#
# print(is_palindrome(head))  # False


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
