def calculate_performance(results):
    weights = {'latency': 0.4, 'throughput': 0.35, 'accuracy': 0.25}
    weighted_sum = sum(results[metric] * weight for metric, weight in weights.items())
    return round(weighted_sum, 3)

# Irrelevant auxiliary data (distractor at intervention level 5)
baseline_metrics = {'latency': 120, 'throughput': 85, 'accuracy': 92}
deprecated_flags = [False, True, False]

# Core input data
benchmark_results = {'latency': 95, 'throughput': 97, 'accuracy': 99}

# Computation chain
raw_total = sum(benchmark_results.values())
adjusted_total = raw_total * 0.98 if raw_total > 100 else raw_total
final_score = calculate_performance(benchmark_results)

# Output result as required
print(f"Result: {final_score}")