from collections import deque

class WarehouseNode:
    def __init__(self, energy_cost, left=None, right=None):
        self.energy_cost = energy_cost
        self.left = left
        self.right = right

def simulate_robot_navigation(root_node):
    if not root_node:
        return 0
    
    # Stack for DFS traversal
    node_stack = [(root_node, 0)]  # (node, accumulated_cost)
    max_threshold = 100
    energy_readings = []
    
    while node_stack:
        current_node, path_cost = node_stack.pop()
        new_cost = path_cost + current_node.energy_cost
        
        # Early return condition
        if new_cost > max_threshold:
            energy_readings.append(new_cost)
            continue
            
        # Leaf node check
        if not current_node.left and not current_node.right:
            energy_readings.append(new_cost)
        else:
            # Push children to stack
            if current_node.right:
                node_stack.append((current_node.right, new_cost))
            if current_node.left:
                node_stack.append((current_node.left, new_cost))
    
    # Calculate final balance using list comprehension and lambda
    valid_readings = [x for x in energy_readings if x <= max_threshold]
    adjustment_factor = (lambda vals: sum(vals) % 7 if vals else 0)(valid_readings)
    
    # Final calculation with set operations
    unique_costs = frozenset(energy_readings)
    final_energy_balance = len(unique_costs) * 3 - adjustment_factor
    
    return final_energy_balance

# Build warehouse tree
root = WarehouseNode(10)
root.left = WarehouseNode(20)
root.right = WarehouseNode(15)
root.left.left = WarehouseNode(25)
root.left.right = WarehouseNode(30)
root.right.left = WarehouseNode(35)
root.right.right = WarehouseNode(5)
root.left.left.left = WarehouseNode(40)  # This path exceeds threshold
root.left.left.right = WarehouseNode(45) # This path exceeds threshold

final_energy_balance = simulate_robot_navigation(root)
print(f"Result: {final_energy_balance}")