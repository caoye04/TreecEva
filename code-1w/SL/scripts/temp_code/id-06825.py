def calculate_final_score(ranks, coeffs):
    base_scores = [100 - rank for rank in ranks]
    weighted_scores = [score * weight for score, weight in zip(base_scores, coeffs)]
    adjusted_scores = [s + 5 if s < 90 else s - 2 for s in weighted_scores]
    total = sum(adjusted_scores)
    bonus = 10 if all(s >= 85 for s in adjusted_scores) else 0
    return total + bonus

# Irrelevant distraction variables
dummy_data = [1, 1, 2, 3, 5, 8]
scaling_factor = 1.5

rankings = [1, 3, 2, 4]
weights = [0.2, 0.3, 0.4, 0.1]

final_score = calculate_final_score(rankings, weights)
print(f"Target result: {final_score}")