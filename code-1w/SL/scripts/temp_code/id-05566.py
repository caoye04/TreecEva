from collections import defaultdict, Counter

# Simulated sensor log entries with noise and irrelevant fields
log_entries = [
    {'sensor': 'temp_01', 'value': 98, 'status': 'OK', 'timestamp': '2023-04-01T10:00:00', 'calibration': 0.95},
    {'sensor': 'temp_02', 'value': 102, 'status': 'OK', 'timestamp': '2023-04-01T10:01:00', 'calibration': 0.98},
    {'sensor': 'temp_01', 'value': 97, 'status': 'OK', 'timestamp': '2023-04-01T10:02:00', 'calibration': 0.95},
    {'sensor': 'pressure_x', 'value': 210, 'status': 'ERR', 'timestamp': '2023-04-01T10:03:00', 'calibration': 1.02},
    {'sensor': 'temp_02', 'value': 104, 'status': 'OK', 'timestamp': '2023-04-01T10:04:00', 'calibration': 0.98},
    {'sensor': 'flow_z', 'value': 85, 'status': 'OK', 'timestamp': '2023-04-01T10:05:00', 'calibration': 1.05},
    {'sensor': 'temp_01', 'value': 103, 'status': 'OK', 'timestamp': '2023-04-01T10:06:00', 'calibration': 0.95},
    {'sensor': 'vibration_a', 'value': 190, 'status': 'WARN', 'timestamp': '2023-04-01T10:07:00', 'calibration': 0.99}
]

# Irrelevant helper that looks important but isn't used in critical path
def analyze_trend(data_list):
    trend_score = 0
    for i in range(1, len(data_list)):
        trend_score += (data_list[i] - data_list[i-1]) * 0.5
    return round(trend_score, 2)

# Decoy function that processes unrelated metrics
def compute_health_index(entries):
    warnings = [e for e in entries if e['status'] == 'WARN']
    errors = [e for e in entries if e['status'] == 'ERR']
    return len(warnings) * 10 + len(errors) * 50

# Unused transformation map (red herring)
sensor_multiplier = defaultdict(lambda: 1.0, {
    'temp_01': 1.05,
    'temp_02': 1.03,
    'pressure_x': 0.98
})

# Another decoy: advanced calibration matrix not actually applied
calibration_matrix = {
    'temp_01': lambda x: x * 1.1 if x > 100 else x * 0.9,
    'temp_02': lambda x: x * 1.07,
    'default': lambda x: x * 1.0
}

# Real processing begins here
valid_sensors = ['temp_01', 'temp_02']

# Filter only temperature sensors with OK status
filter_data = lambda logs: [
    entry for entry in logs 
    if entry['sensor'] in valid_sensors and entry['status'] == 'OK'
]

# Misleading aggregation that seems useful but is unused
temp_snapshot = {}
for entry in log_entries:
    if 'temp' in entry['sensor']:
        temp_snapshot[entry['sensor']] = temp_snapshot.get(entry['sensor'], 0) + entry['value']

# Critical transformation pipeline
processed_values = []

def process_readings(filtered_logs):
    raw_values = [entry['value'] for entry in filtered_logs]
    calib_values = [int(v * 0.95) for v in raw_values]  # Apply uniform correction
    
    # Compute moving threshold based on first two values
    if len(calib_values) > 2:
        threshold = (calib_values[0] + calib_values[1]) // 2
    else:
        threshold = calib_values[0] if calib_values else 0
    
    # Apply conditional amplification
    amplified = []
    for v in calib_values:
        if v > threshold:
            amplified.append(v * 2 + 1)
        elif v == threshold:
            amplified.append(v + 10)
        else:
            amplified.append(v * 3)
    
    # Use Counter to find most frequent adjusted reading
    freq_map = Counter(amplified)
    mode_val = max(freq_map, key=lambda x: freq_map[x])
    
    # Final diagnostic derived from mode and length
    base_diagnostic = mode_val % 100
    length_factor = len(amplified) ** 2
    final_diagnostic = base_diagnostic * 2 + length_factor
    
    # Dead code branch: never reached due to logic above
    if False and len(amplified) == 0:
        fallback = sum(raw_values) // len(raw_values)
        final_diagnostic = fallback * 10
    
    # Unused intermediate: looks like it's part of output but isn't
    outlier_count = sum(1 for v in amplified if v > 200)
    
    return final_diagnostic

# Execute processing chain
filtered_logs = filter_data(log_entries)
final_diagnostic = process_readings(filtered_logs)

# Print result as required
print(f"Target result: {final_diagnostic}")