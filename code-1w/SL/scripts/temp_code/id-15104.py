def calculate_performance(data):
    weights = {'latency': 0.4, 'throughput': 0.35, 'memory_efficiency': 0.25}
    weighted_sum = 0
    for key, value in data.items():
        if key in weights:
            weighted_sum += value * weights[key]
    return round(weighted_sum, 3)

# Benchmark results from system test
test_data = {
    'latency': 85.0,
    'throughput': 92.0,
    'memory_efficiency': 78.0,
    'power_usage': 120.5  # irrelevant metric
}

# Distractor variables (minimal interference)
baseline = 80.0
margin = 5.5
dummy_list = [1, 2, 3]  # unused

final_score = calculate_performance(test_data)
Result: {final_score}