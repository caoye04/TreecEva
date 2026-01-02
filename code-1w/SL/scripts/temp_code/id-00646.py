def evaluate_performance(metrics, weights):
    # Normalize metrics to a common scale (0-100)
    normalized = {}
    for k, v in metrics.items():
        if v < 0:
            normalized[k] = 0
        elif v > 100:
            normalized[k] = 100
        else:
            normalized[k] = v

    # Apply weight adjustments based on priority tiers
    adjusted_scores = {}
    tier_map = {'critical': 1.5, 'important': 1.2, 'standard': 1.0}
    criticality_tiers = {
        'latency': 'critical',
        'throughput': 'important',
        'accuracy': 'critical',
        'memory_usage': 'standard',
        'power_efficiency': 'important'
    }

    temp_buffer = []
    for metric_name in weights.keys():
        base_value = normalized.get(metric_name, 0)
        tier_multiplier = tier_map.get(criticality_tiers.get(metric_name, 'standard'), 1.0)
        weighted_val = base_value * weights[metric_name] * tier_multiplier
        adjusted_scores[metric_name] = weighted_val
        temp_buffer.append(weighted_val * 0.1)  # Irrelevant computation

    # Simulate noise filtering
    filtered_noise = sum([x ** 0.5 for x in temp_buffer if x > 0.5])

    # Aggregate final score with bonus logic
    raw_total = sum(adjusted_scores.values())
    bonus_eligible = set()
    for name, score in adjusted_scores.items():
        if score >= 40 and name in ['latency', 'accuracy']:
            bonus_eligible.add(name)

    bonus_points = 0
    if len(bonus_eligible) == 2:
        bonus_points = 15
    elif len(bonus_eligible) == 1:
        bonus_points = 5

    # Final adjustment using set intersection for alignment check
    expected_metrics = {'latency', 'throughput', 'accuracy'}
    provided_metrics = set(metrics.keys())
    alignment_count = len(expected_metrics & provided_metrics)
    alignment_bonus = alignment_count * 3

    # Dead code: unused function call simulation
    def calculate_variance(data):
        mean = sum(data) / len(data)
        return sum((x - mean) ** 2 for x in data) / len(data)

    dummy_data = [12, 45, 67, 23, 89]
    _ = calculate_variance(dummy_data)  # Computation with no effect

    final_score = raw_total + bonus_points + alignment_bonus
    return final_score

# Main execution
metric_set = {
    'latency': 95,
    'throughput': 70,
    'accuracy': 98,
    'memory_usage': 45,
    'power_efficiency': 60
}

benchmark_weights = {
    'latency': 0.3,
    'throughput': 0.25,
    'accuracy': 0.35,
    'memory_usage': 0.05,
    'power_efficiency': 0.05
}

final_score = evaluate_performance(metric_set, benchmark_weights)
print(f"Result: {final_score}")