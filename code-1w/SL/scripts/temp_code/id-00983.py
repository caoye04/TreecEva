import math

# Simulated sensor data from multiple environmental monitoring stations
temperature_readings = [23.4, 19.5, 27.8, 22.1, 31.0, 18.9, 25.3, 24.7, 20.2]
humidity_readings = [45, 53, 38, 60, 33, 58, 41, 47, 50]
pressure_readings = [1013, 1009, 1015, 1020, 1005, 1018, 1012, 1014, 1007]
wind_speed_readings = [12.5, 8.3, 15.1, 6.7, 18.2, 9.4, 11.0, 13.6, 7.8]

# Irrelevant calibration constants (distractor)
CALIBRATION_OFFSET_A = 0.023
CALIBRATION_OFFSET_B = -0.041
REFERENCE_VOLTAGE = 3.3
NOISE_FLOOR_DB = 45.6

# Misleading intermediate calculations (red herring)
total_samples = len(temperature_readings)
avg_temp = sum(temperature_readings) / total_samples
avg_humidity = sum(humidity_readings) / total_samples
variance_pressure = sum((p - 1013) ** 2 for p in pressure_readings) / total_samples
dew_point_estimate = [round(h * (237.7 * math.log(h / 100)) / (237.7 - math.log(h / 100)), 2) 
                        for h in humidity_readings if h > 0]  # unused later

# Threshold configuration for anomaly detection (critical)
threshold_map = {
    'temp': {'min': 20.0, 'max': 26.0},
    'humidity': {'min': 40, 'max': 55},
    'wind': {'min': 7.0, 'max': 14.0}
}

# Data alignment and preprocessing (relevant)
sensor_data = list(zip(temperature_readings, humidity_readings, wind_speed_readings))
indexed_data = [(i, t, h, w) for i, (t, h, w) in enumerate(sensor_data)]

# Filtering logic based on dual criteria (relevant + distractor)
valid_indices = []
filtered_data = []
for idx, t, h, w in indexed_data:
    meets_temp = threshold_map['temp']['min'] <= t <= threshold_map['temp']['max']
    meets_humidity = threshold_map['humidity']['min'] <= h <= threshold_map['humidity']['max']
    meets_wind = threshold_map['wind']['min'] <= w <= threshold_map['wind']['max']
    
    # Composite condition with short-circuiting (relevant)
    if meets_temp and (meets_humidity or meets_wind):  # note: OR creates wider inclusion
        valid_indices.append(idx)
        filtered_data.append({'index': idx, 'temp': t, 'humidity': h, 'wind': w})
    
    # Dead code path - unreachable due to logic above (distractor)
    if False:
        fallback_value = math.sin(w) * math.cos(t)
        normalized = (t - avg_temp) / (max(temperature_readings) - min(temperature_readings))

# Unused transformation function (decoy)
def transform_coordinates(data_list):
    """Irrelevant geospatial transformation."""
    return [(d[1]*0.01, d[2]*0.02) for d in data_list]

# Unused statistical function (decoy)
def compute_rolling_average(values, window=3):
    """Simulate time-series smoothing."""
    if len(values) < window:
        return []
    return [sum(values[i:i+window]) / window for i in range(len(values)-window+1)]

# Core processing function with embedded logic chain
def analyze_variance(dataset):
    if not dataset:
        return 0.0
    temps = [entry['temp'] for entry in dataset]
    mean = sum(temps) / len(temps)
    squared_diffs = [(x - mean) ** 2 for x in temps]
    variance = sum(squared_diffs) / len(squared_diffs)
    return round(variance, 3)

# Secondary metric calculation (partially relevant)
def count_extreme_conditions(dataset):
    high_wind = sum(1 for d in dataset if d['wind'] > 13.0)
    low_humidity = sum(1 for d in dataset if d['humidity'] < 45)
    return high_wind * 2 + low_humidity  # weighted count

# Main processing pipeline
status_flags = []
for i, entry in enumerate(filtered_data):
    flag = 0
    if entry['temp'] > 24.0:
        flag |= 1
    if entry['humidity'] > 48:
        flag |= 2
    if entry['wind'] > 12.0:
        flag |= 4
    status_flags.append(flag)

# Bit manipulation analysis (relevant concept)
aggregated_flag = 0
for f in status_flags:
    aggregated_flag ^= f  # XOR accumulation

# Auxiliary diagnostic score (irrelevant)
baseline_score = 0
for reading in temperature_readings:
    if reading > 25:
        baseline_score += int(reading) % 3

# Final diagnostic computation (key statement)
def process_readings(data, thresholds):
    if not data:
        return -1
    
    # Step 1: Variance analysis
    variance_metric = analyze_variance(data)
    
    # Step 2: Extreme condition weighting
    severity_weight = count_extreme_conditions(data)
    
    # Step 3: Flag-based adjustment
    adjustment_factor = bin(aggregated_flag).count('1')  # number of set bits
    
    # Step 4: Length scaling
    size_factor = len(data) * 10
    
    # Step 5: Final composition (deterministic)
    result = int(size_factor + severity_weight * 7 - variance_metric * 5 + adjustment_factor * 3)
    
    # Dead code with misleading comment (distractor)
    # NOTE: Previous version used exponential scaling (deprecated)
    #       Kept for backward compatibility checks
    #       DO NOT USE: exp_component = math.exp(-variance_metric)
    
    return result

# Execute key statement
temp_snapshot = [x for x in temperature_readings]  # irrelevant copy
final_diagnostic = process_readings(filtered_data, threshold_map)
print(f"Target result: {final_diagnostic}")