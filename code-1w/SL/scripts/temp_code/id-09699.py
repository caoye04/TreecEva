import math

# Simulated sensor data with noise and metadata
data_stream = [
    {'id': 'S1', 'values': [3.2, 1.8, 4.5, 2.7], 'active': True, 'calib': 0.95},
    {'id': 'S2', 'values': [0.1, -0.3, 0.05, 0.2], 'active': False, 'calib': 1.0},
    {'id': 'S3', 'values': [2.1, 3.3, 2.9, 3.0], 'active': True, 'calib': 0.98},
    {'id': 'S4', 'values': [-1.0, -1.1, -0.9, -1.2], 'active': True, 'calib': 1.05}
]

# Irrelevant calibration function (decoy)
def calibrate_sensor(x):
    return x * 1.02 if x > 0 else x * 0.98

# Unused signal smoothing (dead code path)
def smooth_signal(signal):
    return [sum(signal[i:i+3]) / 3 for i in range(len(signal) - 2)]

# Real processing begins here
threshold_map = {
    'low_noise': lambda x: abs(x) < 0.5,
    'high_signal': lambda x: x > 3.0
}

# Extract active sensors and apply calibration
active_sensors = []
for sensor in data_stream:
    if sensor['active']:
        calibrated = [v * sensor['calib'] for v in sensor['values']]
        active_sensors.append({'id': sensor['id'], 'readings': calibrated})

# Filter data based on high_signal criterion using lambda and enumerate
filtered_data = []
for entry in active_sensors:
    matched_indices = []
    readings = entry['readings']
    for i, val in enumerate(readings):
        if threshold_map['high_signal'](val):
            matched_indices.append(i)
    if matched_indices:
        # Include only first match for complexity
        filtered_data.append({'sensor': entry['id'], 'index': matched_indices[0], 'value': readings[matched_indices[0]]})

# Misleading aggregation (not used in final result)
total_energy = 0
for d in data_stream:
    for v in d['values']:
        total_energy += v ** 2

# Auxiliary transformation using zip and string methods (partial distractor)
labels = ['A', 'B', 'C', 'D', 'E']
indexed_labels = list(zip(range(len(labels)), labels))
dummy_pairs = [(i, l.lower().strip()) for i, l in indexed_labels if l != 'X']

# Core logic hidden among distractions
def analyze_variance(data_list):
    if not data_list:
        return 0.0
    values = [d['value'] for d in data_list]
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return round(variance, 6)

# Secondary processing function
def count_critical_signals(data_list, func):
    count = 0
    for d in data_list:
        if func(d['value']):
            count += 1
    return count

# Main processing pipeline
variance_score = analyze_variance(filtered_data)
critical_count = count_critical_signals(filtered_data, threshold_map['low_noise'])

# Red herring: unused complex structure
signal_matrix = [[0 for _ in range(4)] for _ in range(4)]
for i, d in enumerate(data_stream):
    for j, val in enumerate(d['values']):
        if i == j:
            signal_matrix[i][j] = val ** 2

# Final processing step with key variable
final_output = 0
offset_key = ''.join([label[1].upper() for label in dummy_pairs[:3]])  # Uses string method and zip
offset_val = hash(offset_key) % 100

if variance_score > 0.5:
    final_output = int(variance_score * 10000) + offset_val
else:
    backup_vals = [entry['value'] for entry in filtered_data]
    if backup_vals:
        geometric_mean = math.exp(sum(math.log(abs(v)) for v in backup_vals) / len(backup_vals))
        final_output = int(geometric_mean * 100) - critical_count
    else:
        final_output = -1

# Additional distraction: unused recursive function
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

# Another decoy operation
useless_sum = sum([i for i in range(1, 11) if i % 2 == 0])

# Critical execution point
final_output = process_signals(filtered_data, threshold_map)

# Actual implementation of process_signals (was missing)
def process_signals(data_chunk, config_map):
    temp_result = 0
    for item in data_chunk:
        val = item['value']
        # Apply non-linear transformation
        transformed = math.log(val) * 2 if val > 1 else val / 0.75
        if config_map['high_signal'](transformed):  # Note: uses transformed value
            temp_result += int(transformed ** 2)
        elif not config_map['low_noise'](val):
            temp_result -= 1
    return temp_result + len(data_chunk)

# Print final result
print(f"Result: {final_output}")