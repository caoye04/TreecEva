def calculate_final_score(results, weights):
    base_score = 0
    adjustment = 0
    
    # Process each subject's result using dictionary keys
    for subject in results:
        if subject in weights:
            base_score += results[subject] * weights[subject]
        else:
            base_score += results[subject] * 0.1
    
    # Apply adjustment based on performance thresholds
    if base_score > 75:
        adjustment = 10
    elif base_score >= 60:
        adjustment = 5
    
    # Minor irrelevant tracking variable (minimal interference)
    record_timestamp = True
    
    final_score = base_score + adjustment
    return final_score

# Input data
exam_results = {'math': 85, 'physics': 70, 'chemistry': 90}
bonus_weights = {'math': 1.2, 'physics': 1.1}

# Computation entry point
target_result = calculate_final_score(exam_results, bonus_weights)
final_score = target_result

print(f"Result: {final_score}")