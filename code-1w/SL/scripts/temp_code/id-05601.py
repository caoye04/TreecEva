def evaluate_performance(log, threshold):
    # Initialize tracking variables
    success_count = 0
    warning_count = 0
    temp_adjustment = 0.0
    volatility_index = 0.0

    # Irrelevant statistical counters (distractors)
    total_entries = len(log)
    outlier_count = 0
    cumulative_bias = 0.0

    for entry in log:
        metric_val = entry['value']
        category = entry['type']

        # Real logic: count successes above threshold
        if metric_val > threshold:
            success_count += 1
            if category == 'critical':
                temp_adjustment += 0.3
        elif metric_val < threshold * 0.5:
            warning_count += 1
            # Distractor: this affects nothing
            cumulative_bias += metric_val * 0.1

        # Volatility calculation - semi-relevant but not used directly
        if category in ['fluctuating', 'volatile']:
            volatility_index += abs(metric_val - threshold) * 0.1

        # Dead code path (never executed due to fixed categories)
        if category == 'deprecated':
            outlier_count += 1  # Unreachable

    # Core computation: performance score based on success rate
    performance_ratio = success_count / total_entries if total_entries else 0
    penalty = warning_count * 1.5

    # Secondary adjustment using dictionary-based weight map
    weight_map = {'critical': 2, 'standard': 1, 'auxiliary': 0}
    bonus = 0
    for entry in log:
        bonus += weight_map.get(entry['type'], 0) * (1 if entry['value'] > threshold else 0)

    # Final score with red herring terms that cancel out
    final_score = int(
        (performance_ratio * 100) + 
        bonus - 
        penalty + 
        temp_adjustment - 
        temp_adjustment  # Cancels itself
    )

    return final_score

# Simulated telemetry data from system health monitor
data_log = [
    {'value': 78, 'type': 'critical'},
    {'value': 65, 'type': 'standard'},
    {'value': 40, 'type': 'standard'},
    {'value': 88, 'type': 'critical'},
    {'value': 30, 'type': 'standard'},
    {'value': 70, 'type': 'auxiliary'},
    {'value': 90, 'type': 'critical'},
    {'value': 60, 'type': 'standard'}
]

base_threshold = 70
final_score = evaluate_performance(data_log, base_threshold)
print(f"Result: {final_score}")