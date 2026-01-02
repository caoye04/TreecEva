def evaluate_performance(metrics, weights):
    # Initialize intermediate variables (some are distractions)
    base_score = 0
    penalty_adjustment = 0
    bonus_multiplier = 1.0
    temp_sum = 0
    outlier_count = 0

    # Real computation begins
    weighted_total = 0
    weight_sum = 0

    for key in metrics:
        if key in weights:
            weighted_total += metrics[key] * weights[key]
            weight_sum += weights[key]

    # Compute average performance score
    if weight_sum > 0:
        base_score = weighted_total / weight_sum

    # Distraction: Analyze variance-like metric (not used)
    squared_diffs = []
    for val in metrics.values():
        diff = val - base_score
        squared_diffs.append(diff * diff)  # Not actually influencing final result

    # Bonus logic based on completeness (only if all 5 metrics present)
    if len(metrics) >= 5:
        bonus_multiplier = 1.1

    # Penalty for outliers (defined as values < 10)
    for val in metrics.values():
        if val < 10:
            penalty_adjustment -= 2

    # Additional distraction: simulate data smoothing
    smoothed_values = {}
    for k, v in metrics.items():
        if k.endswith('_rate'):
            smoothed_values[k] = round(v * 0.95, 2)  # unused

    # Final aggregation
    final_score = (base_score + penalty_adjustment) * bonus_multiplier

    # More distraction: normalize to scale (unused path)
    if final_score > 100:
        normalized = final_score / 1.5  # dead code due to input constraints

    return int(final_score)

# Main execution
if __name__ == '__main__':
    # Input data
    metrics = {
        'throughput': 85,
        'latency': 12,
        'error_rate': 3,
        'availability': 99,
        'response_time': 15,
        'reliability': 95
    }

    weights = {
        'throughput': 0.3,
        'latency': 0.2,
        'error_rate': 0.25,
        'availability': 0.1,
        'response_time': 0.15
    }

    # Unused variables (distractors)
    expected_range = (0, 100)
    calibration_factor = 0.987
    debug_trace = []

    # Key statement
    final_score = evaluate_performance(metrics, weights)

    print(f"Target result: {final_score}")