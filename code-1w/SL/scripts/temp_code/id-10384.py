def calculate_final_score(data, importance):
    base = 0
    bonus = 0
    scaling_factor = 1.5

    # Process each category score with its weight
    for key in data:
        if key in importance:
            base += data[key] * importance[key]
    
    # Apply conditional bonus based on performance threshold
    if data['accuracy'] > 85:
        bonus = 10
    
    # Irrelevant distraction: unused variable
    temp_debug_log = "Processing complete"
    
    final_score = (base * scaling_factor) + bonus
    return final_score

# Input datasets
category_results = {
    'accuracy': 90,
    'speed': 75,
    'consistency': 80,
    'coverage': 70
}

weights = {
    'accuracy': 0.4,
    'speed': 0.3,
    'consistency': 0.2,
    'coverage': 0.1
}

# Compute result
final_score = calculate_final_score(category_results, weights)

Result: {final_score}