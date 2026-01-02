from collections import defaultdict

def calculate_performance(results):
    totals = defaultdict(int)
    weights = {'latency': 0.4, 'throughput': 0.35, 'accuracy': 0.25}
    
    for metric, values in results.items():
        if metric in weights:
            totals[metric] = sum(values) / len(values)
    
    composite = 0
    for metric, avg_val in totals.items():
        composite += avg_val * weights[metric]
    
    adjustment = 1.0
    if totals['accuracy'] > 0.9:
        adjustment = 1.1
    
    final_score = int(composite * adjustment)
    return final_score

# Benchmark data from system tests
benchmark_results = {
    'latency': [120, 110, 115],
    'throughput': [88, 92, 90],
    'accuracy': [0.91, 0.93, 0.90],
    'memory_usage': [512, 520, 518]  # Irrelevant metric (minimal distraction)
}

final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")