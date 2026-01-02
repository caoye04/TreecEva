def process_feedback(reviews, weights):
    total_points = 0
    adjustment_factor = 0.85
    temp_sum = 0
    feedback_count = len(reviews)
    weight_sum = sum(weights.values())
    scaling_factor = feedback_count / (weight_sum + 1) if weight_sum != -1 else 1.0

    # Irrelevant preprocessing: counting adjectives (not used in final logic)
    adjective_count = 0
    for review in reviews:
        words = review['text'].split()
        for word in words:
            if word.endswith('ing') or word.endswith('ed'):
                adjective_count += 1  # Distractor: not used later

    # Actual scoring logic
    category_tally = {'service': [], 'food': [], 'ambiance': []}
    for review in reviews:
        rating = review['rating']
        categories = review['categories']
        for cat in categories:
            if cat in category_tally:
                category_tally[cat].append(rating)

    avg_service = sum(category_tally['service']) / len(category_tally['service']) if category_tally['service'] else 0
    avg_food = sum(category_tally['food']) / len(category_tally['food']) if category_tally['food'] else 0
    avg_ambiance = sum(category_tally['ambiance']) / len(category_tally['ambiance']) if category_tally['ambiance'] else 0

    # Misleading intermediate calculation
    outlier_count = 0
    for review in reviews:
        if review['rating'] < 2:
            outlier_count += 1
    suppression_factor = 1 - (outlier_count * 0.05)  # Looks important but unused

    # Weighted aggregation using weights dictionary
    weighted_total = 0
    for key in weights:
        if key == 'service':
            weighted_total += avg_service * weights[key]
        elif key == 'food':
            weighted_total += avg_food * weights[key]
        elif key == 'ambiance':
            weighted_total += avg_ambiance * weights[key]

    # Final score with dummy offset
    offset = len(reviews[0]['text'].replace(' ', '')) % 5  # Minor obfuscation
    final_score = (weighted_total + offset) * adjustment_factor

    return int(final_score)

# Input data
reviews = [
    {'text': 'Excellent food and great service', 'rating': 5, 'categories': ['service', 'food']},
    {'text': 'Poor ambiance but decent food', 'rating': 3, 'categories': ['ambiance', 'food']},
    {'text': 'Outstanding service and ambiance', 'rating': 5, 'categories': ['service', 'ambiance']},
    {'text': 'Average food, nothing special', 'rating': 2, 'categories': ['food']}
]

weights = {
    'service': 0.4,
    'food': 0.35,
    'ambiance': 0.25
}

final_score = process_feedback(reviews, weights)
print(f"Result: {final_score}")