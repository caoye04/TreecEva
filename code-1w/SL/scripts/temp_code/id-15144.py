from collections import defaultdict

# Simulate sensor data with some noise and redundancy
data = {
    'sensor_A': [12, 15, 14, 0, 13, 16, 14],
    'sensor_B': [9, 0, 11, 10, 10, 0, 12],
    'sensor_C': [20, 18, 19, 0, 21, 20, 18]
}

# Weights for final calculation (some are red herrings)
weights = {
    'A': 0.4,
    'B': 0.3,
    'C': 0.2,
    'D': 0.1  # Unused weight - distractor
}

# Auxiliary tracking structure (semi-relevant)
reading_counts = defaultdict(int)
for key, readings in data.items():
    for r in readings:
        reading_counts[key] += 1 if r > 0 else 0  # Ignore zero readings

# Precompute averages, excluding zero (invalid) readings
averages = {}
for sensor, readings in data.items():
    non_zero = [r for r in readings if r > 0]
    avg = sum(non_zero) / len(non_zero) if non_zero else 0
    averages[sensor] = avg

# Misleading intermediate: normalize to max (not used in final score)
normalized = {}
max_avg = max(averages.values())
for k, v in averages.items():
    normalized[k] = v / max_avg

# Secondary metric: variance (calculated but not used)
variances = {}
for sensor, readings in data.items():
    non_zero = [r for r in readings if r > 0]
    if len(non_zero) > 1:
        mean_val = sum(non_zero) / len(non_zero)
        variances[sensor] = sum((x - mean_val) ** 2 for x in non_zero) / len(non_zero)
    else:
        variances[sensor] = 0

# Weight mapping for active sensors
weight_map = {'sensor_A': 'A', 'sensor_B': 'B', 'sensor_C': 'C'}

# Core logic: compute final weighted score based on averages
weighted_sum = 0
total_weight = 0
for sensor_name, avg_value in averages.items():
    if sensor_name in weight_map:
        weight_key = weight_map[sensor_name]
        if weight_key in weights:
            weighted_sum += avg_value * weights[weight_key]
            total_weight += weights[weight_key]

# Dead code path: hypothetical adjustment (never triggered in this input)
if 'sensor_D' in data:
    extra_bonus = 5.5
    weighted_sum += extra_bonus
else:
    extra_bonus = 0  # Defined but unused

# Final score normalization only if total weight > 0
final_score = weighted_sum / total_weight if total_weight > 0 else 0

# Print result for verification
print(f"Result: {final_score}")