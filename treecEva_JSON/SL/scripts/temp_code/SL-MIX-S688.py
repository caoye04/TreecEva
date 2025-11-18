import math

# Simulated logarithmic returns for 5 assets
log_returns = [0.02, -0.01, 0.03, -0.02, 0.05]
smoothing_factor = 0.8
outlier_threshold = 0.025
metadata_tags = ['low_risk', 'medium_risk', 'high_risk', 'medium_risk', 'low_risk']

# Step 1: Apply exponential smoothing to log returns
smoothed_returns = [
    log_returns[i] * smoothing_factor + 
    (log_returns[i-1] if i > 0 else 0) * (1 - smoothing_factor)
    for i in range(len(log_returns))
]

# Step 2: Filter outliers using logical conditions
filtered_returns = [
    ret if abs(ret) <= outlier_threshold else 
    (outlier_threshold if ret > 0 else -outlier_threshold)
    for ret in smoothed_returns
]

# Step 3: Compute risk scores using exponentiation
risk_scores = [math.exp(ret) for ret in filtered_returns]

# Step 4: Adjust scores based on metadata tags
adjusted_scores = [
    score * (0.9 if 'low_risk' in tag else 1.1 if 'high_risk' in tag else 1.0)
    for score, tag in zip(risk_scores, metadata_tags)
]

# Step 5: Aggregate with logical weighting
weights = [1.0 if x > 0 else 0.5 for x in filtered_returns]
weighted_sum = sum(score * weight for score, weight in zip(adjusted_scores, weights))
total_weight = sum(weights)

# Final computation with ternary operator
final_risk_score = weighted_sum / total_weight if total_weight != 0 else 0.0

print(f"Result: {final_risk_score:.6f}")