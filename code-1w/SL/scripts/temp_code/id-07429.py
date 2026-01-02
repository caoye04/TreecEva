from itertools import groupby

# System node configuration and capacity data
current_nodes = ['A', 'B', 'C', 'D', 'E']
node_statuses = [True, True, False, True, True]  # Active status (irrelevant for final calc)
base_capacities = [120, 150, 95, 130, 110]

# Mapping node to capacity using dictionary operation
capacity_map = {node: base_capacities[i] for i, node in enumerate(current_nodes)}

# Update capacities based on operational rules
for node, active in zip(current_nodes, node_statuses):
    if not active:
        capacity_map[node] *= 0  # Inactive nodes have zero capacity

# Key computation step
total_capacity = sum(capacity_map.values())

# Print result for verification
print(f"Result: {total_capacity}")