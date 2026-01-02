def calculate_final_score(results):
    weights = {'midterm': 0.3, 'final': 0.5, 'project': 0.2}
    weighted_scores = [results[k] * weights[k] for k in weights]
    return sum(weighted_scores)

exam_results = {
    'midterm': 85,
    'final': 92,
    'project': 78,
    'attendance': 100  # irrelevant to calculation
}

# Extra variable for minor distraction
temp_buffer = [0] * 5

final_score = calculate_final_score(exam_results)
print(f"Result: {final_score}")