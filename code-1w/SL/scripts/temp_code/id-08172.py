def calculate_performance(results):
    weighted_scores = [(score * weight) for score, weight in results]
    total_weight = sum(weight for _, weight in results)
    return sum(weighted_scores) / total_weight if total_weight != 0 else 0

# Benchmark data: (accuracy, weight)
benchmark_results = [(0.95, 4), (0.87, 3), (0.92, 5)]

# Secondary metrics (distractor variables)
peak_memory_usage = 1.2  # GB
average_latency = 45      # ms
sample_count = 1000

# Key computation
final_score = calculate_performance(benchmark_results)

# Output result
print(f"Result: {final_score}")