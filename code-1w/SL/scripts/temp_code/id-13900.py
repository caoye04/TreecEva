def calculate_total(feedback, multipliers):
    base_scores = {k: len(v) for k, v in feedback.items()}
    bonus = sum(1 for text in feedback['positive'] if 'excellent' in text.lower())
    penalty = sum(1 for text in feedback['negative'] if 'critical' in text.lower())
    weighted_sum = sum(base_scores[key] * multipliers[key] for key in multipliers)
    return weighted_sum + bonus - penalty

reviews = {
    'positive': [
        'Great performance',
        'Excellent work on the project',
        'Outstanding contribution'
    ],
    'negative': [
        'Minor issues found',
        'Critical bug in deployment'
    ]
}

weights = {'positive': 2, 'negative': -1}
irrelevant_counter = len([c for c in reviews['positive'][0] if c in 'aeiou'])
final_score = calculate_total(reviews, weights)
print(f"Result: {final_score}")