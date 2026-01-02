from collections import defaultdict, Counter

# Simulate sensor data with noise and redundant readings
data_stream = [
    (1, 10), (2, 15), (1, 12), (3, 8), (2, 14), (1, 11), (4, 20), (3, 9), (2, 16), (1, 10)
]

# Irrelevant backup timestamps (distractor)
timestamps_backup = [1623450000 + i*30 for i in range(len(data_stream))]

# Aggregate sensor readings by ID
data_aggregate = defaultdict(list)
for sensor_id, reading in data_stream:
    data_aggregate[sensor_id].append(reading)

# Compute average per sensor (semi-relevant)
avg_readings = {sid: sum(readings) / len(readings) for sid, readings in data_aggregate.items()}

# Misleading normalization factor (not used in final result)
normalization_factor = max(avg_readings.values()) / min(avg_readings.values()) if avg_readings else 1.0

# Identify outlier sensors based on variance (distractor computation)
variances = {}
for sid, readings in data_aggregate.items():
    mean_val = sum(readings) / len(readings)
    variances[sid] = sum((x - mean_val) ** 2 for x in readings) / len(readings)

# Flag sensors with high variance (dead code path - never used)
noisy_sensors = [sid for sid, var in variances.items() if var > 2.0]

# Preprocess: only keep sensors with even IDs (key filtering step)
filtered_data = {sid: data_aggregate[sid] for sid in data_aggregate if sid % 2 == 0}

# Flatten readings from filtered sensors
flattened_readings = [val for readings in filtered_data.values() for val in readings]

# Compute frequency of each reading value (semi-relevant)
reading_freq = Counter(flattened_readings)

# Weighted contribution based on frequency and value (intermediate step)
weighted_contrib = sum(val * freq ** 0.5 for val, freq in reading_freq.items())

# Secondary adjustment using XOR-based checksum of keys (distractor)
checksum = 0
for key in data_aggregate.keys():
    checksum ^= int(key * 10)
adjustment = checksum & 15  # Use only lower 4 bits

# Simulated environmental correction factor (irrelevant constant computation)
correction_factor = sum(k * v for k, v in zip(avg_readings.keys(), avg_readings.values())) / 100 if avg_readings else 0

# Final processing: scale weighted_contrib by adjustment, but only if length conditions match
length_flag = len(flattened_readings) >= 3

processed_data = {
    'base_value': weighted_contrib,
    'modifier': adjustment if length_flag else 1,
    'noise_level': len(noisy_sensors),  # Unused field
    'valid_sensors': len(filtered_data)
}

# Core calculation function
def calculate_final_score(data):
    base = data['base_value']
    mod = data['modifier']
    # Additional irrelevant check
    if data['valid_sensors'] > 0:
        base *= 1.1
    return int(base * mod)

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")