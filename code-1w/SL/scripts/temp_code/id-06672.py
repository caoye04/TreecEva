import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 22.3, 20.9, 26.1, 24.7, 23.0]
humidity_readings = [45, 52, 58, 41, 60, 55, 39, 47, 50]
pressure_readings = [1013, 1015, 1010, 1018, 1009, 1014, 1020, 1016, 1012]

# Irrelevant auxiliary arrays (distractor)
legacy_codes = ['A7', 'B2', 'C9', 'D4', 'E1', 'F8', 'G3', 'H6', 'I5']
location_ids = ['LOC-001', 'LOC-002', 'LOC-003', 'LOC-004', 'LOC-005']

# System calibration parameters (some are decoys)
calibration_factor = 1.02
offset_adjustment = -0.15
scaling_exponent = 0.93  # unused in final logic
noise_floor = 0.05          # red herring variable

# Thresholds for anomaly detection (used later)
thresh_temp_high = 25.0
thresh_hum_low = 45
thresh_pressure_stable = 1015

# Distractor function: appears useful but not used
def normalize_legacy(codes):
    return [c.replace('A', 'X').upper() for c in codes if '7' not in c]

# Real processing function with distractions inside
def filter_outliers(data, limit=2):
    mean_val = sum(data) / len(data)
    deviations = [(x - mean_val) ** 2 for x in data]
    variance = sum(deviations) / len(deviations)
    std_dev = variance ** 0.5
    
    # Return filtered data within 'limit' standard deviations
    filtered = [x for x in data if abs(x - mean_val) <= limit * std_dev]
    
    # Decoy manipulation (never used)
    temp_shadow = [x * 1.001 for x in filtered]
    temp_shadow = [round(x, 2) for x in temp_shadow]
    
    return filtered

# Another irrelevant utility (dead code path)
def compress_readings(seq):
    grouped = itertools.groupby(sorted(seq), key=lambda x: int(x))
    return {k: len(list(g)) for k, g in grouped}

# Core transformation function
def map_to_zones(values, high_threshold):
    zones = []
    for val in values:
        if val > high_threshold:
            zones.append('critical')
        elif val == high_threshold:
            zones.append('elevated')
        else:
            zones.append('normal')
    return zones

# Main diagnostic processor
def process_readings(data_list, thresholds):
    temp_data = data_list[0]
    hum_data = data_list[1]
    
    # Apply zone mapping
    temp_zones = map_to_zones(temp_data, thresholds['temp'])
    hum_zones = map_to_zones(hum_data, thresholds['hum'])
    
    # Count critical conditions
    temp_critical_count = temp_zones.count('critical')
    hum_critical_count = hum_zones.count('critical')  # always 0 due to threshold
    
    # Compute composite index
    index_score = 0
    for i in range(len(temp_data)):
        if temp_zones[i] == 'critical':
            index_score += temp_data[i] * 2.1
        elif temp_zones[i] == 'elevated':
            index_score += temp_data[i] * 1.3
        else:
            index_score += temp_data[i] * 0.8
    
    # Final diagnostic calculation
    adjustment_factor = 1.0
    if temp_critical_count > 0:
        adjustment_factor = 0.9
    elif len(temp_data) > 5:
        adjustment_factor = 1.1
    
    # Introduce string-based switch (using string method as required)
    status_flag = 'CRITICAL_ALERT'
    if 'ALERT' in status_flag and status_flag.lower().startswith('crit'):
        adjustment_factor *= 0.95
    
    final_index = index_score * adjustment_factor
    
    # Dead computation branch (misleading)
    shadow_value = final_index
    for _ in range(3):
        shadow_value = (shadow_value + 100) / 1.5
        shadow_value = round(shadow_value, 3)
    
    return int(round(final_index))

# Begin actual execution pipeline
filtered_temps = filter_outliers(temperature_readings, limit=1.5)
filtered_humidity = filter_outliers(humidity_readings, limit=1.8)

# Construct input data structure
filtered_data = [
    [round(t, 2) for t in filtered_temps],
    [h for h in filtered_humidity if h >= 40]  # additional filtering
]

# Build threshold map (note: hum threshold set so no 'critical' occurs)
threshold_map = {
    'temp': thresh_temp_high,
    'hum': 65  # higher than max humidity, so no effect
}

# Add decoy dictionary (irrelevant)
metadata_log = {
    'version': 'v2.1-alpha',
    'checksum': sum([len(x) for x in legacy_codes]),
    'timestamp': 1719865234,
    'active': False
}

# Critical execution point
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")