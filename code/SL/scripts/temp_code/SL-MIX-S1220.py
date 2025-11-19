class ListNode:
    def __init__(self, weight, priority):
        self.weight = weight
        self.priority = priority
        self.next = None

def build_linked_list(data):
    if not data:
        return None
    head = ListNode(data[0][0], data[0][1])
    current = head
    for weight, priority in data[1:]:
        current.next = ListNode(weight, priority)
        current = current.next
    return head

def calculate_ratio(node):
    return node.weight / node.priority if node.priority != 0 else float('inf')

# Package data: (weight in kg, priority level)
packages_data = [
    (300, 3), (250, 5), (400, 4), (150, 2), 
    (350, 7), (200, 4), (180, 3), (220, 6)
]

package_list = build_linked_list(packages_data)
nodes = []
current = package_list
while current:
    nodes.append(current)
    current = current.next

# Sort nodes by weight-to-priority ratio in descending order
nodes.sort(key=lambda x: calculate_ratio(x), reverse=True)

truck_capacity = 1000
trucks_used = 0
loaded_weight = 0
remaining_capacity = 0

for node in nodes:
    if loaded_weight + node.weight <= truck_capacity:
        loaded_weight += node.weight
    else:
        remaining_capacity += (truck_capacity - loaded_weight)
        trucks_used += 1
        loaded_weight = node.weight

if loaded_weight > 0:
    remaining_capacity += (truck_capacity - loaded_weight)
    trucks_used += 1

unused_capacity = trucks_used * truck_capacity - sum(node.weight for node in nodes) + remaining_capacity
print(f"Result: {unused_capacity}")