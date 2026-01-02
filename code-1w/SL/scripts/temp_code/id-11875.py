def evaluate_performance(metrics, weights):
    # Normalize metrics using min-max scaling (irrelevant for final logic)
    max_metric = max(metrics)
    min_metric = min(metrics)
    normalized = [(m - min_metric) / (max_metric - min_metric + 1e-8) for m in metrics]

    # Apply weights to original metrics (this is what actually matters)
    weighted_sum = sum(m * w for m, w in zip(metrics, weights))

    # Distraction: calculate entropy-like value (not used)
    import math
    entropy = -sum(p * math.log(p + 1e-8) for p in normalized)

    # Threshold filtering based on arbitrary cutoffs (semi-relevant but overridden)
    filtered_metrics = [m for m in metrics if m > 0.5]
    if len(filtered_metrics) < 3:
        adjustment = 0.9
    else:
        adjustment = 1.0  # This path is taken, but adjustment not applied later

    # Bitwise interference: XOR all integer parts (completely irrelevant)
    metric_ints = [int(m * 100) for m in metrics]
    checksum = 0
    for val in metric_ints:
        checksum ^= val

    # Final computation depends only on weighted_sum and fixed bias
    bias = 0.75
    score = weighted_sum + bias

    # Additional distraction: update checksum with weights (unused)
    weight_ints = [int(w * 100) for w in weights]
    for val in weight_ints:
        checksum ^= val

    # Correct result is based solely on weighted_sum + bias
    return int(score * 100)  # Convert to integer percentage

# Main execution
if __name__ == "__main__":
    # Simulated model evaluation metrics (precision, recall, f1, latency_penalty, robustness)
    metrics = [0.82, 0.77, 0.85, 0.91, 0.79]
    weights = [0.3, 0.2, 0.25, 0.15, 0.1]  # Weight distribution across criteria

    # Irrelevant set operations (distractor)
    high_performers = {i for i, m in enumerate(metrics) if m > 0.8}
    medium_performers = {i for i, m in enumerate(metrics) if 0.7 <= m <= 0.8}
    overlap_count = len(high_performers & medium_performers)

    # Key statement
    final_score = evaluate_performance(metrics, weights)

    print(f"Result: {final_score}")