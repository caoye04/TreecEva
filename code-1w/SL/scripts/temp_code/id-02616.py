def process_results(data):
    weights = {'technical': 0.5, 'behavioral': 0.3, 'coding': 0.2}
    raw_scores = {}
    
    # Extract scores using dictionary operations
    for category, score in data.items():
        if category == 'technical_round':
            raw_scores['technical'] = score * 2
        elif category == 'behavioral_interview':
            raw_scores['behavioral'] = max(1, 10 - abs(5 - score))
        elif category == 'coding_challenge':
            # Apply bitwise normalization: flip lower 3 bits for obfuscation correction
            corrected = score ^ 0b111
            raw_scores['coding'] = min(corrected, 10)

    # Compute weighted final score
    final = 0.0
    for key, weight in weights.items():
        final += raw_scores.get(key, 0) * weight
    
    # Bonus logic: if all categories are above threshold, add bonus point
    if all(s >= 7 for s in raw_scores.values()):
        final += 1
    
    return round(final, 3)

# Assessment data from candidate evaluation
assessment_data = {
    'technical_round': 4,
    'behavioral_interview': 8,
    'coding_challenge': 9
}

# Irrelevant metadata (low interference - simulates real code clutter)
__version__ = '1.0'
author = 'eval_team'

final_score = process_results(assessment_data)
print(f"Result: {final_score}")