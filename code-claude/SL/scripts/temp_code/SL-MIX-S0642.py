def apply_curve(score, curve_factor=1.0):
    # Apply curve to score (not used in final calculation)
    return score * curve_factor

def normalize_weight(weight):
    # Ensure weight is between 0 and 1
    return max(0, min(1, weight))

# Student exam scores
student_scores = {'quiz': 85, 'midterm': 72, 'project': 95, 'participation': 88, 'final': 79}

# Importance weights for each component
weights = {'quiz': 0.15, 'midterm': 0.25, 'project': 0.2, 'participation': 0.1, 'final': 0.3}

# Additional data (not directly used in calculation)
extra_credit = {'quiz': 2, 'midterm': 0, 'project': 5, 'participation': 0, 'final': 3}
class_averages = {'quiz': 78, 'midterm': 75, 'project': 82, 'participation': 90, 'final': 76}

# Process scores with lambda functions
process_score = lambda score, component: score if component != 'participation' else min(score, 100)
adjust_weight = lambda w, component: w * 1.05 if component == 'final' else w

def calculate_final_score(scores, weights):
    # Initialize variables
    weighted_sum = 0
    weight_total = 0
    bonus_points = 0
    
    # Calculate potential curve (not applied)
    potential_curve = sum(class_averages.values()) / len(class_averages)
    
    # Process each component
    for component in scores:
        # Apply processing to scores
        processed_score = process_score(scores[component], component)
        
        # Normalize weight (though weights are already normalized)
        norm_weight = normalize_weight(weights[component])
        
        # Apply adjustment to weight for final exam
        adjusted_weight = adjust_weight(norm_weight, component)
        
        # Track bonus points (not used in final calculation)
        if component in extra_credit:
            bonus_points += extra_credit[component]
            
        # Add to weighted sum
        weighted_sum += processed_score * adjusted_weight
        weight_total += adjusted_weight
    
    # Calculate raw score (not used)
    raw_score = sum(scores.values()) / len(scores)
    
    # Calculate final score
    if weight_total > 0:
        final_score = weighted_sum / weight_total
    else:
        final_score = 0
    
    # Round to one decimal place
    return round(final_score, 1)

# Calculate the final score
result = calculate_final_score(student_scores, weights)
print(f"Result: {result}")