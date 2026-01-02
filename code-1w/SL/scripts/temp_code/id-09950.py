import math

# Sensor calibration constants (used in decoy calculations)
CALIBRATION_FACTOR_A = 0.87
CALIBRATION_FACTOR_B = 1.03
BASELINE_OFFSET = -0.5

# Irrelevant signal smoothing parameters
def smooth_signal(x):
    return [v * 0.9 + 0.1 for v in x]

# Unused noise reduction function
def reduce_noise(data):
    return [d for d in data if abs(d) > 0.1]

# Simulated raw sensor readings (multiple sensors)
raw_readings = {
    'sensor_1': [12, 15, 14, 18, 20, 22, 25],
    'sensor_2': [8, 10, 11, 13, 12, 14, 16],
    'sensor_3': [5, 7, 6, 8, 9, 11, 10],
    'sensor_4': [30, 32, 35, 33, 37, 36, 39]
}

# Misleading intermediate transformation
transformed_readings = {}
for key, values in raw_readings.items():
    transformed_readings[key] = [v ** 0.5 for v in values]

# Dead code path: unused statistical analysis
def compute_statistics(data_dict):
    stats = {}
    for k, v in data_dict.items():
        mean_val = sum(v) / len(v)
        variance = sum((x - mean_val) ** 2 for x in v) / len(v)
        stats[k] = {'mean': mean_val, 'var': variance}
    return stats

# Decoy threshold values (not used in final logic)
threshold_warning = {
    'sensor_1': 16,
    'sensor_2': 13,
    'sensor_3': 8,
    'sensor_4': 34
}

# Actual processing begins here
processed_data = []
for readings in raw_readings.values():
    # Compute moving average of window size 3
    for i in range(2, len(readings)):
        avg = (readings[i-2] + readings[i-1] + readings[i]) / 3
        processed_data.append(round(avg, 2))

# Another layer of irrelevant aggregation
temp_aggregate = {}
for i, val in enumerate(processed_data):
    bucket = i // 5
    if bucket not in temp_aggregate:
        temp_aggregate[bucket] = []
    temp_aggregate[bucket].append(val)

# Real threshold map used in analysis (this one matters)
threshold_map = {
    'critical': 28.0,
    'elevated': 18.0,
    'normal': 10.0
}

# Core analysis logic with distractors
abnormal_count = 0
diagnostic_scores = []

for value in processed_data:
    # Apply fake calibration (doesn't affect result)
    calibrated = value * CALIBRATION_FACTOR_A + BASELINE_OFFSET
    
    # Real condition check using actual thresholds
    if value > threshold_map['critical']:
        diagnostic_scores.append(5)
    elif value > threshold_map['elevated']:
        diagnostic_scores.append(3)
    elif value > threshold_map['normal']:
        diagnostic_scores.append(1)
    else:
        diagnostic_scores.append(0)
    
    # Red herring counter
    if calibrated > 20.0:
        abnormal_count += 1

# Final analysis function with multiple distractions
def analyze_readings(data_list, thresholds):
    score_sum = 0
    peak_magnitude = 0
    fluctuation_index = 0
    
    # Meaningless peak tracking
    for val in data_list:
        if val > peak_magnitude:
            peak_magnitude = val
    
    # Fake fluctuation calculation
    for i in range(1, len(data_list)):
        fluctuation_index += abs(data_list[i] - data_list[i-1])
    
    # ACTUAL scoring logic (depends only on diagnostic_scores from outer scope)
    nonlocal diagnostic_scores
    base_score = sum(diagnostic_scores)
    
    # Apply decay factor that doesn't change integer result
    adjusted = base_score * (1 + 0.1) - 0.5
    
    # Final transformation
    result = int(round(adjusted * 2, 0))
    
    return result

# Execute critical statement
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")