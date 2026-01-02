from collections import defaultdict

def calculate_final_score(assessments):
    scores = defaultdict(int)
    weights = {'quiz': 0.1, 'homework': 0.2, 'exam': 0.7}
    
    for category, grade in assessments:
        scores[category] += grade
    
    weighted_total = 0.0
    total_weight = 0.0
    
    for cat in ['quiz', 'homework', 'exam']:
        if scores[cat] > 0:
            weighted_total += scores[cat] * weights[cat]
            total_weight += weights[cat]
    
    # Normalize by total applied weight
    normalized_score = weighted_total / total_weight if total_weight else 0
    
    bonus = 5 if normalized_score >= 85 else 0
    final_score = int(normalized_score + bonus)
    
    temp_debug = [1 for _ in range(5)]  # Irrelevant debug artifact
    unused_counter = len(temp_debug)
    
    return final_score

assessments_data = [
    ('quiz', 80),
    ('quiz', 90),
    ('homework', 75),
    ('homework', 85),
    ('exam', 88)
]

final_score = calculate_final_score(assessments_data)
print(f"Result: {final_score}")