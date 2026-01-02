import math

# Simulated sensor array data from environmental monitoring stations
temperature_readings = [23.4, 19.8, 25.6, 21.0, 27.3, 18.2, 24.1, 26.7, 20.5, 22.9]
humidity_readings = [45, 52, 39, 58, 33, 61, 48, 37, 54, 46]
pressure_readings = [1013, 1021, 1009, 1018, 1005, 1024, 1015, 1008, 1020, 1012]

# Irrelevant auxiliary data (distractor)
sound_levels = [67, 71, 65, 73, 69, 70, 66, 72, 68, 74]  # Decoy sensor data
vibration_data = [0.03, 0.05, 0.02, 0.07, 0.04, 0.06, 0.03, 0.08, 0.05, 0.01]  # Not used

# Configuration parameters
baseline_temp = 20.0
high_temp_threshold = 25.0
low_humidity_threshold = 40
pressure_variation_limit = 15

# Derived metrics (some relevant, some not)
heat_index_estimates = [
    t + 0.5 * h for t, h in zip(temperature_readings, humidity_readings)
]  # Partially misleading metric

dew_point_approximations = [
    t - ((100 - h) / 5) for t, h in zip(temperature_readings, humidity_readings)
]  # Unused calculation

# Identify stations with potential anomalies (complex filtering logic)
anomalous_stations = []
for i in range(len(temperature_readings)):
    is_high_temp = temperature_readings[i] > high_temp_threshold
    is_low_humidity = humidity_readings[i] < low_humidity_threshold
    pressure_deviation = abs(pressure_readings[i] - pressure_readings[0])
    within_pressure_tolerance = pressure_deviation <= pressure_variation_limit

    # Complex condition with short-circuit behavior and mixed logic
    if (is_high_temp or is_low_humidity) and not (is_high_temp and is_low_humidity):
        if i % 2 == 0:  # Artificial constraint (distractor)
            continue  # Skip even-indexed stations (misleading logic)
        anomalous_stations.append(i)

# Filtering only relevant data based on multiple criteria (core logic)
filtered_data = []
for i in range(len(temperature_readings)):
    temp_dev = abs(temperature_readings[i] - baseline_temp)
    if temp_dev > 2.0 and humidity_readings[i] < low_humidity_threshold:
        adjusted_score = (temp_dev * 1.5) + (50 - humidity_readings[i]) * 0.8
        filtered_data.append(adjusted_score)

# Unused transformation path (dead code path - distractor)
if len(anomalous_stations) > 3:
    adjusted_filtered = [x * 0.9 for x in filtered_data if x > 10]
else:
    temp_snapshot = temperature_readings[::2]  # Mid-processing snapshot (unused)
    adjusted_filtered = [x * 1.1 for x in filtered_data]  # Computed but not used

# Threshold configuration for diagnostic analysis
threshold_levels = {
    'warning': 8.5,
    'critical': 12.0,
    'emergency': 15.0
}

# Diagnostic function with internal complexity and red herrings
def analyze_readings(data, thresholds):
    if not data:
        return 0.0
    
    # Internal computations with irrelevant transformations
    squared_values = [x**2 for x in data]  # Distractor computation
    normalized = [x / max(data) for x in data]  # Not used later
    
    # Core aggregation logic
    total_risk = 0.0
    level_counts = {'warning': 0, 'critical': 0, 'emergency': 0}
    
    for val in data:
        if val >= thresholds['emergency']:
            level_counts['emergency'] += 1
            total_risk += val * 3.0
        elif val >= thresholds['critical']:
            level_counts['critical'] += 1
            total_risk += val * 2.0
        elif val >= thresholds['warning']:
            level_counts['warning'] += 1
            total_risk += val * 1.5
    
    # Complex final weighting with conditional modifiers
    multiplier = 1.0
    if level_counts['emergency'] > 0:
        multiplier *= 1.5
    if level_counts['critical'] >= 2:
        multiplier *= 1.3
    if sum(level_counts.values()) == 0:
        multiplier = 0.0
    
    # Final diagnostic score calculation (key result)
    final_score = total_risk * multiplier
    
    # Red herring: secondary index that looks important but isn't returned
    secondary_index = sum(level_counts.values()) + len([v for v in data if v > 10])
    
    return final_score

# Execute core diagnostic (target execution point)
final_diagnostic = analyze_readings(filtered_data, threshold_levels)

# Print result as required
print(f"Target result: {final_diagnostic}")