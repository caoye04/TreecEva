def calculate_final_score(results, weights):
    base_total = 0
    adjustment = 0
    weight_factor = weights['core']
    
    for subject, score in results.items():
        if score >= 75:
            base_total += score * weight_factor
        else:
            base_total += score * 0.8
    
    # Apply bonus for science subjects
    science_bonus = (results['physics'] + results['chemistry']) * weights['bonus']
    adjustment = int(science_bonus / 10)
    
    raw_score = base_total + adjustment
    
    # Normalize to a 100-point scale
    final_score = raw_score / len(results)
    return final_score

# Simulated exam data
exam_results = {
    'math': 88,
    'physics': 92,
    'chemistry': 78,
    'literature': 81,
    'history': 73
}

bonus_weights = {
    'core': 1.1,
    'bonus': 0.15
}

# Irrelevant distraction: unused variable
placeholder_value = 999

final_score = calculate_final_score(exam_results, bonus_weights)
print(f"Result: {final_score}")