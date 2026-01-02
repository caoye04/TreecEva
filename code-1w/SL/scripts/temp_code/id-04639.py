from itertools import compress

# System node configuration
core_nodes = [1, 0, 1, 1, 0, 1]
base_capacities = [120, 85, 95, 110, 75, 130]
efficiency_flags = [True, False, True, True, False, True]

# Filter active and efficient nodes
active_efficient_mask = [a and b for a, b in zip(core_nodes, efficiency_flags)]
filtered_capacities = list(compress(base_capacities, active_efficient_mask))

# Adjust loads based on operational constraints
adjusted_loads = [
    cap // 2 if cap > 100 else cap
    for cap in filtered_capacities
]

# Critical computation point
total_capacity = sum(adjusted_loads)

# Output result
print(f"Result: {total_capacity}")