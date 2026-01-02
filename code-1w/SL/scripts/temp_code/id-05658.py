from itertools import compress

# System node configurations
core_nodes = [True, False, True, True, False]
node_loads = [85, 42, 73, 91, 64]
capacity_per_node = [200, 150, 180, 220, 170]

# Filter active nodes with acceptable load
acceptable_load = [load < 80 for load in node_loads]
active_and_stable = list(compress(capacity_per_node, (a and b for a, b in zip(core_nodes, acceptable_load))))

# Dummy variable - irrelevant to main logic
dummy_offset = len(node_loads) * 2

# Main computation
capacities = [cap * 0.9 for cap in active_and_stable]
total_capacity = sum(capacities)

Result: total_capacity