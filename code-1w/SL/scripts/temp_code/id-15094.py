import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.7]
humidity_readings = [55.2, 58.7, 61.3, 59.8, 62.1, 64.5, 63.0, 60.4]
co2_levels = [415, 423, 418, 430, 435, 440, 425, 432]

# Irrelevant auxiliary variables (distractors)
baseline_offset = 0.87
scaling_factor = 1.02
normalization_constant = 0.995
dummy_counter = 0
placeholder_matrix = [[0]*3 for _ in range(3)]

# Misleading preprocessing path (dead code - never called)
def legacy_calibrate(data):
    return [x * 0.98 + 1.5 for x in data]

def deprecated_filter(stream):
    return [x for x in stream if x > 0]

# Real processing begins here
raw_mixed_signals = []
for i in range(len(temperature_readings)):
    raw_mixed_signals.append(
        temperature_readings[i] * 2.1 + \
        humidity_readings[i] * 0.8 + \
        co2_levels[i] * 0.01
    )

# Apply moving average filter (relevant)
filtered_signal = []
window_size = 3
for i in range(len(raw_mixed_signals)):
    if i < window_size - 1:
        filtered_signal.append(raw_mixed_signals[i])
    else:
        window_avg = sum(raw_mixed_signals[i - window_size + 1:i + 1]) / window_size
        filtered_signal.append(window_avg)

# Compute signal variance (used later)
mean_signal = sum(filtered_signal) / len(filtered_signal)
signal_variance = sum((x - mean_signal) ** 2 for x in filtered_signal) / len(filtered_signal)

# Bit manipulation decoy (irrelevant but looks important)
checksum = 0
for val in co2_levels:
    checksum ^= int(val)
    checksum = (checksum << 1) & 0xFF | (checksum >> 7)

# Destructuring assignment distraction
temp_first, *temp_middle, temp_last = temperature_readings
humidity_first, *humidity_middle, humidity_last = humidity_readings

# Dictionary-based metadata (partly irrelevant)
sensor_metadata = {
    'device_id': 'ENV-207',
    'location': 'Building C, Floor 5',
    'firmware': 'v2.1.8',
    'calibration_date': '2023-11-05',
    'maintenance_interval_days': 90
}

# Unused transformation chain (red herring)
transform_chain = [
    lambda x: x ** 2,
    lambda x: x + 1.5,
    lambda x: math.log(x) if x > 0 else 0
]

# Actual data processing pipeline
normalized_readings = [
    (x - mean_signal) / (math.sqrt(signal_variance) + 1e-8)
    for x in filtered_signal
]

# Threshold detection with short-circuit logic (relevant)
anomaly_flags = []
for val in normalized_readings:
    is_anomalous = False
    is_anomalous = is_anomalous or (val > 1.8)  # Upper threshold
    is_anomalous = is_anomalous or (val < -1.8) # Lower threshold
    anomaly_flags.append(int(is_anomalous))

# Count anomalies using manual loop (instead of sum()) to obscure logic
anomaly_count = 0
for flag in anomaly_flags:
    if flag == 1:
        anomaly_count += 1

# Secondary derived metric (distractor)
effective_range = max(normalized_readings) - min(normalized_readings)

# Real computation feeding into final result
def compute_stability_index(anomalies, total):
    if total == 0:
        return 100.0
    ratio = anomalies / total
    return 100 * (1 - ratio)  # Higher = more stable

stability_index = compute_stability_index(anomaly_count, len(normalized_readings))

# Complex conditional with misleading branches
diagnostic_code = ''
if stability_index >= 90:
    diagnostic_code = 'GREEN'
    recovery_effort = 0
elif stability_index >= 70:
    diagnostic_code = 'YELLOW'
    recovery_effort = 1
else:
    diagnostic_code = 'RED'
    recovery_effort = 3

# Decoy state machine (never executed)
current_state = 'INIT'
state_transition_log = []
for _ in range(5):
    if current_state == 'INIT':
        current_state = 'WAIT'
    elif current_state == 'WAIT':
        current_state = 'PROCESS'
    # ... truncated logic (dead path)

# Main data structure transformation
processed_data = {
    'readings': normalized_readings,
    'flags': anomaly_flags,
    'metrics': {
        'stability': stability_index,
        'variance': signal_variance,
        'anomaly_rate': anomaly_count / len(normalized_readings)
    },
    'diagnostic': diagnostic_code
}

# Final analysis function
def analyze_readings(data_dict):
    base_score = data_dict['metrics']['stability']
    
    # Additional penalty factors
    flag_sum = sum(data_dict['flags'])
    length_factor = len(data_dict['readings'])
    
    # Red herring: unused bitwise combination
    masked_flags = 0
    for f in data_dict['flags']:
        masked_flags = (masked_flags << 1) | f
    masked_flags = masked_flags & 0xFFFF
    
    # Real adjustment
    adjustment = 0
    if data_dict['diagnostic'] == 'YELLOW':
        adjustment = -5
    elif data_dict['diagnostic'] == 'RED':
        adjustment = -15
    
    # Final computation
    intermediate = base_score + adjustment
    final_value = int(intermediate * 1.25)  # Scale and convert to integer
    
    # Dead branch with misleading comment
    # NOTE: This would adjust for humidity drift (but condition never met)
    humidity_drift_compensation = 0
    if False and sensor_metadata['location']:  # Never executes
        humidity_drift_compensation = -2
    
    return final_value + humidity_drift_compensation

# Critical execution point
final_diagnostic = analyze_readings(processed_data)

# Output result as required
print(f"Target result: {final_diagnostic}")