def calculate_performance_rating():
    base_points = 85
    bonus_multiplier = 1.2
    penalty_factor = 0.9

    # Simulate various performance metrics
    attendance_rate = 0.97
    project_count = 5
    peer_review_avg = 4.6
    leadership_roles = 2

    # Distractor: Irrelevant calculation for team diversity index
    team_size = 12
    gender_diversity_index = 0.82
    tenure_variance = 3.4
    diversity_score = team_size * gender_diversity_index / (tenure_variance + 1)

    # Real logic begins: calculate raw performance score
    raw_score = base_points
    if project_count >= 3:
        raw_score += 10
    if peer_review_avg >= 4.5:
        raw_score += 5

    # Conditional expression for leadership bonus
    leadership_bonus = 8 if leadership_roles >= 2 else 3

    # Accumulate score with bonus and penalties
    adjusted_score = raw_score + leadership_bonus
    adjusted_score *= bonus_multiplier

    # Apply attendance-based penalty if needed
    if attendance_rate < 0.95:
        adjusted_score *= penalty_factor

    # More distractors: unused efficiency metrics
    lines_of_code = 12740
    code_review_count = 23
    avg_response_time = 4.1  # hours
    efficiency_ratio = lines_of_code / (code_review_count * avg_response_time + 1)

    # Final performance rating
    final_score = int(adjusted_score)

    return final_score

# Execute and print result
target_result = calculate_performance_rating()
print(f"Result: {target_result}")