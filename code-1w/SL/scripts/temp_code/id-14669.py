def evaluate_performance(data, importance):
    temp_results = []
    normalized = {}
    total_weight = sum(importance.values())
    adjusted_weights = {k: v / total_weight for k, v in importance.items()}
    
    # Irrelevant pre-processing (distractor)
    outlier_threshold = max(data['accuracy']) * 0.1
    filtered_data = {k: [x for x in v if x > outlier_threshold] for k, v in data.items()}
    
    # Real computation begins
    for key in data:
        raw_avg = sum(data[key]) / len(data[key])
        normalized[key] = round(raw_avg, 3)
    
    # Weighted scoring logic
    weighted_sum = 0.0
    for metric, score in normalized.items():
        if metric in adjusted_weights:
            weighted_sum += score * adjusted_weights[metric]
    
    # Secondary adjustment based on consistency (real impact)
    variance_penalty = 0
    for values in data.values():
        mean_val = sum(values) / len(values)
        variance = sum((x - mean_val) ** 2 for x in values) / len(values)
        variance_penalty += variance * 0.01  # minor penalty

    # Dummy structures (set usage and slicing - required features)
    history_log = list(normalized.values())
    recent_trend = history_log[-3:]  # slicing
    fluctuation_set = set(recent_trend)  # set operation
    stability_bonus = 1.0 if len(fluctuation_set) < 3 else 0.95

    # Final calculation
    base_performance = weighted_sum - variance_penalty
    final_score = int(round(base_performance * stability_bonus))

    # Dead code path (misleading)
    if len(fluctuation_set) == 0:
        final_score *= 2  # never reached

    return final_score

# Main execution
metrics = {
    'accuracy': [0.88, 0.92, 0.85, 0.91],
    'latency': [45, 60, 50, 55],
    'throughput': [80, 75, 85, 90],
    'memory_usage': [100, 95, 110, 90]  # higher is worse
}

weights = {
    'accuracy': 4,
    'latency': 3,
    'throughput': 2,
    'memory_usage': 1
}

# Invert memory usage to align with 'higher is better'
for i in range(len(metrics['memory_usage'])):
    orig_val = metrics['memory_usage'][i]
    inverted = 200 - orig_val  # simple inversion
    metrics['memory_usage'][i] = inverted

# Execute main logic
temp_var = [x * 1.1 for x in metrics['latency']]  # irrelevant transformed copy
unused_dict = {'x': sum(temp_var), 'y': len(temp_var)}  # dead storage

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")