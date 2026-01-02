def evaluate_performance(metrics, importance_weights):
    base_score = 0
    adjustment_factor = 0.85
    temp_result = {}
    legacy_buffer = [0] * len(metrics)  # Unused array - red herring

    for key in metrics:
        if key not in importance_weights:
            continue
        normalized = metrics[key] / (sum(metrics.values()) * 0.01)  # Normalize to percentage scale
        weighted_val = normalized * importance_weights[key]
        base_score += weighted_val

        # Irrelevant intermediate computation (distractor)
        squared_dev = (metrics[key] - sum(metrics.values()) / len(metrics)) ** 2
        temp_result[key] = squared_dev

    # Simulate confidence interval (not used in final score)
    ci_lower = base_score * 0.9
    ci_upper = base_score * 1.1

    # Secondary scoring path with dead logic
    fallback_score = 0
    for v in metrics.values():
        if v > 50:
            fallback_score += 1  # Logic never applied

    # Actual decisive calculation
    final_multiplier = 1.2
    return int(base_score * final_multiplier)

# Main execution context
metric_data = {
    'latency': 45,
    'throughput': 60,
    'accuracy': 75,
    'energy_efficiency': 55
}

weights = {
    'latency': 0.2,
    'throughput': 0.3,
    'accuracy': 0.4,
    'energy_efficiency': 0.1
}

auxiliary_map = {k: v**0.5 for k, v in metric_data.items()}  # Dead computation

intermediate_total = sum([x * 0.5 for x in metric_data.values()])  # Distractor

scaling_constant = 1000  # Unused constant

final_score = evaluate_performance(metric_data, weights)
print(f"Result: {final_score}")