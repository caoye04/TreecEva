def calculate_final_score(ranks, coeffs):
    normalized = [1 / (r + 1) for r in ranks]
    weighted_vals = list(map(lambda x: round(x * 10, 2), normalized))
    scaled_coeffs = [int(c * 5) for c in coeffs]
    product_pairs = zip(weighted_vals, scaled_coeffs)
    partial_products = [val * coeff for val, coeff in product_pairs]
    total = sum(partial_products)
    penalty = 0
    for i, rank in enumerate(ranks):
        if rank > 3:
            penalty += 1
    final_adjustment = total - penalty * 2.5
    return int(final_adjustment)

# Input data
rankings = [1, 4, 2, 5, 3]
weights = [0.8, 0.5, 1.2, 0.9, 1.0]

# Irrelevant auxiliary variable (minor distraction)
dummy_var = [x ** 2 for x in range(3)]

# Key computation
intermediate_result = [rankings[i] + weights[i] for i in range(len(rankings))]
total_score = calculate_final_score(rankings, weights)
print(f"Result: {total_score}")