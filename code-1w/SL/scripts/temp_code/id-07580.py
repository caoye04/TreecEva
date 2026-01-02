def analyze_training_cycle():
    base_metrics = [3, 7, 12, 18, 25]
    adjustment_factor = 1.2
    temp_offsets = [x * 0.1 for x in base_metrics]
    
    # Simulate multi-phase training feedback
    feedback_levels = []
    cumulative_shift = 0
    
    for i in range(len(base_metrics)):
        raw_value = base_metrics[i] + temp_offsets[i]
        if i % 2 == 0:
            adjusted = raw_value * adjustment_factor
        else:
            adjusted = raw_value * (adjustment_factor - 0.2)
        
        # Irrelevant smoothing
        smoothed = (adjusted + cumulative_shift) / (1 + i * 0.05)
        cumulative_shift += adjusted * 0.1
        
        feedback_levels.append(adjusted)

    # Dead code: unused transformation
    inverted_map = {i: round(1/v, 3) for i, v in enumerate(feedback_levels) if v > 0}
    ignored_summary = sum([v**0.5 for v in feedback_levels if v < 20])

    normalization_constant = 0.85
    benchmark_weight = sum(feedback_levels) * normalization_constant

    # Real computation path
    weight_correction = 0
    for val in feedback_levels:
        if val > 15:
            weight_correction += val * 0.05
    
    benchmark_weight -= weight_correction

    final_score = evaluate_performance(feedback_levels, benchmark_weight)
    return final_score


def evaluate_performance(reports, weight):
    peak = max(reports)
    length = len(reports)
    avg = sum(reports) / length
    
    # Distractor: complex but unused formula
    theoretical_max = peak * length * 0.9
    efficiency_ratio = (sum(reports) / theoretical_max) if theoretical_max != 0 else 0
    
    # Actual logic
    if avg > 10:
        performance_bonus = 5
    else:
        performance_bonus = 1
    
    result = int(weight + performance_bonus)  # Final score is integer
    
    # Red herring computation
    secondary_metric = (peak + avg) * 0.5
    _ = round(secondary_metric, 2)
    
    return result

# Execute and print result
final_score = analyze_training_cycle()
print(f"Result: {final_score}")