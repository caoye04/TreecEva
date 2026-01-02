def calculate_final_score(results):
    weights = {'accuracy': 0.5, 'speed': 0.3, 'consistency': 0.2}
    weighted_scores = [weights[k] * v for k, v in results.items() if k in weights]
    return round(sum(weighted_scores), 3)

# Performance metrics from user test session
test_data = {'attempts': 5, 'errors': 2, 'accuracy': 88.0, 'speed': 75.0, 'consistency': 90.0, 'feedback_score': 4.5}

# Irrelevant helper (mild distraction)
process = lambda data: {k: v for k, v in data.items() if isinstance(v, (int, float))}
cleaned = process(test_data)

final_score = calculate_final_score(test_data)
print(f"Target result: {final_score}")