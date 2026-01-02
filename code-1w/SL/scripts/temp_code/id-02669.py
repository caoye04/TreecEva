def analyze_efficiency(values):
    total_ops = sum(values)
    avg_op_time = sum([x / (i + 1) for i, x in enumerate(values)])
    efficiency_ratio = total_ops / (avg_op_time + 1e-5)
    return efficiency_ratio

# Simulate system performance metrics
def process_performance(metrics, bonus_multiplier):
    base_score = 0
    penalty_adjustment = 0
    
    # Irrelevant preprocessing: case conversion on string labels
    labels = ["Task_{}".format(i) for i in range(len(metrics))]
    upper_labels = [label.upper() for label in labels]
    flipped_labels = [label.replace('A', 'X') for label in upper_labels]  # Distractor

    # Core logic with conditional expressions and arithmetic
    for i, val in enumerate(metrics):
        if val > 75:
            base_score += val * 1.2
        elif val > 50:
            base_score += val * 1.1
        else:
            penalty_adjustment += 5

    # Additional irrelevant computation: unused statistical moment
    mean_metric = sum(metrics) / len(metrics)
    variance_proxy = sum((x - mean_metric) ** 2 for x in metrics) / len(metrics)
    skew_attempt = sum(((x - mean_metric) / (variance_proxy + 1e-5)) ** 3 for x in metrics)  # Dead code

    # Bonus logic with logical operations and multiplier interaction
    exceeds_threshold = any(m > 90 for m in metrics)
    all_above_minimum = all(m > 40 for m in metrics)
    performance_flag = exceeds_threshold and all_above_minimum or bonus_multiplier > 1.3

    # Final score calculation – key step
    final_score = base_score - penalty_adjustment
    if performance_flag:
        final_score *= bonus_multiplier

    # More distraction: itertools-like simulation (no actual import needed)
    expanded_metrics = []
    for m in metrics:
        expanded_metrics.extend([m] * 1)  # No-op expansion
    
    # Redundant normalization pass
    normalized = [round(x / sum(expanded_metrics) * 100, 2) for x in expanded_metrics]
    total_normalized = sum(normalized)

    return int(final_score)

# Input data
metrics_data = [88, 92, 76, 81, 67]
bonus_rate = 1.15

# Unused helper function – dead code path
def debug_state():
    return {"status": "inactive", "mode": "debug_off"}

# Execute main logic
final_score = process_performance(metrics_data, bonus_rate)
print(f"Result: {final_score}")