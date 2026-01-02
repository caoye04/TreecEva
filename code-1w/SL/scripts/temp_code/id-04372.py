def evaluate_performance(feedbacks, benchmarks):
    # Core logic variables
    base_rating = 50
    adjustment = 0
    compliance_count = 0

    # Irrelevant tracking (distractor)
    max_feedback_length = 0
    total_chars = 0

    # Process each feedback against benchmark levels
    for fb in feedbacks:
        # Linear search through benchmark criteria
        matched_level = None
        for level, criteria in benchmarks.items():
            if len(fb) >= criteria['min_length'] and fb.startswith(criteria['prefix']):
                matched_level = level
                break  # First match wins (short-circuit)

        # Only 'critical' and 'high' levels contribute to compliance
        if matched_level in ['critical', 'high']:
            compliance_count += 1

        # Character analysis (semi-relevant distractor)
        if len(fb) > max_feedback_length:
            max_feedback_length = len(fb)
        total_chars += len(fb)

    # Real adjustment logic
    if compliance_count >= 2:
        adjustment = 15
    elif compliance_count == 1:
        adjustment = 5
    else:
        adjustment = -10

    # Secondary adjustment based on set uniqueness (core)
    unique_first_chars = len(set([fb[0] for fb in feedbacks if len(fb) > 0]))
    if unique_first_chars >= 3:
        adjustment += 7

    # Irrelevant post-processing (dead path)
    normalized_chars = total_chars / len(feedbacks) if feedbacks else 0
    size_category = 'large' if normalized_chars > 20 else 'small'

    # Final score computation
    final_score = base_rating + adjustment

    # Spurious modification (misleading but not affecting final_score)
    temp_score = final_score * 0.9
    temp_score = round(temp_score)

    return final_score

# Input data
feedback_set = [
    "Critical issue found in module A",
    "High priority update required",
    "Minor tweak suggested",
    "Question about documentation"
]

benchmark_levels = {
    'critical': {'min_length': 25, 'prefix': 'Critical'},
    'high': {'min_length': 10, 'prefix': 'High'},
    'medium': {'min_length': 5, 'prefix': 'M'},
    'low': {'min_length': 3, 'prefix': 'L'}
}

# Execution
final_score = evaluate_performance(feedback_set, benchmark_levels)
print(f"Result: {final_score}")