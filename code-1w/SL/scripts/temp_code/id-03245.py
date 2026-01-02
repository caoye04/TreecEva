def analyze_component(metrics, weights):
    weighted_sum = 0
    total_weight = 0
    temp_debug_value = 0
    
    for k, v in metrics.items():
        if k == 'latency':
            temp_debug_value += v * 0.1
        elif k == 'throughput':
            weighted_sum += v * weights[k]
            total_weight += weights[k]
        elif k == 'memory_usage':
            adjusted = max(100 - v, 0)
            weighted_sum += adjusted * weights[k]
            total_weight += weights[k]
        elif k == 'error_rate':
            # Irrelevant branch – never contributes due to weight exclusion
            normalized = 100 * (1 - min(v, 1))
            dummy_accum = normalized ** 0.5
    
    if total_weight > 0:
        return weighted_sum / total_weight
    else:
        return 0

# Simulate benchmark data
dataset_metadata = {
    'samples': 1000,
    'dimensions': 20,
    'sparsity': 0.85
}

benchmark_results = {
    'latency': 45,           # ms
    'throughput': 880,       # ops/sec
    'memory_usage': 76,      # MB
    'error_rate': 0.002      # fraction
}

weight_profile = {
    'throughput': 0.4,
    'memory_usage': 0.6
    # 'latency' and 'error_rate' intentionally excluded from weights
}

intermediate_diagnostic = 0
for key in benchmark_results:
    if key in weight_profile:
        intermediate_diagnostic += len(key)

# Extraneous calculation chain
temp_factor = 0
for i in range(3):
    temp_factor += (i + 1) * 2
scaling_buffer = [x * temp_factor for x in range(4)]  # Unused later

computed_baseline = analyze_component(benchmark_results, weight_profile)

# Secondary analysis with red herring logic
aggregate_flags = []
for val in benchmark_results.values():
    if val > 100:
        aggregate_flags.append(True)
    else:
        aggregate_flags.append(False)

flag_analysis_result = sum([1 for b in aggregate_flags if b]) * 5  # Distractor

# Final performance scoring with conditional adjustment
def calculate_performance(data):
    base = computed_baseline
    bonus = 0
    
    if data['throughput'] > 800:
        bonus += 12
    if data['memory_usage'] < 80:
        bonus += 8
    
    # Complex condition with dictionary lookup and logical chaining
    critical_condition = (
        data.get('latency', 0) < 50 and 
        data.get('error_rate', 1) < 0.01 and 
        len(weight_profile) >= 2
    )
    
    if critical_condition:
        bonus *= 1.5  # Enhanced bonus for stability
    
    return int(base + bonus)  # Cast to integer for final score

final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")