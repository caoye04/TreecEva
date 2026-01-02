def evaluate_performance(data, importance):
    # Initialize various tracking variables (some are red herrings)
    temp_result = 0
    cumulative = 0
    adjustment_factor = 0.95
    baseline_offset = 10
    debug_trace = []

    # Irrelevant pre-processing step (not used in final logic)
    processed_data = {k: v * adjustment_factor + baseline_offset for k, v in data.items()}

    # Core logic: weighted sum calculation
    weighted_sum = sum(data[key] * importance[key] for key in data)
    total_weight = sum(importance.values())
    normalized_score = weighted_sum / total_weight

    # Distractor: complex conditional that doesn't affect outcome
    if normalized_score > 80:
        grade_level = 'A'
        bonus_multiplier = 1.1
    elif normalized_score > 70:
        grade_level = 'B'
        bonus_multiplier = 1.05
    else:
        grade_level = 'C'
        bonus_multiplier = 1.0  # No bonus

    # Unused helper function (dead code)
    compute_ranking = lambda x: sorted(x.items(), key=lambda item: item[1], reverse=True)

    # Additional irrelevant computation
    outlier_count = 0
    for value in data.values():
        if value < 50 or value > 95:
            outlier_count += 1

    # Final adjustment using string-based threshold check (slicing usage)
    performance_str = "excellent" if normalized_score >= 85 else "good" if normalized_score >= 75 else "acceptable"
    quality_flag = performance_str[:3]  # First three characters

    # Actual final score computation (depends only on normalized_score and fixed rule)
    if quality_flag == "exc":
        final_score = int(normalized_score * 1.2)
    elif quality_flag == "goo":
        final_score = int(normalized_score * 1.1)
    else:
        final_score = int(normalized_score)

    return final_score

# Main execution block
metrics = {'accuracy': 88, 'latency': 76, 'throughput': 82, 'reliability': 79}
weights = {'accuracy': 0.4, 'latency': 0.2, 'throughput': 0.25, 'reliability': 0.15}

# Extra unused data structures (distractors)
backup_metrics = metrics.copy()
deprecated_keys = ['latency', 'throughput']
filtered_metrics = {k: v for k, v in metrics.items() if k not in deprecated_keys}

# Key statement
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Target result: {final_score}")