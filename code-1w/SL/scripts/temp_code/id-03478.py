def evaluate_performance(metrics, threshold):
    # Initialize tracking variables
    score = 0
    penalty_adjustment = 0
    temp_factor = 1
    cumulative_weight = 0

    # Irrelevant statistical counters (distractor)
    mean_value = sum(metrics.values()) / len(metrics)
    variance_proxy = sum((v - mean_value) ** 2 for v in metrics.values())

    # Weighted evaluation of performance metrics
    weights = {'latency': 3, 'throughput': 5, 'error_rate': -4, 'bandwidth': 2}
    debug_log = []

    for key, value in metrics.items():
        if key in weights:
            contribution = value * weights[key]
            if contribution > threshold * abs(weights[key]):
                score += contribution // 10
            else:
                penalty_adjustment -= 1

        # Dead code path - never executed due to fixed keys
        if key == 'redundant_metric_xyz':
            debug_log.append('Unexpected metric encountered')

    # Complex but partially irrelevant combinatorics (modular arithmetic distraction)
    n = len(metrics)
    r = 2
    if n >= r:
        combinatorial_factor = (n * (n - 1) // 2) % 97  # Modulo to bound size
    else:
        combinatorial_factor = 0

    # Secondary adjustment using dictionary operations
    modifier_map = {k: v % 10 for k, v in metrics.items()}
    for mod_val in modifier_map.values():
        cumulative_weight += (mod_val + penalty_adjustment) % 7

    # Final non-linear transformation
    base_score = score * (cumulative_weight + 1)
    final_score = (base_score - combinatorial_factor) + temp_factor

    return final_score

# Main execution block
metric_data = {
    'latency': 25,
    'throughput': 18,
    'error_rate': 6,
    'bandwidth': 40
}
base_threshold = 100

# Execution point of interest
temp_result = evaluate_performance(metric_data, base_threshold)
final_score = evaluate_performance(metric_data, base_threshold)
print(f"Result: {final_score}")