def evaluate_performance(metrics, weights):
    base = 0
    bonus = 0
    penalty = 0
    temp_result = {}
    
    # Irrelevant preprocessing: normalize metrics (not actually used in final logic)
    normalized = {}
    for k, v in metrics.items():
        if v > 100:
            normalized[k] = 100
        elif v < 0:
            normalized[k] = 0
        else:
            normalized[k] = v

    # Distractor computation: simulate calibration (unused)
    calibration_factor = sum(metrics.values()) / len(metrics) if metrics else 1
    adjusted_weights = {k: w * calibration_factor for k, w in weights.items()}

    # Actual logic begins
    for key in ['accuracy', 'precision', 'recall']:
        if key in metrics and key in weights:
            base += metrics[key] * weights[key]
    
    # Bonus logic based on threshold
    if metrics.get('f1_score', 0) > 85:
        bonus = 10
    
    # Penalty for missing latency
    if 'latency_ms' in metrics:
        if metrics['latency_ms'] > 200:
            penalty = 5
    else:
        penalty = 3
    
    # Red herring: complex conditional that never affects output
    if 'throughput' in metrics:
        throughput_bonus = metrics['throughput'] // 10
        scaling_factor = throughput_bonus * 0.1
        temp_result['scaled'] = scaling_factor  # unused

    # Final score calculation
    raw_score = base + bonus - penalty
    final_score = int(raw_score)  # critical assignment point
    
    return final_score

# Main execution
metrics_data = {
    'accuracy': 92,
    'precision': 88,
    'recall': 90,
    'f1_score': 89,
    'latency_ms': 180,
    'throughput': 120,
    'energy_consumption': 45
}

weights_scheme = {
    'accuracy': 0.4,
    'precision': 0.3,
    'recall': 0.3,
    'f1_score': 0.2  # not directly used
}

final_score = evaluate_performance(metrics_data, weights_scheme)
print(f"Result: {final_score}")