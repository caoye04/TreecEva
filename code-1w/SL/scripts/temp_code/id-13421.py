def normalize(value, min_val, max_val):
    if max_val - min_val == 0:
        return 0.5
    return (value - min_val) / (max_val - min_val)

extra_data = [12, 7, 94, 23, 65]
useless_sum = sum(x ** 0.5 for x in extra_data if x % 2 == 1)

# Simulate sensor readings and performance metrics
temp_readings = [22.1, 23.5, 21.9, 24.0, 22.8]
humidity_levels = [45, 47, 50, 44, 46]
response_times = [120, 98, 135, 110, 102]

# Normalize and pack into dictionary
metrics = {
    'temp_stability': 100 * normalize(min(temp_readings), 20, 30),
    'humidity_optimal': 100 * normalize(max(humidity_levels), 40, 60),
    'latency_efficiency': 100 * (1 - normalize(max(response_times), 80, 150)),
    'sample_count': len(temp_readings)
}

# Weight configuration for evaluation
weights = {
    'temp_stability': 0.4,
    'humidity_optimal': 0.3,
    'latency_efficiency': 0.3
}

# Misleading intermediate calculation
baseline_offset = (metrics['sample_count'] * 5.5) - 12.3
shadow_value = baseline_offset * 0.1  # Unused distractor

# Core logic to compute final score
def evaluate_performance(met, w):
    raw_score = 0
    for key in w:
        if key in met:
            raw_score += met[key] * w[key]
    
    # Apply non-linear boost if all metrics are above threshold
    if all(met[k] >= 70 for k in w):
        raw_score *= 1.1
    
    # Additional check for data completeness
    if met.get('sample_count', 0) >= 5:
        raw_score += 5
    
    return int(raw_score)

# Execute main computation
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Result: {final_score}")