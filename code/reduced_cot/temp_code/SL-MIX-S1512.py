from collections import deque

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

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Package weights in grams
package_weights = [150, 300, 120, 200, 180, 90, 250, 160]
drone_capacity = 500  # Maximum weight capacity in grams

# Create linked list of packages
packages_head = create_linked_list(package_weights)

# Convert linked list to list for processing
weights_list = linked_list_to_list(packages_head)

# Greedy algorithm: Sort packages by weight (ascending) to maximize count
sorted_weights = sorted(weights_list)

# Select packages using greedy approach
current_weight = 0
delivered_count = 0
for weight in sorted_weights:
    if current_weight + weight <= drone_capacity:
        current_weight += weight
        delivered_count += 1
    else:
        break

print(f"Result: {delivered_count}")