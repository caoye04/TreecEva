def evaluate_performance(weights, scores, adj):
    base = 0
    bonus = 0
    penalty = 0
    temp_result = [0] * len(scores)
    
    # Irrelevant string processing - distractor
    performance_label = 'excellent' if sum(scores) > 30 else 'average'
    label_upper = performance_label.upper()
    label_len = len(label_upper)
    
    # Misleading normalization (not actually used in final result)
    normalized = [round(s / 10.0, 2) for s in scores]
    pseudo_rank = sorted(normalized, reverse=True)[:3]

    # Real computation begins
    for i in range(len(scores)):
        temp_result[i] = scores[i] * weights[i]
        if scores[i] >= 8 and i % 2 == 0:
            bonus += 1.5
        elif scores[i] < 5:
            penalty += 0.5

    # Red herring: unused helper calculation
    avg_temp = sum(temp_result) / len(temp_result) if temp_result else 0
    threshold_met = [t for t in temp_result if t > 5.0]
    extra_offset = len(threshold_met) * 0.2

    # Actual score accumulation
    base = sum(temp_result)
    adjusted_base = base * adj
    final_component = adjusted_base + bonus - penalty
    
    # Key interference: multiple similar variables
    preliminary_score = final_component * 0.9
    provisional_score = preliminary_score + extra_offset
    final_score = int(round(provisional_score))

    # Dead code path - never executed but looks relevant
    debug_mode = False
    if debug_mode:
        print(f'Debug: {provisional_score=}, {extra_offset=}')

    return final_score

# Input setup
metric_weights = [1.2, 0.8, 1.5, 0.9, 1.1]
raw_scores = [7, 9, 6, 4, 8]
adjustment_factor = 1.05

# Execution
final_score = evaluate_performance(metric_weights, raw_scores, adjustment_factor)
print(f'Result: {final_score}')