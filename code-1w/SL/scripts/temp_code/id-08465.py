from collections import defaultdict

# Simulate sensor data with noise and validity flags
data_stream = [
    {'id': 1, 'value': 15, 'valid': True},
    {'id': 2, 'value': 25, 'valid': False},
    {'id': 1, 'value': 18, 'valid': True},
    {'id': 3, 'value': 40, 'valid': True},
    {'id': 2, 'value': 22, 'valid': True},
    {'id': 1, 'value': 14, 'valid': True},
    {'id': 3, 'value': 44, 'valid': True}
]

# Track occurrences and totals per sensor
reading_count = defaultdict(int)
total_readings = defaultdict(float)
validity_log = []
redundant_sum = 0

for entry in data_stream:
    reading_count[entry['id']] += 1
    if entry['valid']:
        total_readings[entry['id']] += entry['value']
        validity_log.append(True)
    else:
        validity_log.append(False)

# Compute average per sensor
avg_readings = {}
for sensor_id in total_readings:
    avg_readings[sensor_id] = total_readings[sensor_id] / reading_count[sensor_id]

# Misleading intermediate calculations (distractors)
outlier_threshold = 20
high_value_sensors = [sid for sid, avg in avg_readings.items() if avg > outlier_threshold]
scaling_factor = len(high_value_sensors) if high_value_sensors else 1

# Simulate calibration offset
baseline_offset = 5
adjusted_values = {k: v - baseline_offset for k, v in avg_readings.items()}

# Normalize adjusted values using conditional expression
max_adj = max(adjusted_values.values()) if adjusted_values else 1
normalized_scores = {k: (v / max_adj) * 100 for k, v in adjusted_values.items()}

# Dead code path - never executed but looks relevant
temporary_debug = None
if False:
    temporary_debug = sum(normalized_scores.values())

# Auxiliary computation that seems important but isn't directly used
total_valid_entries = sum(1 for x in data_stream if x['valid'])
redundant_sum = sum(total_readings.values()) + total_valid_entries

# Core logic: weight scores by frequency and normalize
weight_map = {sid: count / len(data_stream) for sid, count in reading_count.items()}
weighted_score = sum(normalized_scores[sid] * weight_map[sid] for sid in normalized_scores)

# Final processing function
threshold_check = lambda x: x if x > 30 else 0
filtered_score = sum(threshold_check(v) for v in normalized_scores.values())

def calculate_final_score(data):
    base = weighted_score * 0.7
    bonus = filtered_score * 0.3
    return int(base + bonus)

# Processed data structure (real input to function)
processed_data = {
    'norm': normalized_scores,
    'weights': weight_map,
    'meta': {'total': len(data_stream), 'valid': len(validity_log)}
}

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")