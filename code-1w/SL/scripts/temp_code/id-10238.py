def analyze_component(metrics, weights):
    weighted_sum = 0
    normalization_factor = 0
    temp_debug_value = 0

    for key in ['latency', 'throughput', 'accuracy', 'power']:
        if key == 'latency':
            # Invert latency since lower is better
            inverted = 100 / (metrics.get(key, 1) + 1)
            weighted_sum += inverted * weights[key]
            normalization_factor += weights[key]
        elif key == 'throughput':
            adjusted = metrics.get(key, 0) * 1.5
            weighted_sum += adjusted * weights[key]
            normalization_factor += weights[key]
        elif key == 'accuracy':
            # Apply square root to dampen high accuracy benefits
            dampened = metrics.get(key, 0) ** 0.5
            weighted_sum += dampened * weights[key]
            normalization_factor += weights[key]
        elif key == 'power':
            # Higher power consumption reduces score
            penalty = max(0, 10 - metrics.get(key, 0))
            weighted_sum += penalty * weights[key]
            normalization_factor += weights[key]

    # Irrelevant accumulation (dead-end path)
    for i in range(3):
        temp_debug_value += i * 17

    return weighted_sum / max(normalization_factor, 1)


def calculate_redundant_metric(data):
    # This function is called but its result is not used in final_score
    total = 0
    for k, v in data.items():
        if isinstance(v, dict):
            for sub_k, sub_v in v.items():
                total ^= hash(sub_k) % 100
    return total


def calculate_performance(logs):
    config_weights = {
        'latency': 0.4,
        'throughput': 0.3,
        'accuracy': 0.2,
        'power': 0.1
    }

    intermediate_results = {}
    cumulative_bias = 0

    for idx, entry in enumerate(logs['runs']):
        raw_metrics = entry['metrics']
        score = analyze_component(raw_metrics, config_weights)
        intermediate_results[f'run_{idx}'] = round(score, 3)

        # Accumulate bias (not used later)
        cumulative_bias += idx * 0.01

    # Simulate calibration offset (unused)
    calibration_shift = len(intermediate_results) > 5

    # Final aggregation
    valid_scores = [v for v in intermediate_results.values() if v > 0]
    aggregate = sum(valid_scores) / len(valid_scores) if valid_scores else 0

    # Apply non-linear enhancement
    enhanced = (aggregate ** 1.1) * 0.95

    # Red herring: complex dictionary traversal with no impact
    metadata_tree = logs.get('metadata', {})
    debug_sum = 0
    for k1, v1 in metadata_tree.items():
        if isinstance(v1, dict):
            for k2 in v1.keys():
                debug_sum += len(k2) ^ 3

    # Final scoring logic
    base_final = int(enhanced * 10) / 10.0  # Round down to one decimal
    adjustment = len(logs['runs']) >= 3 and enhanced > 40
    final_adjustment = 2.5 if adjustment else -1.2

    final_score = base_final + final_adjustment

    # Output result
    print(f"Result: {final_score}")
    return final_score

# Main execution
benchmark_data = {
    'runs': [
        {'metrics': {'latency': 20, 'throughput': 60, 'accuracy': 0.95, 'power': 8}},
        {'metrics': {'latency': 25, 'throughput': 55, 'accuracy': 0.92, 'power': 9}},
        {'metrics': {'latency': 18, 'throughput': 65, 'accuracy': 0.97, 'power': 7}},
        {'metrics': {'latency': 22, 'throughput': 58, 'accuracy': 0.94, 'power': 8}}
    ],
    'metadata': {
        'device': {'model': 'X27', 'vendor': 'TechNova'},
        'environment': {'temp': 22, 'humidity': 45}
    }
}

# Irrelevant precomputation
redundant_diagnostic = calculate_redundant_metric(benchmark_data)

final_score = calculate_performance(benchmark_data)