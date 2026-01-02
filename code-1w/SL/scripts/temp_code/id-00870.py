def evaluate_performance(metrics, baseline):
    # Normalize metrics using baseline
    normalized = {k: (v - baseline[k]) / baseline[k] for k, v in metrics.items() if k in baseline}

    # Irrelevant transformation: unused derived metrics
    derived_metrics = {key: val ** 2 for key, val in normalized.items()}
    temp_result = sum(derived_metrics.values()) * 0.1  # Distractor computation

    # Weighted scoring with conditional weights
    weights = {
        'latency': 0.4 if normalized.get('latency', 0) < 0.2 else 0.2,
        'throughput': 0.5 if normalized.get('throughput', 0) > 0.3 else 0.3,
        'error_rate': -0.3 if normalized.get('error_rate', 0) > 0.1 else -0.1
    }

    # Compute raw score
    raw_score = sum(normalized.get(k, 0) * w for k, w in weights.items())

    # Apply nonlinear adjustment using lambda
    adjuster = lambda x: x * 1.5 if x > 0 else x * 0.8
    adjusted_score = adjuster(raw_score)

    # Set operations to filter valid contributions (demonstrating set logic)
    valid_keys = set(weights.keys()) & set(normalized.keys())
    key_count_factor = len(valid_keys) if valid_keys else 1

    # Dead code path: never executed due to fixed condition
    debug_mode = False
    if debug_mode:
        print("Debug info:", derived_metrics)  # Unused branch

    # Final aggregation with key count scaling
    final_score = adjusted_score * key_count_factor

    return final_score

# Baseline system performance
baseline = {
    'latency': 100,
    'throughput': 200,
    'error_rate': 0.05
}

# Current system metrics
metrics = {
    'latency': 110,
    'throughput': 270,
    'error_rate': 0.08,
    'memory_usage': 150  # Irrelevant metric, not in baseline
}

# Execute evaluation
temp_data = [metrics[k] for k in metrics if k != 'memory_usage']
summary_stat = sum(temp_data) // len(temp_data)  # Intermediate distractor

final_score = evaluate_performance(metrics, baseline)
print(f"Result: {final_score}")