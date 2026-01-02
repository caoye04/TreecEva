def calculate_performance(results):
    weights = {'latency': 0.4, 'throughput': 0.35, 'accuracy': 0.25}
    weighted_sum = sum(results[metric] * weight for metric, weight in weights.items())
    return round(weighted_sum, 3)

# Benchmark test results
benchmark_results = {
    'latency': 87.5,
    'throughput': 92.0,
    'accuracy': 96.4
}

# Irrelevant auxiliary data (minimal distraction)
legacy_metrics = [78, 81, 85]
config_version = 'v2.1'

final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")