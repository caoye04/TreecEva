from itertools import combinations

# Sensor calibration data (irrelevant to final result)
base_offsets = {'A': 0.5, 'B': -0.3, 'C': 1.2}
calibration_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# Simulated raw sensor readings (some relevant, some not)
raw_readings = [
    (100, 'temp', 23.5), (101, 'pressure', 1013.2), (102, 'temp', 24.1),
    (103, 'humidity', 45), (104, 'temp', 22.8), (105, 'co2', 410)
]

# Irrelevant transformation: pressure unit conversion
pressure_readings = [r for r in raw_readings if r[1] == 'pressure']
converted_pressure = [round(p[2] * 0.000987, 3) for p in pressure_readings]

# Relevant data extraction and filtering
relevant_tags = ['temp', 'humidity']
filtered_readings = [r for r in raw_readings if r[1] in relevant_tags]
sorted_readings = sorted(filtered_readings, key=lambda x: x[0])

# Extract temperature values only for processing
temp_readings = [r[2] for r in sorted_readings if r[1] == 'temp']

# Dead code path: unused statistical computation
if len(temp_readings) > 5:
    rolling_avg = sum(temp_readings[-3:]) / 3
else:
    rolling_avg = None  # Never used

# Destructuring assignment (partially irrelevant)
first_temp, *middle_temps, last_temp = temp_readings

# Threshold configuration (critical for analysis)
threshold_map = {
    'temp_high': 23.0,
    'temp_low': 22.0,
    'humidity_optimal': (40, 60)
}

# Data window slicing for trend analysis
window_size = 2
overlapping_windows = [
    temp_readings[i:i+window_size] 
    for i in range(len(temp_readings) - window_size + 1)
]

# Count upward trends in temperature
upward_trends = 0
for window in overlapping_windows:
    if len(window) == 2 and window[1] > window[0]:
        upward_trends += 1

# Unused combination generator (distractor)
all_pairs = list(combinations(temp_readings, 2))
divergent_pairs = [(a, b) for a, b in all_pairs if abs(a - b) > 1.0]

# Processed data structure (key input to final function)
processed_data = {
    'readings': temp_readings,
    'count': len(temp_readings),
    'first': first_temp,
    'last': last_temp,
    'trend_score': upward_trends
}

# Decoy function that is never called
def compute_stability_metric(data):
    if not data:
        return 0.0
    variance = sum((x - sum(data)/len(data))**2 for x in data) / len(data)
    return round(1 / (1 + variance), 4)

# Core analysis logic (used)
def analyze_readings(data_dict, thresholds):
    readings = data_dict['readings']
    trend = data_dict['trend_score']
    high_thresh = thresholds['temp_high']
    low_thresh = thresholds['temp_low']
    
    # Count readings above high threshold
    high_count = sum(1 for r in readings if r > high_thresh)
    low_count = sum(1 for r in readings if r < low_thresh)
    
    # Bit manipulation red herring
    encoded_flag = (high_count << 2) ^ (low_count)
    if encoded_flag & 0x8:  # Check if fourth bit is set
        pass  # No effect
    
    # Primary diagnostic logic
    if high_count >= 2 and trend >= 2:
        severity = 3
    elif high_count >= 1 and trend >= 1:
        severity = 2
    else:
        severity = 1
    
    # Final computation: inject humidity status
    humidity_val = [r[2] for r in raw_readings if r[1] == 'humidity'][0]
    min_hum, max_hum = thresholds['humidity_optimal']
    hum_normal = 1 if min_hum <= humidity_val <= max_hum else 0
    
    # Critical calculation: linear combination
    final_score = (severity * 100) + (hum_normal * 50) + (upward_trends * 10)
    
    # Dead branch based on impossible condition
    if first_temp == 999:
        final_score -= 1000
    
    return final_score

# Execute main analysis
final_diagnostic = analyze_readings(processed_data, threshold_map)
print(f"Target result: {final_diagnostic}")