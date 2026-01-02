def evaluate_performance(weights, results):
    # Normalize results using min-max scaling
    min_val = min(results.values())
    max_val = max(results.values())
    normalized = {}
    for k, v in results.items():
        normalized[k] = (v - min_val) / (max_val - min_val) if max_val != min_val else 0.5

    # Irrelevant computation: simulate noise injection (not used in final score)
    noise_offsets = {k: hash(k) % 100 * 0.01 for k in results}
    perturbed = {k: normalized[k] + noise_offsets[k] for k in normalized}

    # Weighted aggregation
    total_weight = sum(weights.values())
    weighted_sum = 0.0
    for metric, weight in weights.items():
        if metric in normalized:
            weighted_sum += normalized[metric] * weight

    # Apply bonus for high consistency (auxiliary logic)
    consistency = 1.0 - (max_val - min_val) / (max_val + 1e-5)
    bonus = 0.1 if consistency > 0.7 else 0.0

    # Dead code: unused branch based on hypothetical condition
    debug_mode = False
    if debug_mode:
        print("Debug info:", normalized, "Bonus applied:", bonus)

    # Final score calculation
    final_score = (weighted_sum / total_weight) + bonus
    return final_score

# Main execution
metric_weights = {'accuracy': 0.4, 'latency': 0.3, 'throughput': 0.2, 'memory': 0.1}
raw_results = {'accuracy': 92, 'latency': 45, 'throughput': 88, 'memory': 60}

# Secondary irrelevant data structure
system_logs = [
    {'timestamp': 1001, 'event': 'init', 'value': 23},
    {'timestamp': 1002, 'event': 'load', 'value': 41},
    {'timestamp': 1003, 'event': 'run', 'value': 17}
]

# Accumulate nothing useful
log_sum = 0
for log in system_logs:
    log_sum += log['value'] * 0.001  # Negligible contribution, just distraction

final_score = evaluate_performance(metric_weights, raw_results)
print(f"Result: {final_score}")