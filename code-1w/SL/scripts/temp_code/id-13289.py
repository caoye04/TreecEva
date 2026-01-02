def analyze_system_health(loads, thresholds):
    max_load = max(loads)
    min_threshold = min(thresholds)
    overload_count = sum(1 for x in loads if x > min_threshold)
    return max_load - min_threshold if overload_count > 0 else 0

system_metrics = {
    'voltage': [110, 115, 120, 130],
    'current': [2.1, 2.3, 2.5, 2.6],
    'temp_zones': (45, 50, 55, 60),
    'fan_speeds': [2000, 2100, 2200, 2300]
}

threshold_limits = {
    'load_cap': 95,
    'thermal_max': 75,
    'voltage_range': (100, 135)
}

# Irrelevant transformation
transformed_data = {k: [x * 1.05 for x in v] if isinstance(v, list) else v 
                     for k, v in system_metrics.items()}

baseline_shift = sum(system_metrics['voltage']) / len(system_metrics['voltage'])
efficiency_ratio = 0.88

# Simulate subsystem weights based on nominal values
system_weights = []
for i in range(4):
    weight = 0
    if system_metrics['voltage'][i] > threshold_limits['voltage_range'][0]:
        weight += 0.4
    if system_metrics['current'][i] < 2.5:
        weight += 0.3
    if system_metrics['temp_zones'][i] < threshold_limits['thermal_max']:
        weight += 0.2
    if i % 2 == 0:
        weight += 0.1  # Artificial bias for even indices
    system_weights.append(round(weight, 2))

# Efficiency map with conditional expressions
efficiency_map = {i: 0.75 if system_weights[i] < 0.6 else (0.85 if system_weights[i] < 0.8 else 0.92) for i in range(4)}

# Distractor: unused function
def estimate_redundancy(nodes, mode='hot'):
    return len(nodes) // 2 if mode == 'hot' else len(nodes) // 3

# Auxiliary calculation not directly used
idle_consumption = sum([v[0] * 0.02 for v in system_metrics.values() if isinstance(v, list)])

# Core stability calculation
running_total = 0
stability_factors = []
for idx, wt in enumerate(system_weights):
    adjusted_eff = efficiency_map[idx] * (1 + wt * 0.1)
    factor = wt * adjusted_eff
    stability_factors.append(factor)
    running_total += factor

normalization_factor = sum(stability_factors)
normalized_scores = [sf / normalization_factor for sf in stability_factors]

# Final computation with distractor variables
buffer_reserve = 1.05
scaling_constant = 1.7
final_load = 0
for i in range(len(normalized_scores)):
    contribution = normalized_scores[i] * system_weights[i] * 100
    final_load += contribution

# Red herring: complex but unused expression
theoretical_capacity = (sum(system_weights) ** scaling_constant) * buffer_reserve if any(w > 0.7 for w in system_weights) else 0

# Answer printed at end
print(f"Result: {final_load}")