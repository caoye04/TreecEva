def analyze_system_load(base_load, threshold=75):
    # Simulate dynamic load adjustment
    adjusted = base_load + (base_load * 0.1)
    return adjusted if adjusted > threshold else threshold

# System performance metrics (simulated sensor inputs)
sensor_a = 85.0
sensor_b = 67.0
sensor_c = 92.0
sensor_d = 73.0

# Historical baselines (distractor data)
historical_avg = (80.1, 72.3, 88.5, 75.0)
baseline_deviation = sum(abs(h - s) for h, s in zip(historical_avg, [sensor_a, sensor_b, sensor_c, sensor_d]))

# Normalize sensor readings to [0,100] scale using lambda
normalize = lambda x: max(0, min(100, x))
normalized_metrics = [normalize(sensor_a), normalize(sensor_b), normalize(sensor_c), normalize(sensor_d)]

# Weight assignment based on component criticality (some weights are misleading)
weights = {
    'core_a': 0.4,
    'core_b': 0.3,
    'aux_c': 0.15,  # Lower impact
    'aux_d': 0.15   # Lower impact
}

# Irrelevant auxiliary calculation (dead computation path)
temp_buffer = []
for val in normalized_metrics:
    temp_buffer.append(val ** 0.5 * 1.5)
buffer_sum = sum(temp_buffer)  # Not used later

# Apply load analysis to each metric (state tracking with intermediate results)
processed = []
for idx, val in enumerate(normalized_metrics):
    if idx % 2 == 0:
        processed.append(analyze_system_load(val, threshold=80))
    else:
        processed.append(analyze_system_load(val, threshold=70))

# Misleading transformation (not affecting final result)
transformed = list(map(lambda x: x * 1.05 if x > 80 else x * 0.95, normalized_metrics))
dummy_aggregate = sum(transformed) / len(transformed)

# Core aggregation logic
metrics = dict(zip(['core_a', 'core_b', 'aux_c', 'aux_d'], processed))

# Final weighted score computation
def aggregate_performance(mets, wts):
    total_weight = 0.0
    weighted_sum = 0.0
    for key, val in mets.items():
        weight = wts.get(key, 0)
        weighted_sum += val * weight
        total_weight += weight
    return round(weighted_sum / total_weight, 4) if total_weight else 0

final_score = aggregate_performance(metrics, weights)
print(f"Result: {final_score}")