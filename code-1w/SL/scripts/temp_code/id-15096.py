def compute_weighted_ranks(elements):
    weights = [0.8, 1.2, 0.9, 1.1, 1.0]
    base_scores = list(map(lambda x: len(x) * 1.5, elements))
    weighted_scores = [base_scores[i] * weights[i] for i in range(len(base_scores))]
    sorted_scores = sorted(weighted_scores, reverse=True)
    return sorted_scores

# Input data representing project names
projects = ['alpha', 'beta_redux', 'gamma', 'delta_prime', 'epsilon']

# Irrelevant distraction: unused variable (minimal interference)
baseline = sum(len(p) for p in projects) / len(projects)

# Compute ranking
final_ranking = compute_weighted_ranks(projects)

# Key execution point
threshold_score = final_ranking[2]

print(f"Result: {threshold_score}")