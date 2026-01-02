def evaluate_performance(weights, data):
    # Normalize data using min-max scaling (irrelevant for final result)
    min_val = min(data)
    max_val = max(data)
    normalized = [(x - min_val) / (max_val - min_val + 1e-9) for x in data]

    # Apply weight transformation via lambda (semi-relevant)
    weighted_metrics = list(map(lambda w: w ** 0.85, weights))

    # Compute weighted sum - this is where final_score is actually determined
    raw_sum = sum(d * w for d, w in zip(data, weights))
    adjustment_factor = 1.0

    # Simulate legacy compatibility mode (dead code path)
    legacy_mode = False
    if legacy_mode:
        adjustment_factor = 0.95
        temp_buffer = [raw_sum * 0.1] * 5
        for i in range(len(temp_buffer)):
            adjustment_factor *= 0.99  # Distractor loop

    # Secondary calculation: efficiency ratio (not used in final score)
    baseline = sum(data) / len(data)
    efficiency_ratio = sum(1 for x in data if x > baseline) / len(data)

    # Core logic: final score depends only on raw_sum and fixed adjustment
    base_score = raw_sum * 0.75
    penalty = 0.0

    # Conditional penalty based on symmetry (untriggered, distractor)
    if len(data) % 2 == 0 and data[0] < data[-1]:
        penalty = 5.0

    final_score = base_score - penalty  # Only this line matters

    # Extraneous post-processing (no effect)
    outlier_count = sum(1 for x in data if abs(x - baseline) > 2 * (max_val - min_val) * 0.1)
    if outlier_count > 2:
        final_score *= 0.98

    return int(final_score)

# Main execution
metric_weights = [0.9, 0.7, 0.5, 0.3, 0.1]
raw_results = [88, 92, 76, 85, 90]

# Irrelevant pre-computations
average_weight = sum(metric_weights) / len(metric_weights)
sorted_pairs = sorted(zip(metric_weights, raw_results), reverse=True)
duplicate_calc = sum(w * r for w, r in sorted_pairs)  # Not used later

final_score = evaluate_performance(metric_weights, raw_results)
print(f"Result: {final_score}")