def calculate_final_score(data, importance):
    base_scores = {k: len(v) for k, v in data.items()}
    weighted = [base_scores[key] * importance[key] for key in base_scores]
    adjustment = sum([i for i in weighted if i > 5])
    final_score = sum(weighted) - adjustment * 0.1
    return final_score

# Simulation of user interaction results
task_results = {
    'login_flow': ['success', 'retry', 'success'],
    'payment_step': ['error', 'success', 'timeout', 'success'],
    'confirmation': ['success']
}
weights = {'login_flow': 1.2, 'payment_step': 2.0, 'confirmation': 1.5}

# Irrelevant auxiliary variable (minimal distraction)
user_count = 42

final_score = calculate_final_score(task_results, weights)
print(f"Target result: {final_score}")