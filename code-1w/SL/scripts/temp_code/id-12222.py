def evaluate_performance(weights, metrics):
    # Normalize metrics using min-max scaling (irrelevant for final logic but looks important)
    normalized = {k: (v - min(metrics.values())) / (max(metrics.values()) - min(metrics.values()) + 1e-8) 
                  for k, v in metrics.items()}

    # Apply weight transformation via lambda (semi-relevant)
    transformed_weights = {k: (lambda x: x ** 1.5 if x > 0.5 else x ** 0.5)(w) for k, w in weights.items()}

    # Boost certain metrics conditionally (some distraction here)
    boosted_metrics = {}
    for key in metrics:
        if key in ['latency', 'error_rate']:
            boosted_metrics[key] = metrics[key] * 0.9  # improvement
        elif key == 'throughput':
            boosted_metrics[key] = metrics[key] * 1.1
        else:
            boosted_metrics[key] = metrics[key]

    # Dummy calculation path that computes something unused
    baseline_score = sum(metrics.values()) / len(metrics)
    adjusted_baseline = baseline_score * 0.95 if len(metrics) > 3 else baseline_score * 1.05

    # Core logic: weighted harmonic mean of key indicators (actual answer source)
    key_indicators = ['throughput', 'latency', 'error_rate']
    weighted_inv_sum = 0.0
    weight_sum = 0.0
    for indicator in key_indicators:
        value = boosted_metrics[indicator]
        weight = weights[indicator]
        weighted_inv_sum += weight / (value + 1e-6)  # avoid division by zero
        weight_sum += weight
    
    harmonic_component = weight_sum / weighted_inv_sum if weighted_inv_sum != 0 else 0

    # Secondary component based on conditional expression (used)
    stability_bonus = 10 if metrics['error_rate'] < 5 and metrics['jitter'] < 8 else 5

    # Final score computation
    final_score = harmonic_component + stability_bonus

    # Dead code - never used, just adds confusion
    debug_snapshot = {
        'normalized': normalized,
        'transformed_weights': transformed_weights,
        'baseline': adjusted_baseline
    }
    
    return int(round(final_score))

# Main execution
metric_weights = {
    'throughput': 0.4,
    'latency': 0.3,
    'error_rate': 0.25,
    'jitter': 0.05  # has low weight and isn't in core formula
}

raw_metrics = {
    'throughput': 85,
    'latency': 120,
    'error_rate': 3.5,
    'jitter': 6.2,
    'availability': 99.9
}

final_score = evaluate_performance(metric_weights, raw_metrics)
print(f"Result: {final_score}")