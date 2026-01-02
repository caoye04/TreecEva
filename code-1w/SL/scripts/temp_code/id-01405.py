def calculate_performance(results):
    weights = [0.2, 0.3, 0.5]
    weighted_sum = sum(r * w for r, w in zip(results, weights))
    return int(weighted_sum)

# Benchmark phases: initialization, processing, output
initialization_phase = 85
processing_phase = 92
output_phase = 78

benchmark_results = [initialization_phase, processing_phase, output_phase]

# Irrelevant distraction: system metadata (minimal interference)
system_info = {"version": "1.2.0", "cores": 4, "uptime": 120}

# Key computation
final_score = calculate_performance(benchmark_results)
print(f"Target result: {final_score}")