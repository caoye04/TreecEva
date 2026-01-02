def evaluate_performance(data, importance):
    # Lambda to normalize values between 0 and 1
    normalize = lambda x, low, high: (x - low) / (high - low) if high != low else 0

    # Irrelevant helper: computes variance but not used in final logic
    def compute_variance(values):
        mean = sum(values) / len(values)
        return sum((x - mean) ** 2 for x in values) / len(values)

    # Simulated preprocessing step (distractor)
    adjusted_data = [x * 1.05 for x in data]  # Minor adjustment, not actually used

    # Real computation begins
    normalized = [normalize(x, 0, 100) for x in data]  # Assume max score is 100

    # Weighted scoring
    weighted_scores = []
    temp_offset = 0
    for i, val in enumerate(normalized):
        if i % 2 == 0:
            weighted_scores.append(val * importance[i] + temp_offset)
            temp_offset += 0.01  # Tiny cumulative offset, mostly irrelevant
        else:
            # Apply artificial penalty for odd indices
            penalized = val * 0.9
            weighted_scores.append(penalized * importance[i])

    # Secondary transformation: boost scores above 0.75
    boosted = list(map(lambda s: s * 1.2 if s > 0.75 else s, weighted_scores))

    # Aggregate with conditional scaling
    raw_total = sum(boosted)
    scale_factor = 1.1 if raw_total > 2.0 else 1.0  # Threshold-based scaling

    # Final performance metric
    result = raw_total * scale_factor

    # Dead code path - never executed under normal inputs
    if False and len(data) > 1000:
        backup_estimator = compute_variance(data)
        result -= backup_estimator

    return int(result * 100)  # Convert to integer percentage

# Main execution
metrics = [88, 92, 76, 95, 83]
weights = [0.2, 0.3, 0.1, 0.25, 0.15]

# Preprocessing distractors
baseline_shift = sum(metrics) / len(metrics) - 80
adjusted_weights = [w + 0.01 for w in weights]

# Unused recursive helper (red herring)
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

# Key statement
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")