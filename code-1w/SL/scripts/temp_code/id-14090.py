def evaluate_performance(feedback, skills):
    base_score = 0
    bonus_multiplier = 1.0
    penalty_count = 0

    # Irrelevant tracking variables (distractors)
    session_log = []
    debug_trace = set()
    temp_result_cache = {}

    for skill in skills:
        if skill in feedback:
            rating = feedback[skill]
            base_score += rating * 10

            # Complex but partially irrelevant logic
            if rating >= 4:
                bonus_multiplier *= 1.1
n            elif rating == 3:
                session_log.append(f"Neutral: {skill}")
            else:
                penalty_count += 1
                debug_trace.add(skill)

    # Secondary computation with dead-end path
    adjustment_factor = 0.95
    calibration_offset = sum([v for v in feedback.values()]) * 0.05
    adjusted_score = base_score * adjustment_factor + calibration_offset

    # Misleading normalization step (not actually used)
    max_possible = len(skills) * 10 * bonus_multiplier
    normalized = (adjusted_score / max_possible) * 100 if max_possible > 0 else 0

    # Final scoring uses only adjusted_score and penalty modifier
    final_modifier = 0.8 if penalty_count > 2 else 1.0
    final_score = int(adjusted_score * final_modifier)

    return final_score

# Main execution
required_skills = ['debugging', 'optimization', 'architecture', 'testing', 'security']
feedback_data = {
    'debugging': 5,
    'optimization': 4,
    'architecture': 3,
    'testing': 5,
    'security': 2,
    'documentation': 4  # Irrelevant key (not in required_skills)
}

intermediate_sum = sum(feedback_data.values()) * 2  # Distractor computation
placeholder_list = [x * 0 for x in range(len(required_skills))]  # Dead code path

final_score = evaluate_performance(feedback_data, required_skills)
print(f"Result: {final_score}")