import itertools

# Analyze data segments and calculate composite metrics
data_segments = [12, 8, 15, 6, 9, 11]
segment_pairs = list(itertools.combinations(data_segments, 2))

# Calculate difference products (distractor calculation)
diff_products = []
for pair in segment_pairs:
    diff = abs(pair[0] - pair[1])
    product = diff * (pair[0] + pair[1])
    diff_products.append(product)

# This sum is not used in final calculation (interference)
unused_sum = sum(diff_products)

# Calculate weighted segment scores
weighted_scores = []
for i, segment in enumerate(data_segments):
    weight = 1.5 if segment > 10 else 0.8
    weighted = segment * weight
    weighted_scores.append(weighted)

# Filter and process relevant scores
filtered_scores = [score for score in weighted_scores if score > 12]

# Calculate average of filtered scores (distractor)
avg_filtered = sum(filtered_scores) / len(filtered_scores) if filtered_scores else 0

# Core calculation: analyze score patterns
pattern_sum = 0
for score in weighted_scores:
    if score % 2 == 0:
        pattern_sum += score * 2
    else:
        pattern_sum += score * 3

# Final analysis score (target variable)
final_analysis_score = pattern_sum - (max(weighted_scores) if weighted_scores else 0)

# Redundant calculation (interference)
redundant_calc = final_analysis_score * 0.75 + avg_filtered

result = final_analysis_score
print(f"Result: {result}")