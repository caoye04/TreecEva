def evaluate_performance(weights, outcomes):
    # Normalize outcomes using min-max scaling (irrelevant for final result)
    min_val = min(outcomes)
    max_val = max(outcomes)
    range_val = max_val - min_val if max_val != min_val else 1
    normalized = [(x - min_val) / range_val for x in outcomes]

    # Apply weights with element-wise multiplication using lambda
    weighted_values = list(map(lambda w, x: w * x, weights, outcomes))

    # Calculate weighted sum
    weighted_sum = sum(weighted_values)

    # Additional distraction: simulate confidence intervals (not used)
    variance = sum([(x - sum(outcomes)/len(outcomes))**2 for x in outcomes]) / len(outcomes)
    std_dev = variance ** 0.5
    margin_of_error = 1.96 * std_dev / (len(outcomes) ** 0.5)

    # Simulate bonus logic based on threshold (distractor branch)
    bonus_applied = False
    if sum(outcomes) > 30:
        extra_bonus = 5.0
        bonus_applied = True  # never used

    # Critical computation: apply penalty if any weight is below 0.1
    penalty = 0
    for w in weights:
        if w < 0.1:
            penalty += 10

    # Final score calculation (this is what matters)
    base_score = weighted_sum * 10
    final_score = base_score - penalty

    return final_score

# Main execution
metric_weights = [0.2, 0.05, 0.3, 0.45]
raw_outcomes = [8, 6, 7, 9]

# Irrelevant pre-processing (distractor)
processed_data = raw_outcomes[1:3]  # slice operation
offset_correction = sum([x**2 for x in processed_data]) * 0.01

# Key statement
final_score = evaluate_performance(metric_weights, raw_outcomes)

# Print result as required
print(f"Target result: {final_score}")