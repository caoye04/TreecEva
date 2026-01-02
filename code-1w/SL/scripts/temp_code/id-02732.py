from collections import defaultdict

def calculate_final_score(weights, scores):
    weighted_sum = 0.0
    total_weight = 0.0
    
    # Normalize weights using dictionary operations
    weight_dict = defaultdict(float, weights)
    score_dict = {k: v for k, v in scores}
    
    # Apply weights to each exam score using slicing and iteration
    for subject in list(weight_dict.keys())[::1]:
        if subject in dict(scores):
            raw_score = dict(scores)[subject]
            weight = weight_dict[subject]
            weighted_sum += raw_score * weight
            total_weight += weight

    # Compute final weighted average
    return round(weighted_sum / total_weight, 3) if total_weight > 0 else 0.0

# Input data as tuples
exam_weights = [('math', 0.4), ('physics', 0.35), ('chemistry', 0.25)]
raw_scores = [('math', 88), ('physics', 92), ('chemistry', 85)]

# Irrelevant distraction: unused variable (minimal interference)
dummy_flag = True

final_score = calculate_final_score(exam_weights, raw_scores)
print(f"Result: {final_score}")