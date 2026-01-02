def analyze_component(reading, threshold=75):
    """Irrelevant helper function for sensor analysis."""
    if reading < threshold:
        return (reading * 1.2) + 3
    else:
        return (reading * 0.8) - 5

# Irrelevant sensor data processing
temperature_readings = [68, 72, 77, 81, 65]
adjusted_temps = []
for val in temperature_readings:
    adjusted_temps.append(analyze_component(val))

# Decoy system status variables
current_state = {'status': 'active', 'mode': 'diagnostic'}
system_flags = {k: False for k in ['overheat', 'pressure_drop', 'flow_stall']}

# Core benchmark metric computation
base_metrics = [85, 92, 78, 96, 88]
weight_vector = [0.2, 0.3, 0.15, 0.25, 0.1]

# Misleading normalization path (dead-end)
normalized_metrics = []
for m in base_metrics:
    if m > 90:
        normalized_metrics.append(m * 0.95)
    elif m < 80:
        normalized_metrics.append(m * 1.05)
    else:
        normalized_metrics.append(m)

# Real logic begins: set-based filtering
valid_ranges = set(range(80, 101))
metric_set = set(base_metrics)
qualified_metrics = metric_set & valid_ranges  # Intersection: only >=80

# Auxiliary transformation (partially relevant)
def apply_bonus(score):
    """Adds conditional bonus based on bit properties."""
    if score & 1:  # odd?
        return score + 4
    elif score % 4 == 0:
        return score + 2
    return score

# Apply bonus only to qualified metrics
enhanced_scores = [apply_bonus(s) for s in qualified_metrics]

# Benchmark data with distractor fields
benchmark_data = {
    'version': '3.1.4',
    'scoring_method': 'weighted_sum',
    'baseline': 85,
    'tolerance': 0.05,
    'aux_data': [analyze_component(x) for x in [70, 75, 80]]  # Red herring
}

# Real evaluation logic
metric_weights = {
    85: 0.2,
    92: 0.3,
    88: 0.25,
    96: 0.25  # Note: 78 was excluded due to set filtering
}

# Recursive contribution accumulator (unnecessarily complex)
def accumulate_contributions(metrics, weights, idx=0):
    if idx >= len(metrics):
        return 0.0
    current_metric = metrics[idx]
    contribution = weights[current_metric] * current_metric
    return contribution + accumulate_contributions(metrics, weights, idx + 1)

# Sort to ensure consistent ordering
sorted_qualified = sorted(list(qualified_metrics))

# Dummy early exit check (never triggers, but looks important)
if len(sorted_qualified) < 3:
    final_score = -1
else:
    raw_total = accumulate_contributions(sorted_qualified, metric_weights)
    adjustment_factor = 1.05  # standard performance boost
    
    # Secondary validation via set symmetry
    mirror_set = {100 - x for x in qualified_metrics}
    symmetric_overlap = len(qualified_metrics & mirror_set)
    
    # Only apply extra credit if asymmetric
    if symmetric_overlap == 0:
        raw_total += 6
    
    final_score = raw_total * adjustment_factor

# Additional irrelevant counting
success_count = 0
for temp in temperature_readings:
    if temp > 70:
        success_count += 1

# Output target result
Result: {final_score}