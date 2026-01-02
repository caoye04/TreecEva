def calculate_final_score(rankings, weights):
    normalized = {k: (1 / v) for k, v in rankings.items()}
    sorted_keys = sorted(normalized, key=normalized.get, reverse=True)
    weighted_values = [normalized[k] * weights[i % len(weights)] for i, k in enumerate(sorted_keys)]
    return int(sum(weighted_values))

# Initial data
rankings = {'alpha': 4, 'beta': 2, 'gamma': 8, 'delta': 1}
weights = [1.5, 0.5, 2.0]

# Computation
intermediate_total = sum(rankings.values())
dummy_flag = intermediate_total > 10
final_score = calculate_final_score(rankings, weights)
print(f"Result: {final_score}")