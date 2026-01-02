from collections import defaultdict

# Simulate a distributed load balancing system with efficiency metrics
node_weights = [12, 8, 15, 7]
request_distribution = (0.3, 0.2, 0.4, 0.1)
overhead_factors = {i: 1.0 - 0.05 * i for i in range(4)}

# Irrelevant mapping - distractor
node_names = ['alpha', 'beta', 'gamma', 'delta']
name_mapping = {idx: name for idx, name in enumerate(node_names)}

# State tracker for monitoring (partially used)
health_status = defaultdict(bool)
for i in range(len(node_weights)):
    if node_weights[i] > 9:
        health_status[i] = True

# Compute effective node capacities (core logic start)
weighted_loads = []
efficiency_log = []
for i, weight in enumerate(node_weights):
    raw_load = weight * request_distribution[i]
    adjusted_load = raw_load * overhead_factors[i]
    weighted_loads.append(adjusted_load)
    
    # Distractor computation: logging unused metric
    peak_ratio = raw_load / max(request_distribution) if max(request_distribution) > 0 else 0
    efficiency_log.append(peak_ratio * 0.9)  # Not used later

# Aggregate total system load
system_load = sum(weighted_loads)

# Simulate cooling efficiency impact (semi-relevant)
temperature = 35
cooling_efficiency = 1.0 - (temperature - 20) * 0.01
if temperature > 30:
    cooling_efficiency *= 0.95  # Additional penalty

# Dummy environmental adjustment (irrelevant)
humidity_adjustment = (100 - 60) * 0.001  # Unused in final calc

# Core efficiency factor based on hardware limits
base_efficiency = 0.88
stability_bonus = 0.03 if all(health_status.values()) else 0.0

# Efficiency degrades under high load
load_pressure = system_load / 20.0
if load_pressure > 1.0:
    stability_bonus *= (1.0 / load_pressure)

efficiency_factor = base_efficiency + stability_bonus

# System capacity derived from nominal peak
nominal_peak = max(node_weights) * len(node_weights)
emergency_buffer = 0.1 * nominal_peak  # Red herring - not applied
system_capacity = sum(node_weights)  # Actual capacity

# Key statement
final_load = system_capacity * efficiency_factor

print(f"Result: {final_load}")