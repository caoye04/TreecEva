import itertools

# System health monitoring simulation with diagnostic computation

# Sensor input data (simulated)
sensor_a_readings = [1.2, 0.9, 1.4, 1.1, 0.8]
sensor_b_readings = [2.1, 1.8, 2.3, 2.0, 1.7]
sensor_c_readings = [0.5, 0.6, 0.4, 0.5, 0.7]

# Irrelevant auxiliary data (distractor)
temp_log = [23.5, 24.1, 22.9, 23.7, 24.0]
humidity_data = [45, 47, 44, 46, 48]

# Preprocessing: normalize sensor readings using min-max scaling
def normalize(data):
    min_val, max_val = min(data), max(data)
    if max_val == min_val:
        return [0.5 for _ in data]
    return [(x - min_val) / (max_val - min_val) for x in data]

normalized_a = normalize(sensor_a_readings)
normalized_b = normalize(sensor_b_readings)
normalized_c = normalize(sensor_c_readings)

# Misleading intermediate calculation (dead path)
avg_normalized = [(a + b + c) / 3 for a, b, c in zip(normalized_a, normalized_b, normalized_c)]
spurious_index = sum(avg_normalized) * 0.1  # Unused later

# Compute moving average over normalized sensor B (distraction)
def moving_average(data, window=2):
    return [sum(data[i:i+window]) / window for i in range(len(data) - window + 1)]

ma_sensor_b = moving_average(normalized_b)

# Core logic: detect anomalies in sensor C and compute anomaly score
anomaly_threshold = 0.45
anomalies_detected = [val > anomaly_threshold for val in normalized_c]
anomaly_count = sum(anomalies_detected)

# Simulate conditional escalation based on pattern clustering
consecutive_anomalies = 0
max_consecutive = 0
for is_anomalous in anomalies_detected:
    if is_anomalous:
        consecutive_anomalies += 1
        max_consecutive = max(max_consecutive, consecutive_anomies)
    else:
        consecutive_anomalies = 0

# Weighted contribution from each sensor (only A and B are actually used)
sensor_a_weight = 0.3
sensor_b_weight = 0.5
sensor_c_weight = 0.2  # Not used due to low reliability

weighted_a = sum(normalized_a) * sensor_a_weight
weighted_b = sum(ma_sensor_b) * sensor_b_weight * 1.1  # Boost for responsiveness

# Aggregate score from relevant sensors
aggregate_score = weighted_a + weighted_b

# Secondary processing: derive correction factor using bit manipulation (red herring)
raw_status_code = 0b110101
shifted_code = raw_status_code << 2
inverted_code = shifted_code ^ 0b11111111
parity_check = bin(inverted_code).count('1') % 2
correction_factor = 1.05 if parity_check == 0 else 0.95

# Offset determined via itertools combinatorial analysis (seemingly complex but deterministic)
combinations = list(itertools.combinations([1, 2, 3, 4], 3))
combination_sum = sum(sum(combo) for combo in combinations)
offset_value = combination_sum * 0.01

# Dead code branch — never executed (distractor)
if len(temp_log) < 3:
    emergency_override = True
    fallback_mode = "ACTIVE"
else:
    emergency_override = False
    fallback_mode = "STANDBY"  # This is irrelevant

# Critical execution point
final_diagnostic = aggregate_score * correction_factor + offset_value

print(f"Result: {final_diagnostic}")