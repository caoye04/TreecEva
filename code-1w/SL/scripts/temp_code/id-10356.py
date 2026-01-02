def analyze_component(metrics, config):
    baseline = config.get('baseline', 1.0)
    scaling = config.get('scaling', 2.0)
    offset = config.get('offset', 0.5)
    adjustment_factor = (scaling + offset) / baseline

    # Irrelevant intermediate calculation (distractor)
    temp_debug = sum([v * 0.1 for v in metrics.values()]) + 42
    debug_mode = temp_debug > 10

    processed = {}
    for k, v in metrics.items():
        if k.startswith('perf_'):
            processed[k] = v * adjustment_factor
        elif k.startswith('mem_'):
            processed[k] = max(v - 0.1, 0.0) * adjustment_factor
    
    # Semi-relevant aggregation
    total_weight = 0.0
    aggregated = 0.0
    weights = {'perf_cpu': 0.6, 'perf_gpu': 0.8, 'mem_main': 0.4, 'mem_cache': 0.2}
    for key, weight in weights.items():
        if key in processed:
            aggregated += processed[key] * weight
            total_weight += weight

    if total_weight > 0:
        aggregated /= total_weight

    # Dead code path (misleading)
    if debug_mode and False:
        fallback = sum(processed.values()) / len(processed)
        return fallback

    return aggregated


def calculate_performance(raw_data):
    # Preprocessing with dictionary operations
    benchmark_data = {}
    for k, v in raw_data.items():
        if isinstance(v, list) and len(v) > 0:
            benchmark_data['perf_' + k] = sum(v) / len(v)
        elif isinstance(v, dict):
            benchmark_data['mem_' + k] = v.get('usage', 0.0) / (v.get('limit', 1.0))

    # Additional irrelevant transformation
    shadow_copy = {k.upper(): v * 1.01 for k, v in benchmark_data.items()}
    outlier_count = len([v for v in shadow_copy.values() if v > 1.5])

    config = {
        'baseline': 0.9,
        'scaling': 1.8,
        'offset': 0.3
    }

    intermediate_result = analyze_component(benchmark_data, config)
    
    # Final logic step: apply non-linear boost if passing threshold
    if intermediate_result >= 0.75:
        boosted = intermediate_result ** 1.5
    else:
        boosted = intermediate_result * 0.9

    # Secondary adjustment based on bitwise characteristic (red herring)
    flag_check = int(boosted * 100) & 7  # Use only lower 3 bits
    if flag_check in [2, 4, 6]:
        final_adjust = 1.05
    else:
        final_adjust = 1.0

    final_score = int((boosted * final_adjust) * 1000)  # Scale to integer score

    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Input data
input_metrics = {
    'cpu': [0.85, 0.91, 0.87],
    'gpu': [0.76, 0.89, 0.92],
    'main': {'usage': 0.72, 'limit': 1.0},
    'cache': {'usage': 0.65, 'limit': 1.0}
}

# Execute
final_score = calculate_performance(input_metrics)