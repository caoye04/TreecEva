def evaluate_performance(metrics, weights):
    # Initialize intermediate variables (some are distractions)
    base_score = 0
    penalty_adjustment = 0
    bonus_multiplier = 1.0
    temp_sum = 0
    outlier_count = 0

    # Real computation begins: weighted sum of valid metrics
    for key in metrics:
        if key in weights and metrics[key] >= 0:  # Only consider non-negative metrics
            base_score += metrics[key] * weights[key]
        elif metrics[key] < 0:
            outlier_count += 1

    # Distractor: irrelevant accumulation
    for val in metrics.values():
        temp_sum += val ** 2  # Used nowhere in final result

    # Apply penalty if too many outliers (not actually triggered in this input)
    if outlier_count > 2:
        penalty_adjustment = -10

    # Simulate combinatorics: number of possible metric pairs
    n_metrics = len(metrics)
    possible_pairs = n_metrics * (n_metrics - 1) // 2  # distraction

    # Bonus logic: only applies if precision and recall are both high
    if 'precision' in metrics and 'recall' in metrics:
        if metrics['precision'] > 0.8 and metrics['recall'] > 0.8:
            bonus_multiplier = 1.25

    # Dummy loop: simulates state tracking but irrelevant
    status_log = {}
    for i in range(3):
        status_log[i] = f'Step {i}: Processing...'
    # End of distraction

    # Core result calculation
    raw_result = base_score + penalty_adjustment
    final_score = raw_result * bonus_multiplier

    # Normalize using modular arithmetic (only affects result when above threshold)
    if final_score > 100:
        final_score = (final_score % 89) + 11  # maps to 11-99 range

    return final_score


# Main execution
metrics_data = {
    'accuracy': 0.85,
    'precision': 0.92,
    'recall': 0.90,
    'latency_ms': -5,      # invalid, triggers outlier but not enough to penalize
    'throughput': 450
}

weights_map = {
    'accuracy': 0.3,
    'precision': 0.25,
    'recall': 0.25,
    'throughput': 0.2
}

# Unused variables - red herrings
baseline_avg = sum(metrics_data.values()) / len(metrics_data)  # includes negative
config_flags = {'debug': False, 'verbose': True, 'mode': 'production'}
intermediate_total = 0
for k, v in metrics_data.items():
    intermediate_total += len(k) * v  # irrelevant computation

final_score = evaluate_performance(metrics_data, weights_map)
print(f"Result: {final_score}")