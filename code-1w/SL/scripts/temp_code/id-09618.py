def evaluate_performance(metrics, thresholds):
    # Initialize various tracking variables (some are distractions)
    temp_result = 0
    running_total = 0
    debug_log = []
    auxiliary_sum = 0  # unused in final logic

    # Relevant set operations to filter valid metrics
    valid_keys = set(thresholds.keys()) & set(metrics.keys())
    filtered_metrics = {k: metrics[k] for k in valid_keys}

    # Misleading loop - computes something not used later
    for metric in ['throughput', 'latency', 'error_rate']:
        if metric in metrics:
            auxiliary_sum += metrics[metric] // 10  # dead computation

    # Core logic: count how many metrics exceed their threshold
    passed_count = 0
    for key in filtered_metrics:
        if metrics[key] > thresholds[key]:
            passed_count += 1
            running_total += metrics[key]

    # Lambda function to compute bonus factor based on passed tests
    bonus_factor = (lambda x: 1.5 if x >= 3 else 1.1)(passed_count)

    # Another distraction: complex but unused calculation
    outlier_detection = len(set(metrics.values())) > len(metrics) * 0.7
    complexity_score = len(valid_keys) ** 2 if outlier_detection else 0  # irrelevant

    # Final score computation depends only on running_total and bonus_factor
    adjustment = len(filtered_metrics) if passed_count > 0 else 0
    temp_result = running_total * bonus_factor + adjustment

    return int(temp_result)

# Main execution block
if __name__ == "__main__":
    # Input data
    system_metrics = {
        'response_time': 120,
        'throughput': 450,
        'concurrency': 80,
        'error_rate': 0.02,
        'availability': 99.95
    }

    threshold_set = {
        'response_time': 100,
        'throughput': 400,
        'concurrency': 75,
        'availability': 99.9,
        'reliability': 99.0  # not in metrics
    }

    # Extraneous preprocessing step (no impact)
    normalized = {k: v * 1.0 for k, v in system_metrics.items() if isinstance(v, (int, float))}
    scaling_factor = sum(normalized.values()) / len(normalized) if normalized else 1

    # Key statement
    final_score = evaluate_performance(system_metrics, threshold_set)
    
    print(f"Result: {final_score}")