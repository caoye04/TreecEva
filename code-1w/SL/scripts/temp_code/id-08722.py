def compute_final_score(results):
    weighted_scores = []
    max_possible = 100
    score_adjustment = 5  # minor adjustment factor (distractor)

    for i, (score, category) in enumerate(zip(results['scores'], results['categories'])):
        if category == 'math':
            weight = 1.2
        elif category == 'logic':
            weight = 1.5
        else:
            weight = 1.0

        adjusted_score = score * weight
        weighted_scores.append(adjusted_score)

    base_total = sum(weighted_scores)
    bonus = len(results['scores']) * 2 if base_total > 90 else 0
    total_score = base_total + bonus

    return total_score

# Irrelevant auxiliary data (light distractor)
data_log = {'timestamp': '2023-01-01', 'user': 'test_user'}
system_config = {'version': '1.2.1', 'debug': True}

# Input data
results = {
    'scores': [85, 90, 78, 92],
    'categories': ['math', 'logic', 'math', 'logic']
}

# Computation
final_external = 0  # unused variable (minor distraction)
total_score = compute_final_score(results)
print(f"Target result: {total_score}")