def evaluate_performance(weights, results):
    # Normalize results using min-max scaling (irrelevant for final logic but adds distraction)
    min_val, max_val = min(results.values()), max(results.values())
    normalized = {k: (v - min_val) / (max_val - min_val + 1e-8) for k, v in results.items()}

    # Apply weight transformation via lambda (relevant)
    weighted_transform = lambda w, x: w ** 0.5 * x ** 2

    # Distractor: unused function simulating alternative scoring
    def legacy_score(w_dict, r_dict):
        return sum(r_dict[k] * 0.9 for k in r_dict) % 100

    # Intermediate calculation: efficiency ratio (semi-relevant)
    total_effort = sum(results.get(key, 0) for key in ['tasks', 'errors', 'timeouts'])
    success_count = results.get('tasks', 0) - results.get('errors', 0)
    efficiency_ratio = (success_count / (total_effort + 1)) if total_effort > 0 else 0

    # Key metric processing with dictionary and set operations
    active_metrics = set(results.keys()) & set(weights.keys())
    adjustment_factor = len(active_metrics) / len(weights)  # semi-relevant

    # Core computation chain
    raw_sum = sum(results[m] for m in active_metrics)
    weight_sum = sum(weights[m] for m in active_metrics)
    composite_base = raw_sum * adjustment_factor

    # Apply nonlinear transformation using lambda and weighting
    transformed = 0
    for metric in active_metrics:
        if metric == 'tasks':
            transformed += weighted_transform(weights[metric], results[metric])
        elif metric == 'throughput':
            transformed += weights[metric] * results[metric] * efficiency_ratio
        else:
            transformed += weights[metric] * results[metric] * 0.5

    # Final score computed from transformed components
    stability_bonus = 1.0 if results.get('errors', 0) < 3 else 0.7
    final_score = int((transformed * stability_bonus) + (composite_base * 0.3))

    # Dead code path - never executed (distractor)
    if False:
        final_score = max(final_score, 50)
        buffer = [0] * 100

    return final_score

# Main execution context
metric_weights = {
    'tasks': 0.4,
    'throughput': 0.35,
    'errors': 0.1,
    'timeouts': 0.05,
    'latency': 0.1
}

raw_results = {
    'tasks': 85,
    'throughput': 72,
    'errors': 2,
    'timeouts': 1,
    'latency': 44
}

# Statement of interest
final_score = evaluate_performance(metric_weights, raw_results)
print(f"Result: {final_score}")