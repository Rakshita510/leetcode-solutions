class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1:
        current.next = list1
    else:
        current.next = list2

    return dummy.next


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
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

merged = merge_two_lists(list1, list2)

print("Test Case 1:", linked_list_to_list(merged))


# Test Case 2 - Edge case
list1 = create_linked_list([])
list2 = create_linked_list([0])

merged = merge_two_lists(list1, list2)

print("Test Case 2:", linked_list_to_list(merged))