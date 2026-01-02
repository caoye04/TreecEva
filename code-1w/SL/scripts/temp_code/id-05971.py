def calculate_final(scores, weights):
    weighted_sum = sum(scores[subject] * weights[subject] for subject in scores)
    total_weight = sum(weights[subject] for subject in scores)
    return round(weighted_sum / total_weight, 3)

# Student exam scores and subject weights
exam_scores = {'math': 88, 'physics': 92, 'chemistry': 76, 'biology': 85}
weight_map = {'math': 0.3, 'physics': 0.3, 'chemistry': 0.2, 'biology': 0.2}

# Irrelevant distraction: extra subject not in use
temp_subject = 'history'
dropped_score = 73

# Key computation
final_score = calculate_final(exam_scores, weight_map)

# Output result
print(f"Result: {final_score}")