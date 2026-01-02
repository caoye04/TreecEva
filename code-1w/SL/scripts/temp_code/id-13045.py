def transform_value(x):
    if x < 0:
        return abs(x) * 2
    elif x % 3 == 0:
        return x + 10
    else:
        return x - 5

# Sensor calibration data (irrelevant to final result)
calibration_offsets = {'sensor_a': 0.5, 'sensor_b': -0.3, 'sensor_c': 1.2}
active_sensors = ['sensor_a', 'sensor_b']
baseline = sum(calibration_offsets[s] for s in active_sensors if s in calibration_offsets)

# Simulated raw diagnostic readings
raw_readings = [12, -7, 0, 15, 9, -3]

# Irrelevant transformation chain
temp_adjusted = []
for val in raw_readings:
    temp_val = val * 1.1
    if temp_val > 10:
        temp_val -= 2
    temp_adjusted.append(int(temp_val))

# Real processing begins here
processed_data = []
for reading in raw_readings:
    processed = transform_value(reading)
    if processed > 10:
        processed_data.append(processed)

# Threshold configuration map (used in final analysis)
threshold_map = {
    'critical': 20,
    'warning': 10,
    'info': 5
}

# Decoy statistical summary (never used)
summary_stats = {
    'count': len(raw_readings),
    'peak': max(raw_readings),
    'trough': min(raw_readings),
    'range': max(raw_readings) - min(raw_readings),
    'median_guess': sorted(raw_readings)[len(raw_readings)//2]
}

# Auxiliary function that looks important but isn't called
def compute_variance(data):
    mean = sum(data) / len(data)
    squared_diffs = [(x - mean)**2 for x in data]
    return sum(squared_diffs) / len(data)

# Another decoy: historical comparison (unused)
historical_avg = 8.4
variance_ratio = None
if baseline > 0:
    variance_ratio = (baseline / historical_avg) * 100

# Core analysis logic
def analyze_readings(readings, thresholds):
    count_critical = 0
    count_warning = 0
    
    for r in readings:
        if r >= thresholds['critical']:
            count_critical += 1
        elif r >= thresholds['warning']:
            count_warning += 1
    
    # Complex scoring with distractor math
    base_score = count_critical * 7 + count_warning * 3
    adjustment = len(readings) % 4  # Minor tweak
    
    # Dead code path (looks like it affects result)
    if base_score > 25:
        adjustment -= 2  # Never reached
    elif base_score == 0:
        adjustment = 0
    
    # Actual computation
    final_score = base_score + adjustment
    
    # Additional irrelevant mapping
    diagnostic_level = 'green'
    if final_score > 15:
        diagnostic_level = 'amber'
    if final_score > 25:
        diagnostic_level = 'red'
    
    # Final red herring: unused bitwise mix
    magic_constant = 0xABC
    masked_score = final_score ^ magic_constant
    masked_score = masked_score & (magic_constant >> 2)
    
    return final_score  # Only this matters

# Execution point of interest
final_diagnostic = analyze_readings(processed_data, threshold_map)

print(f"Result: {final_diagnostic}")