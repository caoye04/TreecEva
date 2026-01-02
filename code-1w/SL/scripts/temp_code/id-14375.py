def evaluate_performance(feedback_set, benchmark_data):
    base_rating = 75
    adjustment_factor = 0.8
    penalty_rate = 0.1
    
    # Irrelevant metrics (distractor variables)
    avg_response_time = 230
    user_satisfaction_index = 4.2
    deprecated_flag = True
    temp_log = []
    
    for entry in benchmark_data:
        if entry['version'] < 2.0:
            base_rating -= 5
        else:
            base_rating += 3

    # Set operations and list comprehensions (relevant)
    valid_feedback = {f['issue'] for f in feedback_set if f['severity'] > 1}
    critical_issues = {"timeout", "crash", "data_loss"}
    
    # Distractor: unused but plausible computation
    potential_risks = [item for item in valid_feedback if item not in critical_issues]
    mitigation_effort = len(potential_risks) * 1.5

    # Real impact: intersection determines penalty
    active_criticals = valid_feedback & critical_issues
    
    if len(active_criticals) > 0:
        base_rating -= len(active_criticals) * 10

    # Conditional expression with distractor variable
    stability_bonus = 10 if user_satisfaction_index > 4.0 else 5  # uses misleading variable

    # Final score calculation (only some inputs matter)
    final_score = base_rating * adjustment_factor - len(active_criticals) * penalty_rate + stability_bonus

    # Dead code path (distractor)
    if deprecated_flag:
        temp_log.append("Legacy mode detected")

    return int(final_score)

# Input data
feedback_entries = [
    {'issue': 'timeout', 'severity': 3},
    {'issue': 'ui_jank', 'severity': 2},
    {'issue': 'crash', 'severity': 4},
    {'issue': 'slow_load', 'severity': 1}
]

benchmarks = [
    {'version': 1.8, 'score': 88},
    {'version': 2.1, 'score': 92}
]

# Execution point
final_score = evaluate_performance(feedback_entries, benchmarks)
print(f"Result: {final_score}")