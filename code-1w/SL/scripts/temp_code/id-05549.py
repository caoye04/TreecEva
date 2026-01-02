def calculate_final_score(results, weights):
    base_scores = {}
    for subject, score in results.items():
        if score >= 75:
            base_scores[subject] = score * 1.1
        else:
            base_scores[subject] = score * 0.95
    
    weighted_sum = 0.0
    total_weight = 0
    for subject, weight in weights.items():
        if subject in base_scores:
            weighted_sum += base_scores[subject] * weight
            total_weight += weight
    
    avg_weighted = weighted_sum / total_weight if total_weight > 0 else 0
    
    adjustment = 5 if avg_weighted > 80 else 2
    final_score = avg_weighted + adjustment
    
    # Irrelevant tracking variable (minimal interference)
    status_log = "Processing complete"
    return int(round(final_score))

# Input data
exam_results = {
    'math': 82,
    'physics': 78,
    'chemistry': 90,
    'biology': 65
}

bonus_weights = {
    'math': 3,
    'physics': 2,
    'chemistry': 4,
    'literature': 1  # Not in exam_results, should be ignored
}

final_score = calculate_final_score(exam_results, bonus_weights)
print(f"Target result: {final_score}")