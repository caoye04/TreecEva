from collections import Counter, deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

durations = [3, 7, 2, 7, 7, 1, 3, 7, 2]
head = create_linked_list(durations)

duration_counter = Counter()
current_node = head
while current_node:
    duration_counter[current_node.val] += 1
    current_node = current_node.next

total_weekly_checkouts = duration_counter[7]
print(f"Result: {total_weekly_checkouts}")