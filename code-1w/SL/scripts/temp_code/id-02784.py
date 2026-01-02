def evaluate_performance(feedback, scores):
    adjustment_factor = 0.85
    penalty_threshold = 75
    bonus_applied = False
    total_adjustment = 0
    temp_result = 0

    # Irrelevant pre-processing (distractor)
    normalized = {k: v / max(scores.values()) for k, v in scores.items()}
    cumulative = 0
    for val in normalized.values():
        cumulative += val * 0.1  # Noise computation

    # Core logic begins
    final_score = 0
    for student, base in scores.items():
        feedback_level = feedback.get(student, 'neutral')
        
        if base < penalty_threshold:
            if feedback_level == 'positive':
                base *= adjustment_factor + 0.1
            elif feedback_level == 'negative':
                base *= adjustment_factor - 0.2
            else:
                base *= adjustment_factor
        else:
            if feedback_level == 'positive':
                bonus_applied = True
                base += 5
            elif feedback_level == 'critical':
                base -= 10

        final_score += base

    # Redundant post-processing (distractor)
    outlier_count = 0
    for s in scores.values():
        if s > 90:
            outlier_count += 1
    scaling_buffer = outlier_count * 0.5  # Unused but plausible

    # Final adjustment unrelated to loop
    if bonus_applied:
        final_score -= 3  # Small correction

    return int(final_score)

# Data setup
base_scores = {
    'alice': 88,
    'bob': 70,
    'charlie': 92,
    'diana': 65
}

feedback_map = {
    'alice': 'positive',
    'bob': 'negative',
    'charlie': 'critical',
    'diana': 'neutral'
}

# Key execution point
final_score = evaluate_performance(feedback_map, base_scores)
print(f"Result: {final_score}")