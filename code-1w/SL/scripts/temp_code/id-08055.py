def analyze_efficiency(data, thresholds):
    filtered = [x for x in data if x > thresholds[0]]
    squared = list(map(lambda x: x ** 2, filtered))
    avg = sum(squared) / len(squared) if squared else 0
    return avg

# Simulate system performance metrics
data_points = [3, 5, 7, 2, 8, 6, 9, 4]
temp_thresholds = [4, 6, 1]

interim_result = analyze_efficiency(data_points, temp_thresholds)

# Unrelated diagnostic computation (distractor)
diagnostic_trace = set(data_points).difference(set(temp_thresholds))
diag_sum = sum([x for x in diagnostic_trace if x % 2 == 0])

# Core evaluation logic
metrics = [interim_result, len(diagnostic_trace), diag_sum]
benchmark_weights = [0.5, 2, 0.1]

# Auxiliary helper with misleading relevance
def compute_baseline(metric_set):
    base = 0
    for i, val in enumerate(metric_set):
        if i % 2 == 0:
            base += val * 1.5
        else:
            base -= val * 0.5
    return base

baseline_adjustment = compute_baseline(metrics)

# Main scoring logic
weighted_sum = sum(m * w for m, w in zip(metrics, benchmark_weights))
penalty_factor = 0.9 if len(data_points) > 5 else 1.0

# Secondary adjustment using slicing (semi-relevant)
sorted_metrics = sorted(metrics)
mid_values = sorted_metrics[1:-1]  # middle values only
adjustment = sum(mid_values) * 0.2

# Final integration
raw_score = weighted_sum + adjustment
final_score = int(raw_score * penalty_factor + baseline_adjustment * 0.1)

# Print result as required
print(f"Result: {final_score}")