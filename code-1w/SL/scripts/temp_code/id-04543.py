import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 24.9, 23.7, 22.4]
humidity_readings = [45, 47, 50, 52, 58, 60, 55, 53, 49]
pressure_readings = [1013, 1012, 1015, 1010, 1008, 1005, 1007, 1011, 1014]

# Irrelevant backup dataset (distractor)
backup_temperatures = [21.3, 22.0, 20.8, 23.1]
legacy_humidity = [44, 46, 48, 51]

# Calibration parameters
calibration_factor = 0.987
offset_adjustment = 0.15
smoothing_window = 3

# Preprocessing: filter out unstable initial readings
filtered_data = []
for i, temp in enumerate(temperature_readings):
    if i >= 2:  # Skip first two as system stabilizes
        adjusted_temp = (temp * calibration_factor) + offset_adjustment
        filtered_data.append(round(adjusted_temp, 2))

# Distractor: unused transformation chain
transformed_humidity = []
for h in humidity_readings:
    normalized = (h - min(humidity_readings)) / (max(humidity_readings) - min(humidity_readings))
    transformed_humidity.append(round(normalized * 100))

# Distractor: dead code path for alternate calibration
if len(temperature_readings) < 5:
    calibration_factor = 1.02
    filtered_data = [t * calibration_factor for t in temperature_readings]

# Real processing begins: compute moving average (relevance)
moving_avg = []
for i in range(len(filtered_data)):
    if i < smoothing_window - 1:
        moving_avg.append(filtered_data[i])
    else:
        window = filtered_data[i - smoothing_window + 1:i + 1]
        moving_avg.append(sum(window) / len(window))

# Distractor: parallel processing of unrelated metric
pressure_trends = []
counter = 0
for p in pressure_readings:
    trend = 'stable'
    if counter > 0:
        if p > pressure_readings[counter - 1]:
            trend = 'rising'
        elif p < pressure_readings[counter - 1]:
            trend = 'falling'
    pressure_trends.append(trend)
    counter += 1

# Auxiliary function with red herring logic
def analyze_variance(data_list):
    mean_val = sum(data_list) / len(data_list)
    squared_diffs = [(x - mean_val) ** 2 for x in data_list]
    variance = sum(squared_diffs) / len(squared_diffs)
    return round(variance, 4)

# Unused variance analysis (distractor)
variance_diagnostics = {
    'temp_var': analyze_variance(filtered_data),
    'humid_var': analyze_variance(transformed_humidity),
    'press_var': analyze_variance(pressure_readings)
}

# Core logic: process readings using zip and enumerate
# Combines filtered data with index-based weighting
def process_readings(readings, factor):
    weighted_sum = 0.0
    total_weight = 0.0
    
    # Use enumerate and zip with dummy padding (real logic)
    padded_readings = readings + [readings[-1]] * 2  # Extend for alignment
    indices = list(range(len(readings)))
    
    for idx, (i, val) in enumerate(zip(indices, readings)):
        # Complex weight calculation with bit manipulation red herring
        base_weight = (idx + 1) * factor
        modifier = 1 + (math.sin(idx * 0.5) ** 2)
        
        # Bitwise distraction (irrelevant to final result)
        binary_flag = (idx & 1) ^ (len(readings) & 1)
        if binary_flag:
            modifier *= 1.05
        
        final_weight = base_weight * modifier
        weighted_sum += val * final_weight
        total_weight += final_weight
    
    # Final aggregation
    if total_weight == 0:
        return 0.0
    return round(weighted_sum / total_weight, 6)

# Secondary distractor function (never called)
def legacy_processing(seq):
    result = 1
    for x in seq:
        result = (result * x) % 17
    return result

# Critical execution point
final_diagnostic = process_readings(filtered_data, calibration_factor)

# Print result as required
print(f"Result: {final_diagnostic}")