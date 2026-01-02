def calculate_performance(results):
    weights = {'latency': 0.4, 'throughput': 0.35, 'accuracy': 0.25}
    weighted_sum = 0.0
    
    for i, (key, value) in enumerate(zip(results.keys(), results.values())):
        if key not in weights:
            continue
        adjustment = 1.0
        if i == 0:  # latency gets a slight penalty if highest
            adjustment = 0.95
        weighted_sum += value * weights[key] * adjustment
    
    return int(weighted_sum)

# Benchmark test results
dummy_data = [1, 2, 3]
offset = len(dummy_data) * 2
benchmark_results = {
    'latency': 85,
    'throughput': 90,
    'accuracy': 95,
    'version': 'v2.1'  # irrelevant field
}

initial_estimate = sum(benchmark_results[k] for k in ['latency', 'throughput', 'accuracy']) // 3
final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")