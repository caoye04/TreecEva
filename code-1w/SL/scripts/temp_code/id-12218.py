def evaluate_performance(skills, difficulty):
    base_score = 0
    penalty = 0
    bonus = 0
    temp_result = 0

    # Irrelevant string processing (distractor)
    skill_names = ['debugging', 'optimization', 'architecture', 'testing']
    formatted_skills = [name.upper().replace('I', '1') for name in skill_names]
    debug_info = ''.join(formatted_skills)[:10]  # Not used later

    # Real logic begins
    for level in skills:
        if level >= difficulty:
            base_score += level * 1.5
        else:
            penalty += (difficulty - level) * 0.5

    # Extra nested structure with semi-relevant computation
    if base_score > 50:
        adjustment_factor = 1.2
        for i in range(2):
            temp_result += base_score * (adjustment_factor - i * 0.1)
        bonus = (temp_result / 2) * 0.1
    else:
        bonus = 10

    # More distractions: unused intermediate calculations
    avg_skill = sum(skills) / len(skills)
    skill_variance = sum((x - avg_skill) ** 2 for x in skills) / len(skills)
    theoretical_max = len(skills) * difficulty * 2  # Unused metric

    # Final score calculation
    final_score = base_score - penalty + bonus

    # Additional red herring: string-based conditional that doesn't affect output
    status_flag = 'HIGH' if final_score > 60 else 'LOW'
    log_entry = f'Status: {status_flag} | Score: {final_score:.2f}'.strip()

    return int(final_score)


# Main execution
skill_levels = [8, 12, 9, 14]
challenge_difficulty = 10

# Initialization of irrelevant tracking variables
attempt_counter = 0
session_token = 'ABC123XYZ'.lower().replace('1', 'A')  # Dead code path

final_score = evaluate_performance(skill_levels, challenge_difficulty)
print(f'Result: {final_score}')