def preprocess_readings(sensor_data):
    normalized = {}
    base_offset = 10
    for key, readings in sensor_data.items():
        adjusted = [x - base_offset for x in readings]
        normalized[key] = [val ** 0.5 if val > 0 else 0 for val in adjusted]
    return normalized

sensor_readings = {
    'temp': [26, 31, 19],
    'pressure': [15, 25, 35],
    'humidity': [20, 45, 10]
}

# Irrelevant transformation (dead-end path)
transformed_metrics = []
for i, (k, v) in enumerate(sensor_readings.items()):
    magnitude = sum(x ** 2 for x in v)
    transformed_metrics.append((i, magnitude))

processed_data = preprocess_readings(sensor_readings)

# Weight assignment with red herring variables
weights = {'temp': 0.5, 'pressure': 0.3, 'humidity': 0.2}

scaling_factor = 2.5
offset_correction = -3
useless_tracker = set()
for idx, key in enumerate(processed_data.keys()):
    temp_val = sum(processed_data[key]) * scaling_factor
    useless_tracker.add((idx, temp_val % 7))

intermediate_results = {}
dummy_aggregate = 0
total_entries = 0

for label, values in processed_data.items():
    raw_sum = sum(values)
    entry_count = len(values)
    total_entries += entry_count
    # Store intermediate but not final result
    intermediate_results[label] = raw_sum * weights[label]
    dummy_aggregate += raw_sum ** 0.1  # Distractor computation

# Real calculation begins here
final_score = 0
for label, weight in weights.items():
    if label in processed_data:
        avg_value = sum(processed_data[label]) / len(processed_data[label])
        contribution = avg_value * weight * 10
        final_score += contribution

# Additional misleading operation (not affecting final_score)
outlier_flags = set()
for k, v in processed_data.items():
    for val in v:
        if val > 3.5:
            outlier_flags.add(k)

# Final irrelevant sort
sorted_intermediates = sorted(intermediate_results.items(), key=lambda x: x[1], reverse=True)

print(f"Result: {final_score}")