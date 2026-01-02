def evaluate_performance(metrics):
    base_weight = 0.8
    bonus_factor = 1.2
    penalty_threshold = 75
    
    # Irrelevant metrics (distractors)
    unused_metric_a = sum([i**2 for i in range(5)])
    temp_offset = len("performance") * 2
    unused_metric_b = set(range(10, 20))

    # Core logic begins
    valid_metrics = {x for x in metrics if isinstance(x, int) and x >= 0}
    adjusted_metrics = {x + 5 for x in valid_metrics if x < penalty_threshold}
    
    if len(valid_metrics) > len(adjusted_metrics):
        adjustment_count = len(valid_metrics) - len(adjusted_metrics)
        scaling_modifier = 0.95 ** adjustment_count
    else:
        scaling_modifier = 1.0
        fallback_used = True  # Dead variable
    
    raw_average = sum(adjusted_metrics) / len(adjusted_metrics) if adjusted_metrics else 0
    
    # Conditional bonus application
    bonus_applied = False
    if raw_average >= 80:
        raw_average *= bonus_factor
        bonus_applied = True
    
    # Secondary adjustment using base weight
    weighted_score = raw_average * base_weight
    
    # Final aggregation with string-based case conversion (irrelevant but adds cognitive load)
    status_tag = "Pass" if weighted_score >= 60 else "Review"
    status_code = status_tag.lower().upper().capitalize()  # No effect
    
    # Compute final score
    final_score = round(weighted_score, 2)
    
    # Extra unused data structure manipulation
    metric_summary = {
        'count': len(metrics),
        'valid': len(valid_metrics),
        'adjusted': len(adjusted_metrics),
        'score': final_score
    }
    
    return final_score

# Main execution
metric_data = [88, 72, 91, -5, 'N/A', 67, 83]
interim_result = max(metric_data[:3])  # Distractor computation
offset_correction = pow(2, 3) - 8  # Always zero, irrelevant
normalization_step = sum([1 for _ in metric_data if isinstance(_, str)]) * 5  # Unused

final_score = evaluate_performance(metric_data)
print(f"Result: {final_score}")