product_scores = [85, 92, 78, 95, 88, 67, 91, 84]
quality_threshold = 80
scaling_factor = 1.25

# Filter products above quality threshold
filtered_products = [score for score in product_scores if score >= quality_threshold]

# Calculate some intermediate metrics (distractor operations)
average_all = sum(product_scores) / len(product_scores)
max_possible = max(product_scores) * 1.5
score_range = max(product_scores) - min(product_scores)

# Calculate weighted average (distractor)
weights = [i * 0.1 for i in range(1, len(filtered_products) + 1)]
weighted_avg = sum(f * w for f, w in zip(filtered_products, weights)) / sum(weights)

# Final quality calculation
final_quality_score = max(filtered_products) * scaling_factor

print(f"Result: {final_quality_score}")