def evaluate_performance(feedback):
    score = 0
    adjustments = {'accuracy': 0.8, 'clarity': 1.2, 'efficiency': 0.9}
    weights = {'accuracy': 4, 'clarity': 3, 'efficiency': 5}
    temp_buffer = [0] * len(feedback)  # Irrelevant preallocation (distractor)

    for i, (key, value) in enumerate(feedback.items()):
        if key in adjustments:
            adjusted_val = value * adjustments[key]
            weighted = adjusted_val * weights[key]
            score += weighted

    outlier_threshold = 10  # Unused variable (minor distractor)
    final_score = int(score / sum(weights.values()))
    return final_score

# Input data
evaluation_data = {'accuracy': 8, 'clarity': 7, 'efficiency': 9}

# Execution
temp_result = sum(evaluation_data.values())  # Minor irrelevant computation
final_score = evaluate_performance(evaluation_data)
print(f"Result: {final_score}")