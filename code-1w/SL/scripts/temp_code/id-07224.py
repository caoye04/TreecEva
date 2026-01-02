from itertools import compress

# System resource parameters
core_nodes = [4, 8, 6, 7, 5]
standby_nodes = [2, 3, 4, 1, 2]
utilization_rate = [0.85, 0.92, 0.88, 0.90, 0.87]

# Calculate effective capacity per node group
effective_capacity = [core * rate + standby for core, standby, rate in zip(core_nodes, standby_nodes, utilization_rate)]

# Threshold for optimization: only consider groups with capacity above average
avg_capacity = sum(effective_capacity) / len(effective_capacity)
mask = [cap >= avg_capacity for cap in effective_capacity]

# Apply optimization filter
optimized_allocations = list(compress(effective_capacity, mask))

# Final aggregation step
total_capacity = sum(optimized_allocations)

# Irrelevant logging variables (minimal distraction)
current_timestamp = 1712345678
debug_mode = False

Result: total_capacity