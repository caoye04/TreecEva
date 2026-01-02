def evaluate_performance(feedback, rating):
    # Irrelevant mapping for distraction
    sentiment_weights = {
        'positive': 1.2,
        'negative': 0.5,
        'neutral': 0.8,
        'critical': 0.3,
        'excellent': 1.5
    }

    # Distractor counters
    total_entries = len(feedback)
    temp_sum = 0
    adjustment_factor = 0.9

    # Real logic starts: count specific feedback types
    weighted_total = 0
    valid_categories = ['usability', 'performance', 'security']

    for category, details in feedback.items():
        if category not in valid_categories:
            continue  # Skip irrelevant categories

        # Extract sub-score and sentiment
        sub_score = details.get('score', 0)
        sentiment = details.get('sentiment', 'neutral')

        # Real contribution to result
        if sentiment == 'positive' or sentiment == 'excellent':
            weighted_total += sub_score * 1.1
        elif sentiment == 'negative' or sentiment == 'critical':
            weighted_total += sub_score * 0.7
        else:
            weighted_total += sub_score * 0.9

    # Additional distraction: unused loop over keys
    for key in sentiment_weights.keys():
        temp_sum += 1  # Dead computation

    # Combine with base rating using bitwise adjustment (real step)
    # Use XOR to perturb base rating slightly based on number of valid entries
    valid_count = sum(1 for c in feedback.keys() if c in valid_categories)
    perturbation = rating ^ valid_count  # Bitwise operation affecting result

    # Final score calculation
    final_score = (weighted_total / valid_count) if valid_count > 0 else rating
    final_score = (final_score + perturbation) / 2  # Blending with perturbed base

    return int(final_score)  # Ensure integer result


# Main execution
base_rating = 75
feedback_map = {
    'usability': {'score': 80, 'sentiment': 'positive'},
    'performance': {'score': 70, 'sentiment': 'neutral'},
    'security': {'score': 60, 'sentiment': 'critical'},
    'documentation': {'score': 85, 'sentiment': 'excellent'},  # Invalid category
    'maintenance': {'score': 50, 'sentiment': 'negative'}       # Invalid category
}

# Key statement
final_score = evaluate_performance(feedback_map, base_rating)
print(f"Result: {final_score}")