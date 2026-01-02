def process_feedback(reviews, weights):
    total = 0
    bonus = 0
    penalty = 0
    adjustment_factor = 1.0
    
    # Irrelevant preprocessing: count uppercase letters in feedback (distractor)
    uppercase_count = sum(1 for review in reviews for c in review if c.isupper())
    
    # Actual logic begins
    sentiment_scores = []
    for review in reviews:
        clean_review = review.strip().lower()
        if 'excellent' in clean_review or 'great' in clean_review:
            sentiment_scores.append(5)
        elif 'good' in clean_review or 'satisfactory' in clean_review:
            sentiment_scores.append(4)
        elif 'average' in clean_review or 'okay' in clean_review:
            sentiment_scores.append(3)
        elif 'poor' in clean_review or 'bad' in clean_review:
            sentiment_scores.append(2)
        else:
            sentiment_scores.append(1)
    
    # Secondary distraction: simulate response time analysis (unused)
    response_lengths = [len(review.split()) for review in reviews]
    avg_length = sum(response_lengths) / len(response_lengths) if response_lengths else 0
    
    # Apply weights and compute weighted score
    weighted_sum = 0
    for i in range(len(sentiment_scores)):
        weighted_sum += sentiment_scores[i] * weights[i]
    
    # Bonus logic based on pattern (never triggered due to data, but looks relevant)
    if 'excellent' in reviews[0].lower() and weights[0] > 0.8:
        bonus = 10
    elif avg_length > 10:
        bonus = 5

    # Core computation
    base_score = weighted_sum * 10
    final_score = base_score + bonus - penalty

    # Red herring: adjust for case density (computationally irrelevant)
    case_ratio = uppercase_count / (sum(len(r) for r in reviews) + 1)
    if case_ratio > 0.1:
        adjustment_factor = 0.95

    final_score = int(final_score * adjustment_factor)  # Final assignment

    return final_score

# Input data
detailed_reviews = [
    "This was an EXCELLENT experience overall!",
    "Good service, though a bit slow.",
    "Average quality for the price.",
    "Poor attention to detail, very disappointing."
]

weights_config = [0.4, 0.3, 0.2, 0.1]

# Execution
final_score = process_feedback(detailed_reviews, weights_config)
print(f"Result: {final_score}")