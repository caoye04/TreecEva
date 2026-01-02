def evaluate_performance(feedback, thresh):
    # Irrelevant preprocessing: count adjectives (distractor)
    sentiment_words = ['excellent', 'good', 'poor', 'outstanding', 'average']
    adjective_count = sum(1 for word in sentiment_words if any(word in f.lower() for f in feedback))

    # Relevant logic begins: extract numeric ratings from feedback strings
    raw_ratings = []
    for entry in feedback:
        parts = entry.split(':')
        if len(parts) == 2:
            try:
                rating = float(parts[1].strip())
                raw_ratings.append(rating)
            except ValueError:
                continue

    # Distractor: unused transformation
    normalized = [round((r - min(raw_ratings)) / (max(raw_ratings) - min(raw_ratings)) * 100) for r in raw_ratings if len(raw_ratings) > 1]

    # Semi-relevant: filter based on threshold
    passing = [r for r in raw_ratings if r >= thresh]

    # Compute stability metric (irrelevant to final result but adds cognitive load)
    volatility = 0.0
    for i in range(1, len(raw_ratings)):
        volatility += abs(raw_ratings[i] - raw_ratings[i-1])

    # Key computation: final score is average of passing ratings multiplied by count bonus
    if passing:
        base_avg = sum(passing) / len(passing)
        bonus = len(passing)  # incentive for more passing reviews
        final_score = base_avg * bonus
    else:
        final_score = 0

    return final_score


# Input data
feedback_list = [
    'Review1: 4.5',
    'Review2: 3.2',
    'Review3: 7.8',
    'Review4: invalid',
    'Review5: 8.1',
    'Review6: 6.9'
]
threshold = 6.0

# Execution point
final_score = evaluate_performance(feedback_list, threshold)

print(f"Result: {final_score}")