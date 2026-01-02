def evaluate_performance(feedback, metrics):
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []

    # Irrelevant tracking variables (distractors)
    debug_log = []
    iteration_count = 0

    for entry in metrics:
        if entry == 'accuracy':
            base_score += 15
        elif entry == 'latency':
            base_score += 10
            penalty_adjustment -= 3
        elif entry == 'throughput':
            bonus_tracker.append(7)

    # Dead code path - never executed due to fixed input
    if len(metrics) > 100:
        base_score *= 0.5  # hypothetical scaling (unused)

    # Conditional expression with logical operations
    stability = (len(feedback) >= 3) and ('stable' in feedback)
    critical_flag = not (base_score > 40 and penalty_adjustment >= -5)

    # Set operations: core relevant logic
    expected_signals = {'accurate', 'responsive', 'consistent'}
    feedback_set = set(feedback)
    matched_signals = expected_signals & feedback_set  # intersection

    # Additional scoring based on signal match
    for _ in matched_signals:
        base_score += 5

    # Redundant but plausible computation
    avg_bonus = sum(bonus_tracker) / len(bonus_tracker) if bonus_tracker else 0
    temp_normalization = round(avg_bonus * 0.1, 2)

    # Final decision logic with short-circuit evaluation
    if stability or (critical_flag and len(matched_signals) == 0):
        final_score = base_score - abs(penalty_adjustment)
    else:
        final_score = base_score + len(matched_signals)

    return final_score

# Main execution
input_feedback = ['accurate', 'responsive', 'redundant_signal']
target_metrics = ['accuracy', 'latency', 'throughput']

# Irrelevant pre-computations
placeholder_data = [i * 2 for i in range(5)]
metadata_cache = {k: v for k, v in enumerate(['init', 'load', 'verify'])}

final_score = evaluate_performance(input_feedback, target_metrics)
print(f"Result: {final_score}")