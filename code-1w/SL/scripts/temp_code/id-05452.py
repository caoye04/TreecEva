def calculate_final_score(weights):
    raw_scores = {'math': 85, 'physics': 90, 'chemistry': 78, 'biology': 88}
    adjustments = {'math': 1.05, 'physics': 0.95, 'chemistry': 1.0, 'biology': 1.02}
    weighted_sum = 0.0
    total_weight = 0.0
    
    for subject, base_score in raw_scores.items():
        adjusted = base_score * adjustments[subject]
        weighted = adjusted * weights[subject]
        weighted_sum += weighted
        total_weight += weights[subject]
    
    final_normalized = weighted_sum / total_weight
    bonus = 5 if final_normalized > 85 else 2
    final_score = final_normalized + bonus
    return final_score

exam_weights = {'math': 0.3, 'physics': 0.3, 'chemistry': 0.2, 'biology': 0.2}
final_score = calculate_final_score(exam_weights)
print(f"Result: {final_score}")