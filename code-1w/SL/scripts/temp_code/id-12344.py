def analyze_response_time(rt):
    if rt < 0.1:
        return 'exceptional'
    elif rt < 0.5:
        return 'good'
    elif rt < 1.0:
        return 'average'
    else:
        return 'slow'

# Irrelevant helper function (decoy)
def compute_entropy(data):
    import math
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    entropy = 0.0
    total = len(data)
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Another decoy: unused statistical transformation
def smooth_data(series):
    smoothed = [series[0]]
    for i in range(1, len(series)):
        smoothed.append(0.7 * series[i] + 0.3 * smoothed[i-1])
    return smoothed

# Misleading intermediate processing
def adjust_for_bias(value, bias_factor=1.0):
    # This function is called but its result discarded in key logic
    adjusted = value * (1 - bias_factor * 0.05)
    if adjusted > 100:
        adjusted = 95  # artificial cap
    return adjusted

# Core logic disguised among distractions
def evaluate_consistency(logs):
    consistency_scores = []
    for entry in logs:
        actions = entry['actions']
        diffs = [abs(a - b) for a, b in zip(actions, actions[1:])]
        avg_diff = sum(diffs) / len(diffs) if diffs else 0
        consistency_scores.append(1 / (1 + avg_diff))
    return [round(s * 100) for s in consistency_scores]

# Key computation buried in abstraction
def aggregate_performance(levels, weights):
    mapping = {'exceptional': 90, 'good': 70, 'average': 50, 'below_avg': 30, 'slow': 20}
    raw_values = [mapping.get(level, 0) for level in levels]
    weighted_sum = sum(val * w for val, w in zip(raw_values, weights))
    total_weight = sum(weights)
    base_score = weighted_sum / total_weight if total_weight else 0
    
    # Secondary adjustment based on hidden rule
    penalty = 0
    for i, level in enumerate(levels):
        if level == 'slow' and weights[i] > 0.2:
            penalty += 5
    return int(base_score - penalty)

# Simulated system telemetry (distractor structure)
telemetry = {
    'cpu_load': [0.6, 0.7, 0.8, 0.9],
    'mem_usage_gb': [3.2, 3.8, 4.1, 4.5],
    'temp_c': [65, 68, 70, 73]
}

# Fake calibration data (red herring)
calibration_sequence = [0.11, 0.22, 0.33, 0.44]
transformed = [round(x**2, 3) for x in calibration_sequence]

# Real input data
response_times = [0.08, 0.45, 0.72, 1.2, 0.33]
feedback_levels = [analyze_response_time(rt) for rt in response_times]

# Unused alternate scoring method (dead path)
alt_weights = [0.1, 0.1, 0.1, 0.1, 0.1]
alternate_score = sum(aggregate_performance(feedback_levels[:i+1], alt_weights[:i+1]) for i in range(5)) // 5

# Main weighting reflecting importance
weights = [0.4, 0.3, 0.2, 0.1, 0.05]

# Consistency evaluation (partially relevant)
mock_logs = [
    {'actions': [10, 12, 11, 13]},
    {'actions': [20, 18, 19, 21]},
    {'actions': [5, 7, 6, 8]},
    {'actions': [30, 25, 28, 32]},
    {'actions': [15, 14, 16, 15]}
]
consistency_metrics = evaluate_consistency(mock_logs)

# Apply bias adjustment to consistency (but don't use directly)
bias_adjusted_metrics = [adjust_for_bias(cs, 0.8) for cs in consistency_metrics]

# Critical statement
final_score = aggregate_performance(feedback_levels, weights)

# Print final result as required
print(f"Target result: {final_score}")