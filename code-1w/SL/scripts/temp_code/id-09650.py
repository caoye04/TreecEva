from itertools import compress

# Simulate user ratings and review lengths for a content ranking system
documents = ['doc_A', 'doc_B', 'doc_C', 'doc_D']
ratings = [3.5, 4.2, 3.8, 4.0]
review_lengths = [120, 180, 90, 200]  # in words

# Calculate normalized rating per word efficiency
efficiency_scores = [r / (l / 100) for r, l in zip(ratings, review_lengths)]

# Use short reviews as filter (less than 150 words)
valid_indices = [length < 150 for length in review_lengths]
filtered_efficiency = list(compress(efficiency_scores, valid_indices))

# Normalize ratings using min-max scaling
min_eff = min(filtered_efficiency)
max_eff = max(filtered_efficiency)
normalized_ratings = [(score - min_eff) / (max_eff - min_eff) for score in filtered_efficiency]

adjustment_factor = 1.5
final_score = max(normalized_ratings) * adjustment_factor
print(f"Result: {final_score}")