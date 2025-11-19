class ShipmentNode:
    def __init__(self, priority):
        self.priority = priority
        self.next = None

class WarehouseSystem:
    def __init__(self):
        self.head = None
    
    def add_shipment(self, priority):
        new_node = ShipmentNode(priority)
        new_node.next = self.head
        self.head = new_node
    
    def get_total_priority(self):
        total = 0
        current = self.head
        while current:
            total += current.priority
            current = current.next
        return total

import collections
import itertools

# Initialize data structures
incoming_stack = []
outgoing_queue = collections.deque()
warehouse = WarehouseSystem()

# Process shipment data
shipments_data = [15, 23, 8, 42, 35, 19, 27]
priority_modifiers = {i: v for i, v in enumerate([2, -1, 3, -2, 1, 4, -3])}
modified_priorities = {k: shipments_data[k] + v for k, v in priority_modifiers.items()}

# Push modified priorities to stack
for priority in modified_priorities.values():
    incoming_stack.append(priority)

# Transfer from stack to queue with conditional logic
while incoming_stack:
    item = incoming_stack.pop()
    # Apply ternary operation for special handling
    processed_item = item * 2 if item > 30 else (item // 2 if item < 10 else item)
    outgoing_queue.append(processed_item)

# Process outgoing shipments with early termination condition
shipment_count = 0
while outgoing_queue and shipment_count < 5:
    shipment = outgoing_queue.popleft()
    # Break condition based on comparison operation
    if shipment == 19:
        break
    warehouse.add_shipment(shipment)
    shipment_count += 1

# Calculate balance with nested loop for adjustment factors
adjustment_factors = [[1, 2], [3, 4], [5, 6]]
total_adjustments = 0
for i, sublist in enumerate(adjustment_factors):
    for j, factor in enumerate(sublist):
        total_adjustments += factor * (i + 1) * (j + 1)

# Final balance calculation
base_priority = warehouse.get_total_priority()
final_balance = base_priority + total_adjustments if base_priority > 50 else base_priority - total_adjustments
print(f"Result: {final_balance}")