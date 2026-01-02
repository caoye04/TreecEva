from collections import defaultdict, Counter

# Simulated sensor data stream with noise and redundant readings
data_stream = [
    (1, [23.1, 22.9, 23.0, 24.5, 23.2]),
    (2, [25.3, 25.1, 25.2, 26.0, 25.4]),
    (3, [19.8, 19.9, 20.0, 21.5, 19.7]),
    (4, [24.0, 24.2, 24.1, 25.6, 24.3]),
    (5, [26.7, 26.5, 26.8, 27.1, 26.6])
]

# Irrelevant calibration map for unused sensors
sensor_calibrations = {
    'A': lambda x: x * 1.02,
    'B': lambda x: x + 0.15,
    'C': lambda x: x * 0.98
}

# Misleading intermediate variables
baseline_shift = 0.0
redundant_accumulator = 0
noise_floor = 0.05
aggregated_noise = []

# Real processing begins here
valid_sensors = []
temperature_buckets = defaultdict(list)

for idx, readings in data_stream:
    # Filter out spikes using simple threshold (not the main logic)
    clean_readings = [r for r in readings if abs(r - sum(readings)/len(readings)) < 1.0]
    temperature_buckets[idx] = clean_readings
    
    # Determine validity based on variance (actual relevant check)
    mean_val = sum(clean_readings) / len(clean_readings)
    variance = sum((r - mean_val) ** 2 for r in clean_readings) / len(clean_readings)
    if variance < 0.6:
        valid_sensors.append(idx)

# Decoy statistical analysis on irrelevant dimensions
summary_stats = {}
for k, v in temperature_buckets.items():
    summary_stats[k] = {
        'min': min(v),
        'max': max(v),
        'range': max(v) - min(v)
    }
    # Useless transformation
    aggregated_noise.extend([noise_floor * x for x in v if x > 25])

# Character frequency distractor (completely irrelevant)
status_labels = ['OK', 'OK', 'ERROR', 'OK', 'WARNING']
label_counter = Counter(''.join(status_labels))
total_chars = sum(label_counter.values())

# Another red herring: enumerate with zip on unrelated sequences
timestamps = [1001, 1002, 1003, 1004, 1005]
fake_correlation = []
for i, (ts, lbl) in enumerate(zip(timestamps, status_labels)):
    fake_correlation.append(f'{i}-{ts % 100}:{lbl}')

# Core logic hidden among distractions
primary_data = []
for sensor_id in valid_sensors:
    primary_data.extend(temperature_buckets[sensor_id])

# Actual aggregation
aggregate_score = sum(primary_data) / len(primary_data)

# Multiple decoy calculations
phantom_offset = sum(summary_stats[k]['range'] for k in summary_stats) * 0.1
placeholder_value = len(aggregated_noise) * 0.01
offset_value = len(valid_sensors) * 1.5  # Actually used

correction_factor = 1.0
if len(valid_sensors) >= 3:
    correction_factor = 1.2
elif len(valid_sensors) == 2:
    correction_factor = 1.1

# Key statement — answer depends on this
final_diagnostic = aggregate_score * correction_factor + offset_value

# Dead code path (never executed due to logic above)
if False:
    correction_factor *= 0.9
    final_diagnostic = -999

# Print result as required
print(f"Result: {final_diagnostic}")