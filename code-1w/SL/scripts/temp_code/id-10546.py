def evaluate_performance(metrics, weights):
    # Normalize metrics using min-max scaling (irrelevant for final logic but adds distraction)
    normalized = {}
    for k, v in metrics.items():
        if v > 0:
            normalized[k] = (v - 1) / (10 - 1) * 100
        else:
            normalized[k] = 0

    # Irrelevant transformation: string-based encoding of metric names
    encoded_keys = ''.join([k[0].upper() for k in metrics.keys()])
    key_hash = sum([ord(c) for c in encoded_keys]) % 100

    # Core logic begins: weighted harmonic mean of selected metrics
    selected_metrics = ['accuracy', 'latency', 'throughput']
    product_scores = []

    for metric_name in selected_metrics:
        raw_value = metrics.get(metric_name, 1)
        weight = weights.get(metric_name, 0.0)
        if raw_value > 0 and weight > 0:
            # Transform each into contribution via harmonic component
            contribution = weight / (1.0 / raw_value)
            product_scores.append(contribution)

    # Secondary irrelevant computation: set operations on keys
    metric_set_a = set(metrics.keys())
    metric_set_b = set(weights.keys())
    overlap = metric_set_a & metric_set_b
    extra_info = len(overlap) * 10 + key_hash

    # More distraction: enumerate and zip usage with unused tuple unpacking
    indexed_weights = list(enumerate(sorted(weights.values())))
    paired_data = list(zip(metrics.values(), weights.values()))
    temp_sum = sum([a * b for a, b in paired_data[:2]])  # Used nowhere

    # Actual determination of score: geometric mean of product scores
    if not product_scores:
        return 0.0

    running_product = 1.0
    for val in product_scores:
        running_product *= val

    geometric_mean = running_product ** (1.0 / len(product_scores))

    # Final adjustment based on auxiliary calculation (extra_info affects result slightly)
    final_score = geometric_mean + (extra_info / 1000.0)

    return final_score

# Main execution
metrics = {
    'accuracy': 9,
    'latency': 3,
    'throughput': 7,
    'memory_usage': 5,
    'scalability': 8
}
weights = {
    'accuracy': 0.4,
    'latency': 0.3,
    'throughput': 0.3,
    'energy_efficiency': 0.1
}

intermediate_result = sum(metrics.values()) * 0.1  # Distractor variable
placeholder_list = [1, 1, 2, 3, 5, 8]
for i, val in enumerate(placeholder_list):
    if i % 2 == 0:
        placeholder_list[i] = val * 2

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")