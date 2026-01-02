def evaluate_performance(metrics, thresholds):
    # Initialize tracking variables
    passed_count = 0
    total_weight = 0.0
    penalty_offset = 0
    debug_log = []

    # Auxiliary computation - not directly affecting final result
    temp_values = [x ** 0.5 for x in metrics if x > 10]
    auxiliary_sum = sum(temp_values) / (len(temp_values) + 1)

    # Main evaluation loop with enumerate and zip
    for i, (metric, threshold) in enumerate(zip(metrics, thresholds)):
        weight = (i + 1) * 0.5  # Increasing weight per position
        total_weight += weight

        # Boolean logic and comparison operations
        meets_target = metric >= threshold
        is_critical = i in {0, 2, 4}

        # Logical combination with short-circuit behavior
        if is_critical and meets_target:
            passed_count += 1
            debug_log.append(f"Critical metric {i} passed")
        elif not is_critical and meets_target:
            passed_count += 0.5  # Partial credit for non-critical

        # Bitwise red herring: used but doesn't impact final score
        mask_check = i & 3
        if mask_check == 0:
            penalty_offset += 1  # Distractor increment

    # Composite calculation with irrelevant adjustments
    base_score = (passed_count / len(thresholds)) * 100
    adjusted_score = base_score + (auxiliary_sum * 0.1) - (penalty_offset * 0.5)

    # Final nonlinear transformation
    final_score = int(round(adjusted_score ** 1.05))

    # Irrelevant tuple unpacking and dead code path
    summary_stats = (base_score, adjusted_score, final_score)
    s1, s2, s3 = summary_stats
    if s1 < 0:
        return -1  # Dead code - unreachable due to input constraints

    return final_score

# Input data
metrics_data = [85, 70, 90, 60, 80]
threshold_levels = [80, 65, 88, 50, 75]

# Execution point
final_score = evaluate_performance(metrics_data, threshold_levels)
print(f"Result: {final_score}")