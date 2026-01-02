def evaluate_performance(feedback):
    base_score = 0
    bonus_multiplier = 1.0
    penalty_count = 0
    temp_result = 0
    intermediate_values = []

    # Irrelevant preprocessing: counting characters in keys
    key_length_sum = sum(len(key) for key in feedback.keys())
    if key_length_sum > 20:
        temp_result += 5  # Distractor logic

    # Actual scoring logic
    for category, details in feedback.items():
        raw_value = details['rating'] * details['weight']
        if details['rating'] < 3:
            penalty_count += 1
        intermediate_values.append(raw_value)

    # More distractions: unused statistical computation
    if intermediate_values:
        avg_intermediate = sum(intermediate_values) / len(intermediate_values)
        std_dev_guess = (max(intermediate_values) - min(intermediate_values)) / 2

    # Real impact: bonuses for high consistency
    ratings = [d['rating'] for d in feedback.values()]
    if all(r >= 4 for r in ratings):
        bonus_multiplier = 1.5

    # Base score calculation
    for val in intermediate_values:
        base_score += val * 10

    # Fake normalization path (not taken)
    normalized_base = base_score / 100.0
    if normalized_base > 10:
        normalized_base = 10  # Dead code effect

    # Final computation
    final_score = int(base_score * bonus_multiplier)

    # Extra red herring: modifying a variable not used later
    final_score_temp = final_score + penalty_count * 2
    final_score_temp = abs(final_score_temp - temp_result)

    return final_score

# Setup input data
detailed_feedback = {
    'design': {'rating': 4, 'weight': 0.3},
    'usability': {'rating': 5, 'weight': 0.4},
    'performance': {'rating': 4, 'weight': 0.3},
    'documentation': {'rating': 2, 'weight': 0.2}  # Triggers penalty
}

# Execution leading to final_score
total_penalties = sum(1 for v in detailed_feedback.values() if v['rating'] < 3)
placeholder_sum = sum(v['rating'] for v in detailed_feedback.values())

final_score = evaluate_performance(detailed_feedback)
print(f"Result: {final_score}")