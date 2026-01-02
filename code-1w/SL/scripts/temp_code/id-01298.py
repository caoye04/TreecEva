def process_feedback(reviews, weights):
    total = 0
    base_adjustment = 0.85
    temp_sum = 0  # distractor variable
    scaling_factor = len(weights) * base_adjustment  # used only in irrelevant path

    # Irrelevant computation block (distractor)
    outlier_count = 0
    for review in reviews:
        if len(review['comment']) > 200:
            outlier_count += 1
    if outlier_count > 2:
        scaling_factor *= 0.9  # dead-end adjustment, not used later

    # Core logic with string and dictionary processing
    weighted_total = 0
    feedback_strength = 0
    for i, entry in enumerate(reviews):
        comment = entry['comment'].strip().lower()
        rating = entry['rating']
        category = entry['category']

        # Dictionary-based weight lookup
        if category in weights:
            weight = weights[category]
        else:
            weight = 1.0

        # String analysis affecting logic
        positivity_boost = 1.0
        if 'excellent' in comment or 'outstanding' in comment:
            positivity_boost = 1.2
        elif 'poor' in comment or 'lacking' in comment:
            positivity_boost = 0.8

        # Bitwise influence (modulating impact using XOR pattern)
        modifier_key = (i + 1) ^ 3
        if modifier_key > 2:
            weight *= 1.1

        contribution = rating * weight * positivity_boost
        weighted_total += contribution

        # Track strength of feedback based on text length
        if len(comment) > 50:
            feedback_strength += 1.5
        else:
            feedback_strength += 0.8

    # Final aggregation
    normalized_strength = feedback_strength / len(reviews)
    final_score = int(weighted_total / len(reviews) * normalized_strength)

    # Unused variables (distractors)
    avg_review_length = sum(len(r['comment']) for r in reviews) / len(reviews)
    temp_sum += avg_review_length * base_adjustment

    return final_score

# Input data
reviews = [
    {'rating': 4, 'comment': 'Good, but lacking detail.', 'category': 'usability'},
    {'rating': 5, 'comment': 'Excellent feature set and outstanding performance!', 'category': 'features'},
    {'rating': 3, 'comment': 'Average experience, nothing special.', 'category': 'usability'},
    {'rating': 5, 'comment': 'Outstanding usability and excellent support!', 'category': 'support'},
    {'rating': 2, 'comment': 'Poor implementation with many bugs.', 'category': 'features'}
]
weights = {'usability': 1.2, 'features': 0.9, 'support': 1.4}

result = process_feedback(reviews, weights)
print(f"Result: {result}")