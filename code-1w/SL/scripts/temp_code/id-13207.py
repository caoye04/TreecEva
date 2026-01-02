def calculate_performance(data, weights):
    weighted_sum = sum(data[key] * weights.get(key, 0) for key in data)
    normalization_factor = sum(weights.values())
    return round(weighted_sum / normalization_factor, 3)

# Irrelevant auxiliary metric (distractor)
baseline_adjustment = 0.95

# Core metrics and weights
metrics = {
    'accuracy': 0.92,
    'latency': 0.81,
    'throughput': 0.88,
    'energy_efficiency': 0.76
}

weight_map = {
    'accuracy': 4,
    'latency': 2,
    'throughput': 3,
    'energy_efficiency': 1
}

# Additional unused variable (minor distraction)
optimization_log = []

final_score = calculate_performance(metrics, weight_map)
print(f"Result: {final_score}")