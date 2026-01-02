def calculate_performance(data):
    weights = {'latency': 0.4, 'throughput': 0.35, 'memory_efficiency': 0.25}
    weighted_sum = 0
    for metric, weight in weights.items():
        raw_value = data.get(metric, 0)
        normalized = max(0, min(100, raw_value))  # clamp to [0, 100]
        weighted_sum += normalized * weight
    
    # Apply non-linear efficiency bonus using lambda
    bonus_fn = lambda x: 5 if x > 90 else (2 if x > 75 else 0)
    bonus = bonus_fn(data['throughput'])
    
    return weighted_sum + bonus

# Simulated benchmark results
test_result = {
    'latency': 87,
    'throughput': 92,
    'memory_efficiency': 68
}

# Distractor variables (minimal interference)
baseline = 75
overhead = 3.2

final_score = calculate_performance(test_result)
print(f"Result: {final_score}")