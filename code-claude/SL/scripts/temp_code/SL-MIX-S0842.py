# Calculate weighted average of student scores
scores = [85, 92, 78, 90]
weights = [0.2, 0.3, 0.15, 0.35]
total_weights = sum(weights)

# Store some metadata about the scores
num_scores = len(scores)
max_score = max(scores)
min_score = min(scores)

# Calculate weighted sum of scores
result = sum(map(lambda x: x[0] * x[1], zip(weights, scores)))

# Display the result
print(f"Result: {result}")