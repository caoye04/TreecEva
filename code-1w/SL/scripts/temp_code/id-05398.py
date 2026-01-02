def evaluate_performance(weights, results):
    # Normalize results using min-max scaling (irrelevant for final score but adds distraction)
    min_val, max_val = min(results), max(results)
    normalized = [(r - min_val) / (max_val - min_val + 1e-8) for r in results]

    # Apply weight masking based on performance thresholds (distractor logic)
    mask = [1 if r >= sum(results) / len(results) else 0.5 for r in results]
    masked_weights = [w * m for w, m in zip(weights, mask)]
    total_weight = sum(masked_weights)

    # Core logic: weighted harmonic mean of top 3 results (key computation)
    sorted_results = sorted([r for r in results], reverse=True)[:3]  # slicing top 3

    # Harmonic mean with weights applied only to top 3
    weighted_inv_sum = 0.0
    weight_slice = weights[:3]
    for i, val in enumerate(sorted_results):
        if val != 0:
            weighted_inv_sum += weight_slice[i] / val
    
    # Dead code: entropy calculation (not used in output)
    from math import log
    entropy = 0
    for p in [w/sum(weights) for w in weights]:
        if p > 0:
            entropy -= p * log(p, 2)

    # Auxiliary metric: outlier detection (unused)
    avg = sum(results) / len(results)
    variance = sum((x - avg) ** 2 for x in results) / len(results)
    std_dev = variance ** 0.5
    outliers = [x for x in results if abs(x - avg) > 2 * std_dev]

    # Final score: inverse of weighted inverse sum (harmonic style)
    if weighted_inv_sum == 0:
        return 0
    final_harmonic = 3 / weighted_inv_sum  # 3 elements

    # Additional state tracking (semi-relevant)
    performance_band = ""
    if final_harmonic > 80:
        performance_band = "excellent"
    elif final_harmonic > 60:
        performance_band = "good"
    else:
        performance_band = "needs_improvement"

    # Critical result assignment
    final_score = int(round(final_harmonic))

    # Spurious dictionary aggregation (set and dict operations as distractors)
    stat_summary = {
        'count': len(results),
        'top_3_avg': sum(sorted_results) / 3,
        'score_level': performance_band,
        'outlier_count': len(outliers)
    }
    unique_result_set = set(results)
    stat_summary['unique_count'] = len(unique_result_set)

    return final_score

# Main execution
metric_weights = [0.4, 0.3, 0.2, 0.1, 0.05]
raw_results = [75, 88, 92, 64, 77, 95, 83]
final_score = evaluate_performance(metric_weights, raw_results)
print(f"Target result: {final_score}")