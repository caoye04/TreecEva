ratings = [85, 90, 78, 92]
weights = [0.2, 0.3, 0.1, 0.4]

# Compute weighted average as adjustment factor
adjustment_factor = sum(w * (r / 10) for r, w in zip(ratings, weights))

# Normalize ratings to range [0, 1]
normalized_ratings = {r / 100 for r in ratings}

# Apply conditional scaling based on threshold
scaled_normalized = {val if val >= 0.8 else val * 1.1 for val in normalized_ratings}

# Determine final score using lambda-based max selection
final_score = max(scaled_normalized, key=lambda x: x * adjustment_factor)

print(f"Result: {final_score}")