def calculate_final_score(raw_data, importance_weights):
    # Preprocess: extract and normalize values
    normalized = {}
    total_weight = sum(importance_weights.values())
    temp_values = []
    
    for key, value in raw_data.items():
        if key in ['metric_a', 'metric_b', 'metric_c']:
            normalized[key] = value / (value + 10)  # Avoid division by zero
            temp_values.append(normalized[key])

    # Distractor: unused transformation
    inverted_metrics = {k: 1/v for k, v in normalized.items() if v != 0}
    avg_inverted = sum(inverted_metrics.values()) / len(inverted_metrics) if inverted_metrics else 0

    # Weighted aggregation
    weighted_sum = 0.0
    for metric, norm_value in normalized.items():
        weight = importance_weights.get(metric, 0)
        weighted_sum += norm_value * weight
    
    # Bonus logic based on threshold
    bonus_trigger = all(v > 0.5 for v in normalized.values())
    adjustment_factor = 1.2 if bonus_trigger else 0.9
    
    # Secondary distractor: complex slicing with no impact
    history_log = temp_values[::-1][:len(temp_values)//2 + 1]
    if len(history_log) > 1:
        trend_estimate = (history_log[0] - history_log[-1]) * 100
    else:
        trend_estimate = 0

    # Final computation
    base_score = weighted_sum / total_weight if total_weight != 0 else 0
    final_score = base_score * adjustment_factor

    # Irrelevant dictionary update
    diagnostics = {
        'base': base_score,
        'adjustment': adjustment_factor,
        'bonus_applied': bonus_trigger,
        'trend': trend_estimate,
        'inverted_avg': avg_inverted
    }
    
    return final_score

# Input data
metrics = {
    'metric_a': 15,
    'metric_b': 25,
    'metric_c': 35,
    'metric_d': 45  # This one will be ignored
}

weights = {
    'metric_a': 0.2,
    'metric_b': 0.3,
    'metric_c': 0.5
}

# Execution point
final_score = calculate_final_score(metrics, weights)
print(f"Result: {final_score}")