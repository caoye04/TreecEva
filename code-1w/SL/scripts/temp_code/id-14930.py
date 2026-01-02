def evaluate_performance(skills, challenges):
    base_multiplier = 1.5
    penalty_factor = 0.9
    temp_result = 0
    final_score = 0
    
    # Irrelevant string processing (distractor)
    skill_names = ['debugging', 'optimization', 'design', 'testing']
    formatted_names = [name.title() + '_V1' for name in skill_names if len(name) > 6]
    unused_mapping = {i: name.upper() for i, name in enumerate(skill_names)}

    # Real computation begins
    adjusted_scores = []
    for i in range(len(skills)):
        raw_score = skills[i] * challenges[i]
        if raw_score > 25:
            raw_score -= (raw_score % 4)  # Adjustment step
        adjusted_scores.append(raw_score)
    
    # Summation with conditional logic
    total_adjusted = sum(adjusted_scores)
    if total_adjusted > 100:
        total_adjusted = total_adjusted // 2
    
    # Modular arithmetic and accumulation
    for val in adjusted_scores:
        temp_result += (val % 7) * 2
    
    # Core formula
    final_score = int((total_adjusted * base_multiplier) - temp_result)
    
    # Dead code path (distractor)
    extra_bonus = 0
    for j in range(5):
        if j > 10:  # Never executes
            extra_bonus += j * 2
    
    return final_score

# Input data
skill_levels = [6, 7, 5, 8]
challenge_ratings = [4, 5, 6, 4]

# Execution point
final_score = evaluate_performance(skill_levels, challenge_ratings)
print(f"Result: {final_score}")