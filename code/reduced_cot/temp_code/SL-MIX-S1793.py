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

from collections import defaultdict

# Initial package weights
package_weights = [15, 22, 8, 30, 12, 25, 18]

# Create linked list of package weights
head = create_linked_list(package_weights)

# Create frequency map
weight_freq = defaultdict(int)
for weight in package_weights:
    weight_freq[weight] += 1

# Process: Increase weights by 5 if frequency > 1, else decrease by 2
current = head
while current:
    if weight_freq[current.val] > 1:
        current.val += 5
    else:
        current.val -= 2
    current = current.next

# Convert back to list and sort descending
updated_weights = linked_list_to_list(head)
updated_weights.sort(reverse=True)

# Dynamic programming: calculate maximum cumulative weight up to each position
n = len(updated_weights)
cumulative_max = [0] * n
cumulative_max[0] = updated_weights[0]
for i in range(1, n):
    cumulative_max[i] = max(updated_weights[i], cumulative_max[i-1] + updated_weights[i])

# Calculate final cumulative weight
cumulative_weight = sum(cumulative_max)

print(f"Result: {cumulative_weight}")