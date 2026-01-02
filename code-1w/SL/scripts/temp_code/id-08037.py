from collections import defaultdict

# Simulate student subject scores and weighting factors
scores = {'math': 85, 'physics': 90, 'chemistry': 78, 'biology': 88}
weights = {'math': 0.3, 'physics': 0.25, 'chemistry': 0.2, 'biology': 0.25}

def calculate_final_score(score_dict, weight_dict):
    weighted_sum = 0.0
    total_weight = sum(weight_dict.values())
    
    # Apply weights using enumerate for positional tracking (though not strictly needed)
    for i, (subject, score) in enumerate(score_dict.items()):
        if subject in weight_dict:
            weighted_sum += score * weight_dict[subject]
    
    # Normalize by total weight (redundant here since weights sum to 1.0, but included for robustness)
    normalized_score = weighted_sum / total_weight if total_weight else 0
    return round(normalized_score, 3)

# Irrelevant auxiliary data (minor distraction, intervention level 4)
student_data = defaultdict(lambda: 'N/A')
student_data['name'] = 'Alice'
student_data['grade_level'] = 11

# Calculation of interest
target_result = calculate_final_score(scores, weights)
print(f"Target result: {target_result}")