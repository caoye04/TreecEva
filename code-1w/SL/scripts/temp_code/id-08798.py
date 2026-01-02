def evaluate_performance(feedback, skills):
    base_score = 0
    penalty_adjustment = 0.0
    bonus_tracker = []

    # Irrelevant aggregation (distractor)
    total_entries = sum(len(entries) for entries in feedback.values())
    avg_per_category = total_entries / len(feedback) if feedback else 0

    # Misleading statistical computation
    outlier_threshold = 3
    high_feedback_count = sum(1 for entries in feedback.values() for v in entries if v > outlier_threshold)

    # Core logic begins
    skill_weights = {'debugging': 3, 'design': 2, 'testing': 4, 'documentation': 1}
    weight_sum = sum(skill_weights[skill] for skill in skills)

    raw_contribution = 0
    for skill in skills:
        if skill in feedback:
            # Compute weighted average for each required skill
            skill_values = feedback[skill]
            valid_scores = [v for v in skill_values if 1 <= v <= 5]
            if valid_scores:
                avg_score = sum(valid_scores) / len(valid_scores)
                raw_contribution += avg_score * skill_weights[skill]
    
    # Normalize by total weight
    normalized_score = raw_contribution / weight_sum if weight_sum else 0

    # Conditional bonus based on set uniqueness (semi-relevant)
    unique_scores = len(set(v for entries in feedback.values() for v in entries))
    if unique_scores >= 4:
        bonus_tracker.append(2.5)

    # Red herring: unused function call structure
    def calculate_consistency(data):
        return all(len(vals) >= 2 for vals in data.values())
    
    is_consistent = calculate_consistency(feedback)  # Not used in final score

    # Final adjustment using conditional expression
    final_score = int(normalized_score * 10) + (bonus_tracker[0] if bonus_tracker else 0)

    # Dead code path (never executed under current logic)
    if penalty_adjustment > 10:
        final_score -= 5

    return final_score

# Data setup
feedback_map = {
    'debugging': [4, 5, 4],
    'design': [3, 3],
    'testing': [5, 4, 5, 4],
    'documentation': [2, 3]
}
target_skills = ['debugging', 'testing', 'design']

intermediate_total = sum(sum(vals) for vals in feedback_map.values())  # Distractor

final_score = evaluate_performance(feedback_map, target_skills)
print(f"Result: {final_score}")