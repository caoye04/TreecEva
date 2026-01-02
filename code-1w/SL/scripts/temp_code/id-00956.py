def evaluate_performance(metrics, weights):
    # Initialize various tracking variables (some are red herrings)
    temp_result = 0
    cumulative = 0
    baseline_adjustment = 0.85
    scaling_factor = 1.2  # Not actually used in final computation

    # Irrelevant transformation (dead code path)
    transformed_metrics = {k: v * 0.95 for k, v in metrics.items() if k != 'accuracy'}

    # Key computation happens here
    weighted_sum = 0
    norm_factor = sum(weights.values())
    for key in metrics:
        if key in weights:
            weighted_sum += metrics[key] * weights[key]
    
    # Additional distracting logic
    if len(metrics) > 3:
        baseline_adjustment *= 1.1
    else:
        baseline_adjustment *= 0.9

    # Another irrelevant lambda (misleading)
    outlier_filter = lambda x: max(0.1, min(x, 0.9))
    filtered_accuracy = outlier_filter(metrics['accuracy'])

    # Actual core logic
    adjusted_weighted = weighted_sum / norm_factor
    penalty = 0
    if metrics['consistency'] < 0.7:
        penalty = 10
    elif metrics['consistency'] > 0.9:
        penalty = -5  # bonus

    # Final score calculation
    raw_score = adjusted_weighted * 100
    final_score = raw_score - penalty

    # More distractions
    diagnostic_log = {
        'input_size': len(metrics),
        'weight_norm': norm_factor,
        'temporal_decay': 0.98,
        'ghost_metric': raw_score * 0.01
    }

    return int(final_score)

# Main execution
metrics = {
    'accuracy': 0.92,
    'precision': 0.85,
    'recall': 0.88,
    'consistency': 0.93,
    'latency': 45
}

weights = {
    'accuracy': 0.4,
    'precision': 0.2,
    'recall': 0.2,
    'consistency': 0.2
}

# Irrelevant pre-processing
buffered_data = [x for x in range(10) if x % 2 == 0]
dummy_aggregate = sum(buffered_data) * 0.1

# Key statement
final_score = evaluate_performance(metrics, weights)

print(f"Result: {final_score}")