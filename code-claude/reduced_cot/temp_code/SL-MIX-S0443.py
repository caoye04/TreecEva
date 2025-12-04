# Calculate student test scores with weightings

# Raw test scores (out of 100)
test_scores = [85, 92, 78, 90]

# Corresponding weights for each test (adds up to 1.0)
weights = [0.2, 0.3, 0.15, 0.35]

# Calculate passing threshold
pass_threshold = 80
max_bonus = 5

# Use zip to pair scores with weights and calculate weighted scores
weighted_scores = []
for i, (score, weight) in enumerate(zip(test_scores, weights)):
    weighted_score = score * weight
    # Add small bonus for scores above threshold
    if score > pass_threshold:
        bonus = min((score - pass_threshold) * 0.1, max_bonus * weight)
        weighted_score += bonus
    weighted_scores.append(weighted_score)

# Calculate total weighted score
total_score = sum(weighted_scores)

print(f"Result: {total_score}")