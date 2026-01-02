def evaluate_performance(feedback):
    base_rating = 75
    adjustment = 0
    peak_moment = False
    temp_buffer = 0

    for i, fb in enumerate(feedback):
        if fb == 'success':
            adjustment += (i + 1) * 1.5
            if i % 3 == 0:
                temp_buffer += 2.5  # Irrelevant accumulation
        elif fb == 'warning':
            adjustment -= 5
        else:  # 'failure'
            adjustment -= 8
            if i > 0 and feedback[i-1] == 'success':
                peak_moment = True

    # Distractor logic: unrelated metrics
    compliance_check = all(f != 'failure' for f in feedback)
    bonus_eligible = len([f for f in feedback if f == 'success']) > 2
    dummy_metric = sum(1 for x in feedback if x == 'warning') * 3.3

    # Conditional expression used
    final_score = base_rating + adjustment + (10 if peak_moment and bonus_eligible else 0)
    
    # Dead code path - never executed due to logic
    if len(feedback) == 0:
        final_score = 0

    return int(final_score)

# Simulated feedback log from system audit
feedback_sequence = ['success', 'success', 'warning', 'success', 'failure']

# Key computation point
final_score = evaluate_performance(feedback_sequence)

print(f"Target result: {final_score}")