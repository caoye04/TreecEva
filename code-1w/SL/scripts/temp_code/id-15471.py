def evaluate_performance(metrics, weights):
    # Normalize metrics to a 0-1 scale
    normalized = {k: v / 100.0 for k, v in metrics.items() if v > 0}

    # Irrelevant transformation: character counting on keys
    key_length_sum = sum(len(k) for k in metrics.keys())
    dummy_shift = key_length_sum % 7

    # Distractor: unused data structure manipulation
    reversed_metrics = {k[::-1]: v for k, v in metrics.items()}
    flipped_weights = {k[::-1]: w for k, w in weights.items()}

    # Core logic begins: filter only valid metric entries
    valid_keys = set(normalized.keys()) & set(weights.keys())
    if not valid_keys:
        return 0.0

    # Apply weights conditionally using ternary-like expressions
    weighted_sum = sum(
        normalized[k] * weights[k] if k in weights else normalized[k] * 0.1
        for k in normalized
    )

    # Secondary adjustment based on set intersection size
    adjustment_factor = len(valid_keys) / len(weights) if weights else 1.0

    # Tertiary score boost if certain conditions are met (conditional expression)
    bonus = 5.0 if len(metrics) >= 3 and 'accuracy' in metrics else 0.0

    # Final aggregation with rounding
    raw_score = weighted_sum * adjustment_factor + bonus
    final_score = round(raw_score, 4)

    # Dead code path: never executed due to prior conditions
    if False and 'f1' in metrics:
        extra_penalty = -2.5
        final_score += extra_penalty

    return final_score


# Input data
metric_set = {
    'accuracy': 88,
    'precision': 92,
    'recall': 85,
    'latency_ms': -10  # Invalid (negative), will be filtered out
}

benchmark_weights = {
    'accuracy': 0.4,
    'precision': 0.3,
    'recall': 0.3
}

# Intermediate distractor computation
auxiliary_total = sum(v * 2 for v in benchmark_weights.values())
dummy_list = [1, 1, 2, 3, 5, 8]
filtered_primes = [x for x in dummy_list if x in {2, 3, 5, 7, 11}]

# Key execution point
final_score = evaluate_performance(metric_set, benchmark_weights)
print(f"Result: {final_score}")