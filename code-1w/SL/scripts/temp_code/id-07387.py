from collections import defaultdict, Counter

# Simulated network node diagnostics (irrelevant to final result)
def analyze_node_health(node_metrics):
    severity = 0
    for metric in node_metrics:
        if metric > 0.8:
            severity += 1
    return severity

# Decoy function: appears related but unused in critical path
def calculate_bandwidth_cost(route, usage):
    base = sum([len(route) * 0.5, usage * 0.3])
    return base * 1.2 if base > 10 else base * 0.8

# Misleading data transformation (dead end)
traffic_snapshot = [0.4, 0.6, 0.9, 0.2, 0.8]
weighted_load = [x * 1.5 for x in traffic_snapshot if x < 0.75]
peak_count = len([x for x in traffic_snapshot if x >= 0.7])

# Irrelevant counters and logs
debug_log = defaultdict(int)
debug_log['init'] = 1
for i in range(3):
    debug_log[f'step_{i}'] += i * 2

event_counter = Counter('network_latency'.split('_'))

# Core simulation parameters (some are decoys)
system_threshold = 0.7
scaling_factor = 1.8
dummy_offset = 0.15

# Actual demand and efficiency data
# Note: Only 'demand_profile' and 'efficiency_matrix' are used in final calculation
demand_profile = [120, 200, 150, 180, 90]
efficiency_matrix = [0.6, 0.9, 0.75, 0.8, 0.65]

# Red herring: complex-looking but unused formula
projected_growth = sum(demand_profile) * scaling_factor + dummy_offset * 100
adjusted_projection = projected_growth * (1 - system_threshold)

# Auxiliary diagnostic function (never called in execution path)
def validate_system_stability(resources):
    avg = sum(resources) / len(resources)
    return avg > 100 and max(resources) < 300

# Another distraction: partial computation with no downstream use
interim_result = 0
for i, val in enumerate(demand_profile[:3]):
    interim_result += val * efficiency_matrix[i] * 0.1

# Key algorithm: resource optimization using weighted average
# This is the actual logic that determines the answer
def optimize_allocation(demand, efficiency):
    total_weighted = sum(d * e for d, e in zip(demand, efficiency))
    total_efficiency = sum(efficiency)
    
    # Apply conditional adjustment based on profile characteristics
    if sum(demand) > 500:
        adjustment = 1.1
    else:
        adjustment = 0.95
    
    # Secondary check: if any high-efficiency component exists
    has_high_efficiency = any(e > 0.8 for e in efficiency)
    bonus = 1.05 if has_high_efficiency else 1.0
    
    # Final capacity calculation
    base_capacity = total_weighted / total_efficiency
    adjusted_capacity = base_capacity * adjustment * bonus
    
    # Additional logic: penalty if demand variance is high
    mean_demand = sum(demand) / len(demand)
    variance = sum((d - mean_demand) ** 2 for d in demand) / len(demand)
    if variance > 1500:
        adjusted_capacity *= 0.93
    
    return int(adjusted_capacity)

# Execution point of interest
resource_capacity = optimize_allocation(demand_profile, efficiency_matrix)

# Print final result as required
print(f"Target result: {resource_capacity}")