import math

# Sensor calibration constants (irrelevant to final result but looks important)
CALIBRATION_FACTOR_A = 0.872
CALIBRATION_FACTOR_B = 1.045
BASELINE_OFFSET = -0.013

# System thresholds and configuration
threshold_map = {
    'temp': 75.5,
    'pressure': 32.0,
    'vibration': 8.7,
    'humidity': 60.0
}

# Simulated raw sensor data with decoy fields
raw_readings = [
    {'sensor': 'T1', 'temp': 73.2, 'seq': 1001, 'status': 'OK'},
    {'sensor': 'P2', 'pressure': 34.1, 'seq': 1002, 'status': 'WARN'},
    {'sensor': 'V3', 'vibration': 9.1, 'seq': 1003, 'status': 'ALERT'},
    {'sensor': 'H4', 'humidity': 58.3, 'seq': 1004, 'status': 'OK'},
    {'sensor': 'T5', 'temp': 77.3, 'seq': 1005, 'status': 'ALERT'}
]

# Irrelevant transformation: converts readings to string representations
stringify = lambda x: {k: str(v) for k, v in x.items() if k != 'seq'}
stringified_data = [stringify(reading) for reading in raw_readings]

# Decoy function that appears useful but is never called
def calibrate_sensor(data, factor):
    """Applies calibration (not used in main logic)"""
    return {k: v * factor + BASELINE_OFFSET for k, v in data.items() if isinstance(v, (int, float))}

# Auxiliary function to extract numeric sensor values (used)
def extract_metrics(entry):
    metrics = {}
    for key, value in entry.items():
        if key in threshold_map and isinstance(value, (int, float)):
            metrics[key] = value
    return metrics

# Process only relevant fields from raw data
processed_data = []
for reading in raw_readings:
    extracted = extract_metrics(reading)
    if extracted:
        processed_data.append(extracted)

# Another irrelevant utility: computes entropy of status transitions (dead code)
def compute_status_entropy(logs):
    status_seq = [entry['status'] for entry in logs]
    freq = {}
    for s in status_seq:
        freq[s] = freq.get(s, 0) + 1
    entropy = 0
    for count in freq.values():
        p = count / len(status_seq)
        entropy -= p * math.log2(p)
    return round(entropy, 3)

# Unused intermediate calculation (red herring)
status_diversity_index = compute_status_entropy(raw_readings)

# Core analysis logic
anomaly_counter = 0
def analyze_single_reading(reading_dict, thresholds):
    global anomaly_counter
    anomalies = 0
    for sensor_type, value in reading_dict.items():
        if value > thresholds[sensor_type]:
            anomalies += 1
    if anomalies > 0:
        anomaly_counter += 1
    return anomalies

# Higher-order function factory (distractor with plausible use)
def make_validator(ref_value):
    return lambda x: abs(x - ref_value) < 0.5

# Unused validators (decoy closures)
temp_stable = make_validator(73.0)
pressure_stable = make_validator(32.5)

# Main diagnostic engine
anomaly_list = []
for record in processed_data:
    count = analyze_single_reading(record, threshold_map)
    anomaly_list.append(count)

# Bit manipulation red herring: encodes anomaly pattern into bitmask (unused)
anomaly_bitmask = 0
for i, cnt in enumerate(anomaly_list):
    if cnt > 0:
        anomaly_bitmask |= (1 << i)
decoded_flag = bin(anomaly_bitmask).count('1')

# Real computation path begins here — conditional override logic
override_rules = {
    'temp': lambda x: x >= 77.0,  # trigger if temp >= 77.0
    'vibration': lambda x: x > 9.0
}

override_triggered = False
for reading in processed_data:
    for sensor, value in reading.items():
        if sensor in override_rules and override_rules[sensor](value):
            override_triggered = True
            break
    if override_triggered:
        break

# Final diagnostic determination
base_score = len([a for a in anomaly_list if a > 0])
if override_triggered:
    base_score *= 2

# Irrelevant aggregation: average of non-thresholded fields (decoy stat)
all_numeric_values = []
for entry in raw_readings:
    all_numeric_values.extend([v for v in entry.values() if isinstance(v, (int, float)) and v not in threshold_map.values()])
mean_auxiliary = sum(all_numeric_values) / len(all_numeric_values)

# Critical assignment point
final_diagnostic = base_score + int(math.floor(anomaly_counter / 2))

# Output the required result
print(f"Result: {final_diagnostic}")