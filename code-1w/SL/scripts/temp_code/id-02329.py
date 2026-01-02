import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 22.3, 20.9, 26.1, 24.7, 23.0, 21.4]
humidity_readings = [45, 52, 58, 43, 60, 55, 48, 50, 54, 47]
pressure_readings = [1013, 1015, 1012, 1016, 1018, 1011, 1014, 1017, 1010, 1019]

# Irrelevant backup logs (distractor data)
backup_logs = [
    {'timestamp': '2023-05-01T10:00:00Z', 'status': 'OK', 'load': 0.45},
    {'timestamp': '2023-05-01T11:00:00Z', 'status': 'OK', 'load': 0.52},
    {'timestamp': '2023-05-01T12:00:00Z', 'status': 'ERROR', 'load': 0.89},
    {'timestamp': '2023-05-01T13:00:00Z', 'status': 'OK', 'load': 0.33}
]

# Decoy processing function (never called)
def analyze_load_pattern(logs):
    peak_load = max(log['load'] for log in logs)
    recovery_count = sum(1 for i in range(1, len(logs)) if logs[i]['load'] < logs[i-1]['load'])
    return {'peak': peak_load, 'recoveries': recovery_count}

# Auxiliary transformation functions
def normalize(values, base=20.0):
    return [round(v - base, 2) for v in values]

def detect_outliers(data, tolerance=2.0):
    mean_val = sum(data) / len(data)
    std_dev = math.sqrt(sum((x - mean_val) ** 2 for x in data) / len(data))
    return [i for i, x in enumerate(data) if abs(x - mean_val) > tolerance * std_dev]

def apply_calibration(readings, factor=1.02, offset=0.5):
    # Simulate hardware calibration
    return [round(r * factor + offset, 2) for r in readings]

# Real processing begins here
norm_temp = normalize(temperature_readings)
calibrated_humidity = apply_calibration(humidity_readings, factor=0.98, offset=-2.0)
outlier_indices = detect_outliers(norm_temp)

# Filter out outlier positions from all modalities
filtered_data = []
for i in range(len(temperature_readings)):
    if i not in outlier_indices:
        filtered_data.append({
            'temp': round(temperature_readings[i], 2),
            'humidity': calibrated_humidity[i],
            'pressure': pressure_readings[i]
        })

# Threshold configuration map (critical for decision logic)
threshold_map = {
    'temp_high': 25.0,
    'temp_low': 20.5,
    'humidity_optimal': set(range(45, 56)),
    'pressure_stable': slice(1012, 1018)
}

# Additional irrelevant transformations (distractors)
deviation_series = [abs(norm_temp[i]) for i in range(len(norm_temp)) if i % 2 == 0]
rolling_average = [sum(norm_temp[i:i+3]) / 3 for i in range(len(norm_temp)-2)]

# Complex diagnostic processor
state_flags = []
for entry in filtered_data:
    temp_flag = 0
    if entry['temp'] > threshold_map['temp_high']:
        temp_flag = 2
    elif entry['temp'] < threshold_map['temp_low']:
        temp_flag = 1
    
    humidity_set = set([int(entry['humidity'])])
    humidity_match = len(humidity_set & threshold_map['humidity_optimal']) > 0
    
    pressure_slice = pressure_readings[slice(0, len(pressure_readings))]
    pressure_context = pressure_slice[threshold_map['pressure_stable']] if threshold_map['pressure_stable'].stop <= len(pressure_slice) else []
    pressure_stable = entry['pressure'] in pressure_context
    
    # Compute composite state
    state_code = (temp_flag << 2) | (humidity_match << 1) | pressure_stable
    state_flags.append(state_code)

# Secondary transformation on state flags
delta_states = []
for i in range(1, len(state_flags)):
    change = state_flags[i] - state_flags[i-1]
    delta_states.append(abs(change) * 2)

# Final aggregation and diagnostic computation
def process_readings(data_chunk, thresholds):
    base_score = 100
    adjustment = 0
    
    # Use dictionary keys to modify score
    config_keys = list(thresholds.keys())
    for key in config_keys:
        if 'high' in key:
            adjustment += 7
        elif 'low' in key:
            adjustment -= 3
        elif 'optimal' in key:
            adjustment += 5
        elif 'stable' in key:
            adjustment += 4
    
    # Modify based on unique state diversity
    unique_states = len(set(state_flags))
    diversity_bonus = unique_states * 3
    
    # Apply decay for consecutive duplicates (pattern analysis)
    duplicate_penalty = 0
    for i in range(1, len(state_flags)):
        if state_flags[i] == state_flags[i-1]:
            duplicate_penalty += 2
    
    # Final diagnostic value
    result = base_score + adjustment + diversity_bonus - duplicate_penalty
    
    # Dead code path (never executed due to structure)
    if False:
        fallback = 0
        for val in deviation_series:
            fallback += int(val * 10)
        result = fallback if fallback > 0 else result
    
    return int(result)

# Execute critical statement
final_diagnostic = process_readings(filtered_data, threshold_map)
print(f"Target result: {final_diagnostic}")