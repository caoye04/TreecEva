def analyze_trends(data, thresholds):
    trend_summary = {}
    for key, values in data.items():
        above_threshold = sum(1 for v in values if v > thresholds.get(key, 0))
        trend_summary[key] = above_threshold
    return trend_summary

# Simulated system diagnostics and performance logs
diagnostic_data = {
    'cpu_load': [0.7, 0.8, 0.9, 0.6, 0.75],
    'memory_usage': [0.6, 0.65, 0.75, 0.8, 0.72],
    'disk_io': [0.5, 0.55, 0.65, 0.7, 0.68]
}

threshold_config = {
    'cpu_load': 0.72,
    'memory_usage': 0.68,
    'disk_io': 0.6
}

# Extract temporal patterns (irrelevant for final result but adds cognitive load)
temporal_analysis = analyze_trends(diagnostic_data, threshold_config)

# Red herring: System health assessment (not used later)
health_flags = {k: 'CRITICAL' if v > 2 else 'NORMAL' for k, v in temporal_analysis.items()}

# Core evaluation logic
feedback_log = [
    {'metric': 'accuracy', 'value': 0.92, 'weight': 0.4},
    {'metric': 'latency', 'value': 0.15, 'weight': 0.3},
    {'metric': 'throughput', 'value': 850, 'weight': 0.3}
]

benchmark_weights = {
    'accuracy': 0.4,
    'latency': 0.3,
    'throughput': 0.3
}

# Distractor: Normalize throughput using slicing (semi-relevant but misleading)
normalized_throughput = feedback_log[2]['value'] / 1000  # Scale to 0-1
feedback_log[2]['value'] = normalized_throughput

# Distractor: Create cumulative history (unused)
history_window = feedback_log[1:] + [{'metric': 'dummy', 'value': 0.0, 'weight': 0.0}]

# Actual scoring logic
base_scores = []
for entry in feedback_log:
    raw = entry['value']
    if entry['metric'] == 'latency':
        # Invert latency since lower is better
        raw = 1 - min(raw, 0.9)  # Cap at 0.9 to avoid negative inversion
    base_scores.append(raw * entry['weight'])

aggregate = sum(base_scores)

# Apply non-linear adjustment based on confidence window (real computation)
if aggregate > 0.7:
    adjustment_factor = 1.1
else:
    adjustment_factor = 0.95

adjusted_score = aggregate * adjustment_factor

# Final calibration using dictionary lookup and slicing
calibration_map = {0.9: 0.05, 0.8: 0.03, 0.7: 0.01, 0.6: -0.02}
slice_key = round(adjusted_score, 1)
boost = calibration_map.get(slice_key, 0)

final_score = adjusted_score + boost

# Print result as required
print(f"Result: {final_score}")