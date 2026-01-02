def evaluate_performance(metrics, importance_weights):
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []
    
    # Irrelevant pre-processing: Normalize unused metric names
    normalized_keys = {k.lower().strip(): v for k, v in metrics.items()}
    temp_aggregate = sum([v for v in importance_weights.values() if v > 0.1])

    consistency_check = True
    for key, weight in importance_weights.items():
        if key in metrics:
            raw_value = metrics[key]
            weighted_contribution = raw_value * weight
            
            # Apply conditional logic based on performance bands
            if raw_value >= 90:
                base_score += weighted_contribution + 2
                bonus_tracker.append(weighted_contribution)
            elif raw_value >= 75:
                base_score += weighted_contribution
            else:
                base_score += weighted_contribution - 1
                penalty_adjustment += 1

            # Red herring: Track artificial decay (never used)
            decay_factor = 0.95 ** penalty_adjustment
            _ = decay_factor * 10  # Distractor computation

    # Unused data structure manipulation
    historical_scores = set()
    for val in metrics.values():
        historical_scores.add(round(val / 10) * 10)

    # Another distraction: compute but don't use correlation proxy
    magnitude_proxy = len(historical_scores) * temp_aggregate

    # Final adjustment based on bonus frequency (only uses length)
    if len(bonus_tracker) >= 2:
        base_score += 3

    return int(base_score)

# Main execution
metric_data = {
    'response_time': 95,
    'accuracy': 88,
    'throughput': 70,
    'reliability': 92
}

weights = {
    'response_time': 0.3,
    'accuracy': 0.4,
    'throughput': 0.2,
    'reliability': 0.5
}

auxiliary_map = {'low': 1, 'high': 5}
buffer_cache = [0] * len(auxiliary_map)  # Dead code path

final_score = evaluate_performance(metric_data, weights)
print(f"Result: {final_score}")