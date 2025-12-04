# Student exam score analysis
raw_scores = [65, 72, 88, 91, 65, 76, 88, 93, 72, 84]
curve_adjustment = 5
adjusted_scores = [score + curve_adjustment for score in raw_scores]

# Filter out any scores above 100 (maximum possible)
max_possible = 100
filtered_scores = [min(score, max_possible) for score in adjusted_scores]

# Calculate passing threshold (70% of maximum)
passing_threshold = 0.7 * max_possible

# Count how many unique scores are above the passing threshold
unique_elements = len(set([x for x in filtered_scores if x > passing_threshold]))

# Additional statistics (not relevant to the main calculation)
avg_score = sum(filtered_scores) / len(filtered_scores)
lowest_score = min(filtered_scores)

print(f"Result: {unique_elements}")