def calculate_final_score(results, weights):
    base_total = 0
    bonus_total = 0
    
    # Aggregate exam scores
    for subject, score in results.items():
        if score >= 60:
            base_total += score * 0.8
        else:
            base_total += score * 0.5
    
    # Apply weighted bonuses
    for category, weight in weights.items():
        bonus_total += weight * 5
    
    return int(base_total // 10 + bonus_total)

# Student exam data
exam_results = {
    'math': 85,
    'physics': 70,
    'chemistry': 55,
    'biology': 90
}

bonus_weights = {
    'science': 2,
    'advanced': 1
}

# Irrelevant placeholder for slight distraction (minimal interference)
temp_data = [1, 2, 3]
scaling_factor = 1.0  # Unused variable

final_score = calculate_final_score(exam_results, bonus_weights)
print(f"Result: {final_score}")