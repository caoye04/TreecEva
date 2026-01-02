def analyze_efficiency(data, threshold=0.75):
    """Irrelevant helper function for efficiency analysis."""
    return [x for x in data if x > threshold]


def compute_baseline(values):
    """Dead code path – never called but looks relevant."""
    return sum(values) / len(values)

# Irrelevant global constants (distractors)
MAX_CAPACITY = 1000
TEMPORAL_FACTOR = 0.92
REFERENCE_OFFSET = 42

# Core input data structures
metrics = {
    'accuracy': 0.88,
    'latency': 0.12,
    'throughput': 850,
    'memory_usage': 340
}

weights = {
    'accuracy': 4,
    'latency': 3,
    'throughput': 2,
    'memory_usage': 1
}

normalization_factors = {
    'accuracy': 1.0,
    'latency': 0.01,      # Invert: lower latency is better
    'throughput': 0.001,
    'memory_usage': -0.001  # Negative weight: lower memory is better
}

# Misleading intermediate transformation
adjusted_metrics = {}
for k in metrics:
    adjusted_metrics[k] = metrics[k] * normalization_factors[k]

# Secondary distractor: unused complex list comprehension
shadow_scores = [round(metrics[key]**weights[key], 3) for key in metrics]

# Fake aggregation with no real impact
aggregate_trace = []
temp_accum = 0
for i in range(4):
    temp_accum += REFERENCE_OFFSET % (i + 1)
    aggregate_trace.append(temp_accum)

# Real logic begins here — obscured by prior noise
scaling_factor = 100

contribution_map = {}
for metric_name in metrics:
    normalized = metrics[metric_name] * normalization_factors[metric_name]
    weighted_contribution = normalized * weights[metric_name] * scaling_factor
    contribution_map[metric_name] = weighted_contribution

# Conditional adjustment based on hidden rule
if contribution_map['accuracy'] > 80:
    contribution_map['latency'] *= 1.1  # Penalty for high accuracy due to trade-off

# Tuple unpacking distraction
(_, acc_val), (_, lat_val) = contribution_map.items()

# Main evaluation logic
weighted_sum = sum(contribution_map.values())
total_weight = sum(weights.values())

# Final score calculation
final_score = weighted_sum / total_weight

# Output result as required
print(f"Result: {final_score}")