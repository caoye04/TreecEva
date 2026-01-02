def calculate_final_score(results, weights):
    base_scores = {k: sum(v[1:4]) for k, v in results.items()}
    weighted_bonus = 0
    
    for subject, data in results.items():
        if subject in weights:
            raw_bonus = data[0] * weights[subject]
            capped_bonus = min(raw_bonus, 10)
            weighted_bonus += capped_bonus
    
    total_base = sum(base_scores.values())
    adjustment = len(base_scores) * 2.5
    final_score = total_base + weighted_bonus + adjustment
    
    # Irrelevant tracking variable (low interference)
    score_count = len(base_scores)
    return final_score

# Input data: [initial_factor, test1, test2, test3]
exam_results = {
    'math': [0.8, 70, 82, 78],
    'physics': [0.9, 65, 88, 70],
    'chemistry': [0.7, 75, 80, 74]
}

bonus_weights = {
    'math': 1.2,
    'physics': 1.5,
    'chemistry': 1.0
}

final_score = calculate_final_score(exam_results, bonus_weights)
print(f"Result: {final_score}")