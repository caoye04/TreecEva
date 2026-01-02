def calculate_final_score(results, weights):
    base_scores = {k: v * 0.8 for k, v in results.items() if v >= 60}
    adjusted_scores = {}
    for subject, score in base_scores.items():
        if subject in weights:
            adjusted_scores[subject] = score + (weights[subject] * 10)
        else:
            adjusted_scores[subject] = score + 5
    extra_credit_pool = sum(weights.values()) * 2
    final_sum = sum(adjusted_scores.values()) + extra_credit_pool
    scaling_factor = 1.05
    return int(final_sum * scaling_factor)

exam_results = {'math': 85, 'physics': 70, 'chemistry': 90, 'literature': 45}
bonus_weights = {'math': 1.2, 'physics': 0.8, 'chemistry': 1.0}
temporary_buffer = [x ** 2 for x in range(5)]
metadata_log = {'version': '2.1', 'author': 'evaluator'}
final_score = calculate_final_score(exam_results, bonus_weights)
print(f"Result: {final_score}")