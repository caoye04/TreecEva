# Calculate weighted average of filtered student scores
scores = [85, 92, 78, 95, 88]
weights = [0.15, 0.25, 0.20, 0.30, 0.10]

# Filter scores above threshold
threshold = 80
filtered_scores = list(filter(lambda score: score >= threshold, scores))

# Calculate number of scores that met the threshold
qualifying = len(filtered_scores)
print(f"Qualifying scores: {qualifying}")

# Create descriptive statistics
avg_score = sum(filtered_scores) / qualifying
max_score = max(filtered_scores)
min_score = min(filtered_scores)

# Calculate the weighted sum of filtered scores
final_score = sum(map(lambda x: x[0] * x[1], zip(weights, filtered_scores)))

# Format the score as a percentage
score_percentage = f"{final_score:.1f}%"

print(f"Result: {final_score}")