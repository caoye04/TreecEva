def analyze_trends(data, thresholds):
    trend_scores = {}
    for key, values in data.items():
        above_threshold = sum(1 for v in values if v > thresholds.get(key, 0))
        trend_scores[key] = above_threshold * len(values)
    return trend_scores

# Simulate system health metrics over time
raw_data = {
    'cpu_load': [0.45, 0.52, 0.61, 0.73, 0.81],
    'memory_usage': [0.66, 0.71, 0.75, 0.78, 0.85],
    'disk_io': [0.30, 0.32, 0.41, 0.44, 0.53],
    'network_latency': [45, 67, 52, 89, 76]
}

thresholds_config = {
    'cpu_load': 0.60,
    'memory_usage': 0.70,
    'disk_io': 0.40,
    'network_latency': 60
}

trend_analysis = analyze_trends(raw_data, thresholds_config)

# Misleading distraction: secondary analysis with dead-end logic
consistency_check = {}
for idx, (k, vals) in enumerate(zip(raw_data.keys(), raw_data.values())):
    diffs = [abs(a - b) for a, b in zip(vals, vals[1:])]
    avg_diff = sum(diffs) / len(diffs) if diffs else 0
    consistency_check[k] = round(avg_diff, 3)

# Unused helper function (dead code path - distractor)
def normalize_values(arr):
    max_val = max(arr)
    return [x / max_val for x in arr]

# Weighted scoring setup
metrics = [
    trend_analysis['cpu_load'],
    trend_analysis['memory_usage'],
    trend_analysis['disk_io']
]

weights = [0.4, 0.35, 0.25]

# Auxiliary calculation with red herring variables
baseline_adjustment = 0
for i, m in enumerate(metrics):
    baseline_adjustment += m * 0.05  # minor offset, not actually used later

# Real computation begins here — linear search for dominant metric
max_metric_index = -1
max_value = -1
for i, val in enumerate(metrics):
    if val > max_value:
        max_value = val
        max_metric_index = i

# Conditional adjustment based on position
if max_metric_index == 0:
    adjustment_factor = 1.1
elif max_metric_index == 1:
    adjustment_factor = 1.05
else:
    adjustment_factor = 1.0

intermediate_total = sum(m * w for m, w in zip(metrics, weights))

# Final performance evaluation with adjustment
final_score = intermediate_total * adjustment_factor

# Distractor: unused normalization attempt
normalized_metrics = [m / 10 for m in metrics]  # irrelevant to result

# Output the target result
Target result: {final_score}