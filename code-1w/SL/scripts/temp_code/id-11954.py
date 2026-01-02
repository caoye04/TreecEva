from itertools import combinations

# Simulate student scores and weighted evaluation
def calculate_final_score(raw_scores, weight_factors):
    normalized = [score / 10 for score in raw_scores]
    weighted = map(lambda x: x[0] * x[1], zip(normalized, weight_factors))
    base_total = sum(weighted)

    # Bonus logic for consistent performance
    variation_pairs = list(combinations(normalized, 2))
    consistency_bonus = 0
    for a, b in variation_pairs:
        if abs(a - b) < 1.0:
            consistency_bonus += 0.5
    
    final_adjustment = len(variation_pairs) > 0
    result = base_total + (consistency_bonus if final_adjustment else 0)
    return result

# Irrelevant auxiliary variable (minimal distraction)
dummy_threshold = 75

scores = [85, 90, 88, 92]
weights = [0.2, 0.3, 0.25, 0.25]

result = calculate_final_score(scores, weights)
print(f"Target result: {result}")