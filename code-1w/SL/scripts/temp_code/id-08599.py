import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 26.7, 18.9, 20.2, 24.8, 23.0]
humidity_readings = [45, 50, 60, 55, 40, 38, 62, 58, 48, 52]
pressure_readings = [1013, 1015, 1012, 1018, 1009, 1020, 1011, 1014, 1016, 1010]

# Irrelevant calibration coefficients (distractor)
CALIBRATION_A = 1.002
CALIBRATION_B = 0.997
OFFSET_X = 0.05
OFFSET_Y = -0.03

# Decoy function - looks important but unused
def calibrate_sensor(data, coeff):
    return [x * coeff for x in data]

# Another decoy: historical baseline (misleading reference)
historical_avg_temp = 21.5
historical_avg_humidity = 52

# Distractor: unused transformation matrix
transform_matrix = [
    [0.8, 0.2],
    [0.3, 0.7]
]

# Linear search for anomalies above threshold (relevant)
def find_anomalies(data, threshold):
    indices = []
    for i in range(len(data)):
        if data[i] > threshold:
            indices.append(i)
    return indices

# Filtering logic with list comprehension (relevant)
above_threshold_idx = find_anomalies(temperature_readings, 24.0)
filtered_data = [temperature_readings[i] for i in above_threshold_idx if humidity_readings[i] < 55]

# Dead code path - never executed (red herring)
DEBUG_MODE = False
if DEBUG_MODE:
    print("Debug: Entering diagnostic mode")
    for val in filtered_data:
        print(f"Raw value: {val}")

# Bit manipulation decoy - looks computational but irrelevant
def hash_code(value):
    shifted = int(value) << 3
    xor_val = shifted ^ 0xFF
    masked = xor_val & 0xFFFF
    return masked

# Unused list of hashed values (distractor)
hashed_temperatures = [hash_code(temp) for temp in temperature_readings]

# Core processing with lambda and list comprehension (relevant)
baseline_correction = lambda x: round(x - historical_avg_temp, 2)
corrected_readings = [baseline_correction(val) for val in filtered_data]

# Complex conditional aggregation (3-level nesting)
aggregated_diagnostic = 0
for val in corrected_readings:
    if val > 0:
        if val < 2.0:
            aggregated_diagnostic += val * 1.5
        else:
            aggregated_diagnostic += val * 0.8
    else:
        aggregated_diagnostic -= abs(val) * 0.3

# Secondary processing chain with sorting (relevant but indirect)
sorted_readings = sorted(corrected_readings)
median_index = len(sorted_readings) // 2
median_corrected = sorted_readings[median_index] if len(sorted_readings) % 2 == 1 else \
    (sorted_readings[median_index-1] + sorted_readings[median_index]) / 2

# Final computation - key statement
final_diagnostic = int(aggregated_diagnostic + (median_corrected * 10))

# Red herring: unused exponential smoothing
ALPHA = 0.3
def smooth_data(series):
    if not series:
        return []
    smoothed = [series[0]]
    for i in range(1, len(series)):
        smoothed.append(ALPHA * series[i] + (1 - ALPHA) * smoothed[-1])
    return smoothed

# Never called - dead code path
smoothed_results = smooth_data([1, 2, 3])  # dummy call to avoid linter

# Print result as required
Result: final_diagnostic