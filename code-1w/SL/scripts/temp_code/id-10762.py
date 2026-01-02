def evaluate_performance(metrics, weights):
    # Initialize various intermediate values, some of which are distractions
    base_score = 0
    bonus_factor = 1.0
    penalty_adjustment = 0
    temp_result = {}

    # Relevant computation: weighted sum of performance metrics
    weighted_sum = sum(metrics[metric] * weights.get(metric, 0) for metric in metrics)

    # Distractor: complex but unused dictionary transformation
    transformed_metrics = {k.upper(): v * 2 for k, v in metrics.items() if v > 50}
    aggregated_key = ''.join(transformed_metrics.keys())
    dummy_aggregation = len(aggregated_key) + sum(transformed_metrics.values()) if transformed_metrics else 0

    # Conditional expression affecting bonus factor (partially relevant)
    bonus_factor = 1.2 if 'accuracy' in metrics and metrics['accuracy'] > 85 else 1.0

    # More distraction: set operations with no impact on final result
    metric_set_a = set(metrics.keys())
    metric_set_b = {'accuracy', 'latency', 'throughput'}
    common_metrics = metric_set_a & metric_set_b
    extra_flags = {flag: True for flag in common_metrics}

    # Simulated penalty logic based on latency (only applies if very high)
    if 'latency' in metrics and metrics['latency'] > 120:
        penalty_adjustment -= 10
    elif 'latency' in metrics and metrics['latency'] < 40:
        penalty_adjustment += 5  # Reward low latency but not used directly

    # Actual scoring logic with dependency chain
    base_score += weighted_sum * bonus_factor
    base_score += penalty_adjustment  # Minor effect

    # Additional irrelevant state tracking
    execution_trace = []
    execution_trace.append('start')
    execution_trace.append('weight_calculation')
    execution_trace.append('bonus_applied')

    # Final score adjusted by hidden rule: cap at 95 if throughput is excellent
    final_score = base_score
    if 'throughput' in metrics and metrics['throughput'] > 90:
        if final_score > 95:
            final_score = 95  # Performance cap for stability reasons

    return final_score

# Main execution block
metrics_data = {
    'accuracy': 88,
    'latency': 35,
    'throughput': 92,
    'memory_usage': 65,
    'scalability': 78
}

weights_config = {
    'accuracy': 0.4,
    'latency': -0.1,
    'throughput': 0.3,
    'memory_usage': 0.1,
    'scalability': 0.2
}

# Irrelevant pre-computations
baseline_avg = sum(metrics_data.values()) / len(metrics_data)
dummy_ratio = baseline_avg / (weights_config['accuracy'] * 10)

# Key statement
final_score = evaluate_performance(metrics_data, weights_config)

print(f"Result: {final_score}")