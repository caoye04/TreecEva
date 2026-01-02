from collections import defaultdict
from itertools import zip_longest

def calculate_final_score(results, weights):
    weighted_sum = 0.0
    normalization_factor = 0.0
    
    # Aggregate scores using default dictionary for missing subjects
    subject_scores = defaultdict(float)
    for subject, score in results:
        subject_scores[subject] += score
    
    # Apply bonus weights with alignment using zip_longest
    for (_, score), (weight_key, bonus) in zip_longest(
        sorted(subject_scores.items()), 
        sorted(weights.items()), 
        fillvalue=(None, 0)
    ):
        if weight_key == 'curve':
            score *= (1 + bonus)
        elif weight_key == 'boost':
            score += bonus
        weighted_sum += score * (bonus + 1 if bonus > 0 else 1)
        normalization_factor += 1
    
    final_score = int(weighted_sum / normalization_factor) if normalization_factor > 0 else 0
    return final_score

# Input data
exam_results = [
    ('math', 85),
    ('physics', 78),
    ('math', 12),  # Additional quiz
    ('chemistry', 90)
]

bonus_weights = {
    'boost': 5,
    'curve': 0.1
}

# Execution point of interest
final_score = calculate_final_score(exam_results, bonus_weights)
print(f"Result: {final_score}")