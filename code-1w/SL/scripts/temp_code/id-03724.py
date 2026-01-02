from collections import defaultdict, Counter
import math

# Simulated sensor readings over time (real data)
sensor_log = [
    {'id': 'S1', 'values': [23.4, 24.1, 25.0, 26.2, 25.8], 'status': 'active'},
    {'id': 'S2', 'values': [19.5, 18.7, 19.0, 18.2, 17.9], 'status': 'active'},
    {'id': 'S3', 'values': [30.1, 31.3, 29.9, 30.5, 31.0], 'status': 'active'},
    {'id': 'S4', 'values': [22.0, 21.8, 22.5, 23.1, 22.7], 'status': 'maintenance'}
]

# Irrelevant baseline configuration (distractor)
system_baseline = {
    'calibration_offset': 0.05,
    'sampling_rate': 100,
    'units': 'Celsius',
    'version': '2.1.3'
}

# Dead code path: unused function (red herring)
def deprecated_analysis(data):
    return sum(x ** 0.5 for x in data if x > 0) / len(data)

# Unused transformation matrix (misleading)
transform_matrix = [
    [1.0, -0.1, 0.05],
    [0.1, 1.0, -0.05],
    [-0.05, 0.05, 1.0]
]

# Distractor: irrelevant string processing (uses string methods)
device_firmware = "sensor-net-v2.1.3-build-2023"
build_number = device_firmware.split('-')[-1]  # '2023'
firmware_channel = device_firmware[11:17]  # 'v2.1.3'

# Fake checksum validation (dead logic)
def validate_checksum(s):
    return sum(ord(c) for c in s) % 256 == 127

# Unused set operations (distraction)
available_sensors = {'S1', 'S2', 'S3', 'S4', 'S5'}
failed_sensors = {'S0', 'S9'}
potential_sensors = available_sensors.difference(failed_sensors)

# Real processing begins here
recent_readings = []
for entry in sensor_log:
    if entry['status'] == 'active':
        recent_readings.extend(entry['values'])

# Compute statistical profile (relevant)
mean_temp = sum(recent_readings) / len(recent_readings)
temp_variance = sum((x - mean_temp) ** 2 for x in recent_readings) / len(recent_readings)
std_dev = math.sqrt(temp_variance)

# Misleading intermediate (looks important but unused later)
adjusted_mean = round(mean_temp + system_baseline['calibration_offset'], 2)

# Character frequency analysis on IDs (irrelevant but plausible)
id_chars = ''.join(entry['id'] for entry in sensor_log)
char_freq = Counter(id_chars)  # Counts 'S' and digits

# Bit manipulation decoy (seemingly relevant to diagnostics)
def bit_scramble(n):
    n = n ^ (n << 1)
    n = n ^ (n >> 2)
    return n & 0xFFFF

scrambled_ids = [bit_scramble(int(entry['id'][1:])) for entry in sensor_log]

# Complex conditional chain with nesting depth 4 (core logic)
def evaluate_health_score(readings, threshold_std=2.0, min_count=3):
    if len(readings) < min_count:
        return 0
    
    high_stress = 0
    window_size = 3
    for i in range(len(readings) - window_size + 1):
        window = readings[i:i+window_size]
        window_avg = sum(window) / len(window)
        if window_avg > mean_temp + std_dev:
            trend_consistent = True
            for j in range(len(window) - 1):
                if window[j] > window[j+1]:
                    trend_consistent = False
                    break
            if trend_consistent:
                high_stress += 1
    
    return high_stress

# Another dead function (unused)
def legacy_diagnostic(arr):
    count = 0
    for x in arr:
        if x > 25 and math.log(x) > 3:
            count += 1
    return count << 2

# Primary diagnostic logic tree
stress_levels = defaultdict(int)
critical_flags = []

for sensor in sensor_log:
    sensor_id = sensor['id']
    values = sensor['values']
    stress_levels[sensor_id] = evaluate_health_score(values)
    
    # Nested condition with red herring variables
    if len(values) >= 4:
        mid_vals = values[1:-1]
        avg_mid = sum(mid_vals) / len(mid_vals)
        if avg_mid > 24.0:
            # Compute unused entropy-like measure
            counts = Counter(round(v, 0) for v in mid_vals)
            entropy = -sum((cnt/len(counts)) * math.log(cnt/len(counts)) 
                          for cnt in counts.values())
            # This branch sets a flag used later
            critical_flags.append(sensor_id)

# Real aggregation step
aggregate_stress = sum(stress_levels.values())

# Set operation distraction
all_flagged = set(critical_flags)
expected_devices = {'S1', 'S2', 'S3'}
missing_in_action = expected_devices.difference(all_flagged)

# Final computation path
scaling_factor = 1.75
if 'S1' in critical_flags and aggregate_stress > 0:
    base_diagnostic = aggregate_stress * scaling_factor
    
    # Additional adjustment based on variance pattern
    variation_score = 0
    for v in recent_readings:
        if abs(v - mean_temp) > std_dev:
            variation_score += 1
    
    # This is the actual answer computation
    final_diagnostic = int(base_diagnostic * 100 + variation_score * 2.5)
else:
    final_diagnostic = -999

# Decoy print statements (never reached)
# print(f"Legacy code output: {legacy_diagnostic(recent_readings)}")
# print(f"Deprecated analysis: {deprecated_analysis(recent_readings)}")

print(f"Result: {final_diagnostic}")