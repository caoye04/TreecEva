from collections import defaultdict
import math

# Simulated sensor data aggregation (distractor: some values are irrelevant)
sensor_logs = [
    {'node': 'A', 'temp': 45, 'load': 0.78, 'errors': 2},
    {'node': 'B', 'temp': 52, 'load': 0.85, 'errors': 1},
    {'node': 'C', 'temp': 61, 'load': 0.92, 'errors': 3},
    {'node': 'D', 'temp': 58, 'load': 0.77, 'errors': 0}
]

# Irrelevant preprocessing: transforms data but not used in final result
def preprocess_logs(logs):
    result = defaultdict(lambda: [])
    for entry in logs:
        status = 'stable'
        if entry['temp'] > 60:
            status = 'overheating'
        elif entry['load'] > 0.8:
            status = 'high_load'
        result[status].append(entry['node'])
    return dict(result)

preprocessed = preprocess_logs(sensor_logs)  # Dead end: never used

# Decoy function that looks important but is unused
def compute_stability_index(data):
    index = 0.0
    for d in data:
        index += d['temp'] * (1 - d['load'])
    return index / len(data)

# Another red herring: complex but unused transformation
baseline_shift = sum([math.log(1 + e['errors']) for e in sensor_logs])
correction_factor = math.sin(baseline_shift) if baseline_shift > 0 else 0

# Real threshold logic (buried among noise)
thresholds = {
    'max_temp': 60,
    'critical_load': 0.9,
    'error_limit': 2
}

# Core diagnostic logic with subtle dependencies
voltage_readings = [110, 115, 108, 120]
fluctuation = sum(abs(a - b) for a, b in zip(voltage_readings, voltage_readings[1:]))

# Misleading intermediate calculation (not directly related)
avg_voltage = sum(voltage_readings) / len(voltage_readings)
power_risk = 'high' if fluctuation > 15 else 'low'  # Distractor

# Data structure manipulation using lambda and set operations
node_set_a = {entry['node'] for entry in sensor_logs if entry['temp'] > 50}
node_set_b = {entry['node'] for entry in sensor_logs if entry['load'] > 0.8}
overloaded_nodes = node_set_a & node_set_b  # Only B qualifies

# Critical grouping operation using defaultdict (actual path)
health_data = defaultdict(int)
for log in sensor_logs:
    if log['temp'] > thresholds['max_temp']:
        health_data['over_temp'] += 1
    if log['load'] > thresholds['critical_load']:
        health_data['high_load'] += 1
    if log['errors'] > thresholds['error_limit']:
        health_data['excess_errors'] += 1

# Unused alternative metric
total_anomalies = sum(health_data.values()) * correction_factor  # Becomes 0 due to correction_factor

# Key processing function with nested logic
process_metrics = lambda data, limits: (
    1000 + 
    (data['over_temp'] * 150) + 
    (data['high_load'] * 200) - 
    (len(overloaded_nodes) * 50) + 
    (int(math.sqrt(fluctuation)) * 10) if fluctuation > 0 else 0
)

# Final computation — only this matters
final_diagnostic = process_metrics(health_data, thresholds)

# Output required format
print(f"Result: {final_diagnostic}")