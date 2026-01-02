def calculate_final_score(results):
    weights = {'midterm': 0.3, 'final': 0.5, 'project': 0.2}
    weighted_sum = 0
    for key in results:
        if key in weights:
            weighted_sum += results[key] * weights[key]
    return int(weighted_sum)

exam_results = {
    'midterm': 85,
    'final': 92,
    'project': 78,
    'attendance': 100  # irrelevant field (distractor)
}

# Preprocessing: normalize final exam if above threshold
if exam_results['final'] > 90:
    exam_results['final'] = 95  # cap at 95

final_score = calculate_final_score(exam_results)
print(f"Result: {final_score}")