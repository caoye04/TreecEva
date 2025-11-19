from collections import deque
import math

def biomass_redistribution(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # Apply logarithmic redistribution
        return math.log(result + 1) if result > 0 else 0
    return wrapper

@biomass_redistribution
def calculate_total_biomass(node_values):
    return sum(node_values)

# Initialize binary tree simulation
node_queue = deque([10.5])
insertions = [3.2, 7.8, 2.1, 9.6, 4.4]

# Process insertions with floating point arithmetic
while insertions:
    current = node_queue.popleft()
    new_val = insertions.pop(0)
    # Left child: 1.5x parent + new value
    left_child = current * 1.5 + new_val
    # Right child: parent squared / 2 minus new value
    right_child = (current ** 2) / 2 - new_val
    node_queue.append(left_child)
    node_queue.append(right_child)

# Convert deque to list for processing
final_nodes = list(node_queue)

# Apply biomass calculation with decorator
final_biomass = calculate_total_biomass(final_nodes)

print(f"Result: {final_biomass}")