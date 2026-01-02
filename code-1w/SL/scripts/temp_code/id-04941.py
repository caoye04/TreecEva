from collections import defaultdict

# Simulate sensor readings with noise and calibration factors
data = [12, 15, 10, 8, 20, 14, 16, 11]
weights = [0.1, 0.3, 0.15, 0.05, 0.2, 0.1, 0.05, 0.05]

# Misleading pre-processing: normalize data (not actually used in final calculation)
normalized_data = [x / sum(data) for x in data]

# Auxiliary structure for tracking metadata (semi-relevant)
sensor_stats = defaultdict(lambda: {'count': 0, 'total': 0})
for i, value in enumerate(data):
    sensor_stats[f'sensor_{i % 4}']['count'] += 1
    sensor_stats[f'sensor_{i % 4}']['total'] += value

# Red herring: compute variance but never use it
mean_data = sum(data) / len(data)
variance = sum((x - mean_data) ** 2 for x in data) / len(data)
std_deviation = variance ** 0.5

# Weighted scoring logic (core computation)
weighted_sum = sum(d * w for d, w in zip(data, weights))

# Additional distraction: simulate calibration adjustments (unused)
calibration_factors = [1.02, 0.98, 1.01, 0.99, 1.03, 0.97, 1.00, 1.01]
adjusted_readings = [d * c for d, c in zip(data, calibration_factors)]

# Secondary scoring path that looks plausible but is not taken
fallback_score = sum(adjusted_readings) / len(adjusted_readings)

# Conditional override that never triggers (dead logic path)
if any(x < 0 for x in data):
    final_score = fallback_score * 0.8
else:
    # Correct path: apply non-linear bonus based on weighted sum
    bonus_factor = 1.0 + (weighted_sum / 100)
    intermediate_score = weighted_sum * bonus_factor
    penalty = 0.05 * sum(1 for x in data if x > 15)  # penalty for high readings
    final_score = intermediate_score - penalty

# Distractor: unused transformation on weights
transformed_weights = [w ** 2 for w in weights]
total_transformed = sum(transformed_weights)

# Output result
print(f"Result: {final_score}")