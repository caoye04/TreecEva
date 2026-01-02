def evaluate_performance(metrics, base):
    # Initialize various tracking variables
    temp_result = 0
    accumulator = 0
    deviation_count = 0
    total_variance = 0.0

    # Baseline thresholds (some are red herrings)
    thresholds = {k: 50 + i for i, k in enumerate(base.keys())}
    ignored_sum = sum([len(str(val)) for val in thresholds.values()])  # Irrelevant computation

    metric_set_filtered = {k: v for k, v in metrics.items() if v > 0}  # Remove non-positive entries

    # Real logic begins: analyze deviations from baseline
    for key in metric_set_filtered:
        if key in base:
            diff = abs(metric_set_filtered[key] - base[key])
            if diff > 10:
                deviation_count += 1
            total_variance += diff

    # Secondary processing with slicing simulation (string representation of numbers)
    str_repr = ''.join([str(int(v)) for v in metric_set_filtered.values()])
    slice_value = int(str_repr[1:-1]) if len(str_repr) > 2 else 0  # Middle digits extraction

    # Set operations to determine coverage
    provided_metrics = set(metrics.keys())
    required_metrics = set(base.keys())
    missing = required_metrics - provided_metrics
    coverage_ratio = len(provided_metrics & required_metrics) / len(required_metrics)

    # Dummy state tracker (not used in final result)
    status_log = []
    for i in range(len(missing) + 1):
        status_log.append(f"Check {i}: OK")

    # Core calculation
    raw_score = 0
    for k in provided_metrics:
        if k in base:
            raw_score += min(metrics[k], base[k]) * 1.5

    adjustment = (coverage_ratio * 100) - (deviation_count * 5)
    final_score = int(raw_score + adjustment + (slice_value % 10))  # Final deterministic computation

    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Define inputs
baseline_data = {'throughput': 80, 'latency': 45, 'error_rate': 2, 'availability': 99}
metric_set = {'throughput': 85, 'latency': 50, 'error_rate': 3, 'scalability': 70}

# Execute and capture result
evaluate_performance(metric_set, baseline_data)