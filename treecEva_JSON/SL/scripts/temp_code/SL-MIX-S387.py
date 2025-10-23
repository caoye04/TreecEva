class TorqueNode:
    def __init__(self, adjustment, next_node=None):
        self.adjustment = adjustment
        self.next = next_node

def build_torque_chain(values):
    if not values:
        return None
    head = TorqueNode(values[0])
    current = head
    for val in values[1:]:
        current.next = TorqueNode(val)
        current = current.next
    return head

def compute_final_output(chain_head):
    from itertools import combinations
    
    adjustments = []
    current = chain_head
    while current:
        adjustments.append(current.adjustment)
        current = current.next
    
    # Short-circuit evaluation with cumulative condition
    valid_combinations = [
        combo for combo in combinations(adjustments, 3)
        if (combo[0] > 0 and combo[1] < 100) or 
           (combo[1] > 0 and combo[2] < 100)
    ]
    
    # Calculate weighted sum
    total = sum(
        (a * b) + c 
        for a, b, c in valid_combinations
        if a + b + c != 0  # Additional short-circuit condition
    )
    
    return total % 1000

# Initialize torque adjustments
initial_adjustments = [10, -5, 25, 0, 40, -15, 30]
torque_chain = build_torque_chain(initial_adjustments)

# Compute final output
final_torque_output = compute_final_output(torque_chain)
print(f"Result: {final_torque_output}")