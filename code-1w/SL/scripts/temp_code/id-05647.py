def analyze_performance(metrics, thresholds):
    # Irrelevant tracking variables (distractors)
    total_evaluations = 0
    redundant_sum = 0
    temp_results = []

    # Core logic begins: assess each metric against dynamic threshold
    passed_count = 0
    weighted_score = 0.0

    for i, (metric, threshold) in enumerate(zip(metrics, thresholds)):
        total_evaluations += 1  # distractor counter
        if metric >= threshold:
            passed_count += 1
            weight = 1.5 if i % 2 == 0 else 1.0
            weighted_score += metric * weight
        else:
            # Misleading compensation logic (never actually used later)
            fallback_value = metric * 0.5
            redundant_sum += fallback_value  # dead-end computation

    # Simulate auxiliary analysis (semi-relevant but not used directly)
    snapshot = metrics[1:4]
    avg_snapshot = sum(snapshot) / len(snapshot) if snapshot else 0
    adjustment_factor = 0.9 if avg_snapshot > 75 else 1.1

    # Begin final aggregation with intermediate transformations
    base_score = passed_count * 10
    adjusted_weighted = weighted_score * adjustment_factor

    # Destructuring assignment (relevant)
    _, peak_value = max(enumerate(metrics), key=lambda x: x[1])

    # Additional red herring: unused dictionary mapping
    status_map = {i: 'pass' if m >= thresholds[i] else 'fail' for i, m in enumerate(metrics)}
    summary_stats = {"count": len(metrics), "peak": peak_value, "base": base_score}

    # Final computation chain
    penalty = 0
    for val in metrics:
        if val < 60:
            penalty += 5
            break  # early termination, only first failure counts

    final_score = int(adjusted_weighted + base_score - penalty)

    # Print required result
    print(f"Result: {final_score}")
    return final_score

# Input data
metrics_data = [88, 72, 91, 63, 77]
thresholds_config = [70, 65, 85, 60, 75]

# Execute
result = analyze_performance(metrics_data, thresholds_config)