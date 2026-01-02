def evaluate_performance(data, importance):
    # Initialize various tracking variables (some are red herrings)
    temp_result = 0
    running_total = 0
    adjustment_factor = 1.0
    baseline = sum(data) / len(data) if data else 0
    deviation_sum = 0
    peak_value = max(data) if data else 0

    # Irrelevant statistical distraction
    squared_errors = [(x - baseline) ** 2 for x in data]
    variance = sum(squared_errors) / len(squared_errors) if squared_errors else 0
    stability_index = 1 / (1 + variance)  # Not actually used later

    # Core weighting logic
    weighted_components = map(lambda val, weight: val * weight, data, importance)
    weighted_sum = sum(weighted_components)
    normalizer = sum(importance) if importance else 1

    # Additional distractions
    outlier_count = 0
    for val in data:
        if abs(val - baseline) > 2 * (variance ** 0.5 if variance > 0 else 1):
            outlier_count += 1
    # Dead code path - never accessed due to fixed condition
    if False:
        adjustment_factor *= 0.9

    # More misdirection
    ranking = sorted(enumerate(data), key=lambda x: x[1], reverse=True)
    rank_map = {idx: rank + 1 for rank, (idx, _) in enumerate(ranking)}
    inverse_ranks = [1 / rank_map[i] for i in range(len(data))] if len(data) > 0 else []

    # Actual calculation uses only weighted average
    raw_score = weighted_sum / normalizer if normalizer != 0 else 0

    # Secondary adjustment based on non-outlier count (only uses original length)
    efficiency_modifier = len(data) - 0.5 * outlier_count  # outlier_count is always 0 due to unreachable variance check
    final_score = raw_score * (1 + 0.05 * min(efficiency_modifier, 10))

    # Extra unused transformations
    lambda_shift = (lambda x: x * 1.05)(raw_score)
    buffer_list = [final_score + i * 0.1 for i in range(3)]
    snapshot = {"score": final_score, "timestamp": 1234567890}

    return final_score

# Main execution block
metrics = [85, 90, 78, 92, 88]
weights = [0.1, 0.2, 0.15, 0.3, 0.25]

# Setup intermediate variables that look important but aren't all used
preliminary_avg = sum(metrics) / len(metrics)
discount_rate = 0.02
normalization_offset = 5

# Key statement
final_score = evaluate_performance(metrics, weights)

print(f"Result: {final_score}")