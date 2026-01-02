def evaluate_performance(metrics, weights):
    # Normalize metrics using lambda for dynamic scaling
    normalized = list(map(lambda x: x / max(metrics) if max(metrics) != 0 else 0, metrics))

    # Irrelevant transformation: reverse and scale (not used in final calculation)
    reversed_scaled = [x * 1.5 for x in reversed(normalized)]
    dummy_metric = sum(reversed_scaled) / len(reversed_scaled) if reversed_scaled else 0

    # Weighted score computation
    weighted_sum = 0
    for i in range(len(normalized)):
        if i % 2 == 0:
            weighted_sum += normalized[i] * weights[i] * 1.1  # Boost even indices slightly
        else:
            weighted_sum += normalized[i] * weights[i]

    # Secondary adjustment based on threshold filtering
    adjustments = []
    for val in metrics:
        if val > sum(metrics) / len(metrics):  # Above average
            adjustments.append(val * 0.05)
        else:
            adjustments.append(0)

    adjustment_total = sum(adjustments)

    # Distractor: complex tuple unpacking with unused components
    config = ('algorithm_v3', 'scaling_active', 0.95)
    _, _, fallback_factor = config

    # Simulate early return that isn't triggered
    if len(metrics) == 0:
        return 0

    # Final score with minor bump from adjustment
    base_score = weighted_sum * 100
    final_score = base_score + adjustment_total

    # Unused data structure creation (set operations as red herring)
    metric_set = set(metrics)
    outlier_check = {x for x in metric_set if x > 3 * sum(metric_set) / len(metric_set)}

    return final_score

# Main execution
metrics = [85, 90, 78, 92, 88]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Preprocessing distraction: case conversion on string list (unrelated)
data_labels = ['Test_A', 'TEST_B', 'test_c']
processed_labels = [label.lower().replace('_', '-') for label in data_labels]

# Key execution point
temp_result = evaluate_performance(metrics, weights)
final_score = round(temp_result, 2)

print(f"Result: {final_score}")