def evaluate_performance(metrics, data_config):
    base_threshold = 85
    adjustment_factor = 0.9
    temp_result = 0
    secondary_cache = []

    # Irrelevant precomputation (distractor)
    for i in range(3):
        temp_result += (i * base_threshold) % 7
        secondary_cache.append(temp_result * 0.5)

    # Core logic begins: metric evaluation using set operations and conditions
    required_metrics = {'latency', 'throughput', 'accuracy', 'power_efficiency'}
    optional_metrics = {'memory_footprint', 'startup_time', 'idle_draw'}
    provided_metrics = set(metrics.keys())

    completeness_ratio = len(provided_metrics & required_metrics) / len(required_metrics)
    bonus_count = len(provided_metrics & optional_metrics)

    score = 0
    if completeness_ratio == 1:
        score += 40
        tier_bonus = 10 if bonus_count >= 2 else 5 if bonus_count == 1 else 0
        score += tier_bonus
    else:
        score += int(completeness_ratio * 30)

    # Additional scoring based on data thresholds (nested logic)
    critical_values = []
    for k, v in metrics.items():
        if k == 'latency' and v < data_config['latency']['target']:
            score += 15
        elif k == 'throughput' and v >= data_config['throughput']['min']:
            score += 12
        elif k == 'accuracy' and v >= data_config['accuracy']['threshold']:
            score += 18
        elif k == 'power_efficiency' and v > data_config['power_efficiency']['optimal']:
            score += 10

        # Collecting values for no real purpose (dead path)
        if v > 0:
            critical_values.append(v ** 0.5)

    # Misleading transformation chain
    transformed_scores = [score // (i + 1) for i in range(3)]
    decayed = sum(transformed_scores) * adjustment_factor
    final_score = int(round(decayed))

    # Unused debug print simulation (irrelevant)
    debug_payload = {"raw": score, "adjusted": decayed, "components": transformed_scores}
    payload_size = len(str(debug_payload))

    return final_score

# Configuration setup
benchmark_data = {
    'latency': {'target': 10},
    'throughput': {'min': 100},
    'accuracy': {'threshold': 0.92},
    'power_efficiency': {'optimal': 80}
}

metric_set = {
    'latency': 8,
    'throughput': 120,
    'accuracy': 0.95,
    'power_efficiency': 88,
    'memory_footprint': 45,
    'idle_draw': 12
}

# Execution point of interest
final_score = evaluate_performance(metric_set, benchmark_data)
print(f"Result: {final_score}")