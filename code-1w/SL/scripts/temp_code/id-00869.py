def evaluate_performance(metrics, data_map):
    baseline = {x: x * 1.5 for x in range(4, 9)}
    temp_result = 0
    adjustment_factor = 0.85
    outlier_threshold = 120
    scaling_cache = {}

    # Irrelevant precomputation (distractor)
    for i in range(3):
        scaling_cache[i] = (i ** 3) / 2.5

    active_keys = set(baseline.keys()) & metrics
    
    fallback_value = 0
    for k in active_keys:
        if k in data_map and data_map[k] < outlier_threshold:
            raw_val = data_map[k] * adjustment_factor
            if raw_val > 50:
                temp_result += raw_val // 2
            else:
                temp_result += raw_val * 1.2
    
    # Dead code path (misleading)
    unused_list = [x for x in scaling_cache.values() if x > 10]
    ignored_sum = sum(unused_list) * 0.1

    penalty = 0
    if len(active_keys) < 3:
        penalty = 15
    
    # Key computation branch
    if temp_result > 100:
        temp_result *= 0.9
    else:
        temp_result += 20

    final_result = int(temp_result - penalty)
    return final_result

# Main execution
metric_set = {5, 6, 7, 10}
benchmark_data = {5: 48, 6: 55, 7: 62, 8: 130}

intermediate_total = 0
for key in benchmark_data:
    intermediate_total += benchmark_data[key] // 10

# Unused diagnostic calculation (distractor)
diagnostic_ratio = intermediate_total / len(benchmark_data) if benchmark_data else 0

final_score = evaluate_performance(metric_set, benchmark_data)
print(f"Target result: {final_score}")