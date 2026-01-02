from collections import defaultdict

# System configuration parameters
total_nodes = 8
redundancy_factor = 3
base_throughput = 150

# Simulated node health scores (irrelevant distractor)
node_health = [0.95, 0.87, 1.0, 0.76, 0.91, 0.88, 0.99, 0.82]

# Workload distribution per unit
workload_distribution = [2, 4, 1, 3, 5, 2, 4, 3]

# Map units to processing tiers
unit_to_tier = defaultdict(int)
for i, load in enumerate(workload_distribution):
    if load > 3:
        unit_to_tier[i] = 2
    elif load > 1:
        unit_to_tier[i] = 1
    else:
        unit_to_tier[i] = 0

# Calculate effective capacity per unit based on tier
capacities = []
for i in range(len(workload_distribution)):
    base = base_throughput
    tier = unit_to_tier[i]
    adjusted = base * (1.1 if tier == 1 else (1.25 if tier == 2 else 1.0))
    capacities.append(adjusted)

# Aggregate total system capacity
system_total = sum(capacities)

# Apply redundancy scaling (only active when redundancy_factor > 2)
system_total *= redundancy_factor if redundancy_factor > 2 else 1.0

# Final efficiency correction based on node count
efficiency_ratio = 0.9 + (total_nodes * 0.01)  # scales with node count
final_capacity = int(system_total * efficiency_ratio)

Result: final_capacity