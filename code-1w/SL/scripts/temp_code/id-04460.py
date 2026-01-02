def evaluate_performance(feedback, threshold):
    base_score = 0
    bonus = 0
    penalty = 0
    temp_result = 0

    # Irrelevant string processing (distractor)
    feedback_text = ''.join(feedback).lower()
    word_count = len(feedback_text.split())
    char_count = len(feedback_text.replace(' ', ''))

    # Semi-relevant data transformation
    scores = []
    for entry in feedback:
        if 'excellent' in entry:
            scores.append(90)
        elif 'good' in entry:
            scores.append(70)
        elif 'poor' in entry:
            scores.append(40)
        else:
            scores.append(60)

    # Actual logic begins
    average_rating = sum(scores) / len(scores) if scores else 0

    # Conditional expression with red herring variables
    adjustment = 10 if average_rating >= threshold else -5
    
    # Dead code path (misleading)
    if word_count > 1000:
        temp_result = char_count * 0.01

    # Core logic with state tracking
    for s in scores:
        if s >= 85:
            bonus += 3
        elif s < 50:
            penalty += 2

    base_score = average_rating + adjustment
    final_score = base_score + bonus - penalty

    # Unused computation (interference)
    normalized = round(final_score / 100.0, 4)
    summary_stats = {
        'count': len(scores),
        'high': max(scores),
        'low': min(scores),
        'normalized_metric': normalized
    }

    return int(final_score)

# Input data
feedback_list = [
    "Work was excellent and outstanding",
    "Good effort shown",
    "Performance was poor this time",
    "Excellent results overall",
    "Satisfactory progress"
]

# Key execution point
final_score = evaluate_performance(feedback_list, 75)
print(f"Result: {final_score}")