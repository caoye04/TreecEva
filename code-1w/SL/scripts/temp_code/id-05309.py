def evaluate_performance(metrics, weights):
    # Normalize metrics using min-max scaling (irrelevant for final result)
    max_metric = max(metrics) if metrics else 1
    normalized = [m / max_metric for m in metrics] if max_metric != 0 else metrics

    # Transform weight keys to uppercase (distractor)
    upper_weights = {k.upper(): v for k, v in weights.items()}

    # Extract specific metrics needed for scoring
    accuracy = metrics.get('accuracy', 0)
    latency = metrics.get('latency', 0)
    throughput = metrics.get('throughput', 0)

    # Compute derived values (some irrelevant)
    latency_penalty = 100 - min(latency, 100)  # Not used later
    efficiency_ratio = throughput / (latency + 1) if latency > 0 else throughput

    # Weight mapping (only two are actually used)
    w_acc = weights.get('accuracy', 1.0)
    w_eff = weights.get('efficiency', 1.5)
    w_sec = weights.get('security', 0.8)  # Unused weight

    # Simulated calibration offset (dead computation)
    calibration_adjustment = sum(upper_weights.values()) * 0.01

    # Core logic: score based on accuracy and efficiency only
    base_score = accuracy * w_acc
    adjusted_score = base_score + (efficiency_ratio * w_eff)

    # Apply artificial cap (relevant)
    capped_score = min(adjusted_score, 95.6)

    # Additional transformation (no effect due to order)
    temp_result = capped_score ** 1.0  # Redundant operation

    # Final adjustment
    final_score = round(temp_result, 2)

    return final_score


# Main execution block
if __name__ == '__main__':
    # Define input data
    metric_set = {
        'accuracy': 88.4,
        'latency': 42,
        'throughput': 68,
        'reliability': 91  # Unused metric
    }

    benchmark_weights = {
        'accuracy': 1.2,
        'efficiency': 1.5,
        'security': 0.9,  # Irrelevant key
        'usability': 0.7  # Irrelevant key
    }

    # Intermediate computations with side effects (mostly distractors)
    total_metrics = len(metric_set)
    avg_metric_value = sum(metric_set.values()) / total_metrics
    metric_names_upper = set(name.upper() for name in metric_set.keys())
    weight_keys = set(benchmark_weights.keys())
    common_keys = metric_names_upper.intersection(weight_keys)  # Slight relevance

    scaling_factor = len(common_keys) * 0.1  # Computed but unused

    # Key statement
    final_score = evaluate_performance(metric_set, benchmark_weights)

    # Print result as required
    print(f"Result: {final_score}")