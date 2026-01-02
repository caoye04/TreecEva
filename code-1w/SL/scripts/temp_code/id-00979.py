from collections import defaultdict
import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 22.3, 20.0, 26.7, 24.8]
humidity_readings = [45, 52, 61, 48, 55, 59, 43, 50]
pressure_readings = [1013, 1015, 1012, 1018, 1014, 1016, 1011, 1017]

# Irrelevant auxiliary data (distractor)
auxiliary_codes = ['A7', 'B2', 'C9', 'D4', 'E1', 'F8', 'G5', 'H3']
lookup_matrix = [[1, 0, -1], [2, 1, 0], [-1, 1, 2]]

# Data aggregation with red herring transformations
raw_bundle = {
    'temp': temperature_readings,
    'humid': humidity_readings,
    'press': pressure_readings
}

# Misleading normalization function (unused)
def normalize_sensor_data(data):
    return [round((x - min(data)) / (max(data) - min(data)), 3) for x in data]

# Decoy transformation chain
decoy_normalized = [round(x * 1.02, 1) for x in temperature_readings]  # Slight perturbation
adjusted_humid = [h + 3 if h < 50 else h - 2 for h in humidity_readings]

# Actual processing begins here — key logic interwoven with noise
status_flags = []
for i in range(len(temperature_readings)):
    if temperature_readings[i] > 24.0:
        status_flags.append('HIGH_TEMP')
    elif humidity_readings[i] > 55:
        status_flags.append('HIGH_HUMID')
    else:
        status_flags.append('NORMAL')

# Distractor: unused flag counter
counter_log = defaultdict(int)
for flag in status_flags:
    counter_log[flag] += 1

# Real filtering logic buried among decoys
outlier_indices = []
for i, temp in enumerate(temperature_readings):
    if abs(temp - sum(temperature_readings) / len(temperature_readings)) > 2.0:
        outlier_indices.append(i)

# Remove outliers from all modalities (correct path)
filtered_temp = [temperature_readings[i] for i in range(len(temperature_readings)) if i not in outlier_indices]
filtered_humid = [humidity_readings[i] for i in range(len(humidity_readings)) if i not in outlier_indices]
filtered_press = [pressure_readings[i] for i in range(len(pressure_readings)) if i not in outlier_indices]

# Construct composite data structure (relevant)
filtered_data = []
for i in range(len(filtered_temp)):
    entry = {
        't': filtered_temp[i],
        'h': filtered_humid[i],
        'p': filtered_press[i]
    }
    filtered_data.append(entry)

# Threshold configuration map (critical for final computation)
threshold_map = {
    't_upper': 24.5,
    't_lower': 20.5,
    'h_critical': 57
}

# Auxiliary calculation with misleading intermediate (red herring)
weighted_index = 0
for i, val in enumerate(filtered_temp):
    weighted_index += val * (i + 1)
weighted_index = round(weighted_index / len(filtered_temp), 2)  # Not used later

# Secondary decoy: pressure trend analysis (irrelevant)
pressure_deltas = [filtered_press[i+1] - filtered_press[i] for i in range(len(filtered_press)-1)]
pressure_trend = 'STABLE'
if all(d >= 0 for d in pressure_deltas):
    pressure_trend = 'RISE'
elif all(d <= 0 for d in pressure_deltas):
    pressure_trend = 'FALL'

# Core diagnostic processor (uses t and h only)
def process_readings(data_list, thresholds):
    high_temp_count = 0
    high_humid_count = 0
    balanced_count = 0
    
    for record in data_list:
        t_flag = False
        h_flag = False
        
        if record['t'] > thresholds['t_upper']:
            t_flag = True
        elif record['t'] < thresholds['t_lower']:
            t_flag = True
            
        if record['h'] > thresholds['h_critical']:
            h_flag = True
        
        if t_flag and h_flag:
            high_temp_count += 1
            high_humid_count += 1
        elif t_flag:
            high_temp_count += 1
        elif h_flag:
            high_humid_count += 1
        else:
            balanced_count += 1
    
    # Final diagnostic score computed as a weighted combination
    severity_score = (high_temp_count * 3) + (high_humid_count * 2) - (balanced_count * 1)
    
    # Apply logarithmic compression if score exceeds threshold (non-linear adjustment)
    if severity_score > 5:
        severity_score = int(math.log(severity_score) * 10)
    
    return severity_score

# Critical execution point
final_diagnostic = process_readings(filtered_data, threshold_map)

# Output result as required
print(f"Target result: {final_diagnostic}")