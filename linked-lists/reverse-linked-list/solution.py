class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


def create_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def linked_list_to_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


# Test Case 1 - Typical case
head = create_linked_list([1, 2, 3, 4, 5])
reversed_head = reverse_list(head)

print("Test Case 1:", linked_list_to_list(reversed_head))


# Test Case 2 - Edge case
head = create_linked_list([1])
reversed_head = reverse_list(head)

print("Test Case 2:", linked_list_to_list(reversed_head))