def evaluate_performance(metrics, weights):
    # Normalize metrics using lambda and map
    normalized = list(map(lambda x: (x - min(metrics)) / (max(metrics) - min(metrics) + 1e-5), metrics))

    # Apply weights with element-wise multiplication
    weighted_scores = [n * w for n, w in zip(normalized, weights)]

    # Distractor: unused calculation of geometric mean
    product = 1.0
    for m in metrics:
        product *= (m + 1)
    geometric_mean = product ** (1 / len(metrics))

    # Calculate final score as weighted sum
    final_score = sum(weighted_scores)

    # Additional distractor: simulate threshold checks that don't affect result
    compliance_flags = set()
    for idx, val in enumerate(weighted_scores):
        if val > 0.5:
            compliance_flags.add(f"high_{idx}")
        elif val > 0.2:
            compliance_flags.add(f"medium_{idx}")

    # Simulate auxiliary processing with bitwise interference (distractor)
    mask = 0b101
    masked_values = []
    for i in range(len(weighted_scores)):
        masked_values.append(int(final_score * 100) & mask)

    # Early return simulation (not triggered but adds logic depth)
    if len(compliance_flags) == 0:
        return -1

    return final_score

# Main execution
metrics = [85, 90, 78, 92, 88]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Irrelevant pre-processing (distractor)
adjusted_metrics = [m * 1.02 for m in metrics]
dropped = [m for m in adjusted_metrics if m < 80]

# Key statement
final_score = evaluate_performance(metrics, weights)

# Print result
print(f"Result: {final_score}")