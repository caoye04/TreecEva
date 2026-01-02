import math

# Simulated environmental sensor array data (temperature, pressure, humidity)
sensor_readings = [
    [23.4, 1013.25, 45],
    [24.1, 1012.80, 47],
    [19.8, 1015.60, 52],
    [20.2, 1014.90, 50],
    [22.7, 1013.80, 46]
]

# Irrelevant auxiliary metadata
device_metadata = {
    'model': 'ENV-PROBE-X2',
    'firmware': 'v3.4.1',
    'deployment_zone': 'N47.23W122.11',
    'last_calibrated': '2023-11-05'
}

# Decoy processing function with unused side effects
def analyze_stability(data):
    trends = []
    for i in range(1, len(data)):
        delta_t = data[i][0] - data[i-1][0]
        delta_p = data[i][1] - data[i-1][1]
        stability_metric = abs(delta_t * 0.7) + abs(delta_p * 0.3)
        trends.append(stability_metric > 1.0)
    return sum(trends)  # This result is never used

# Unused transformation chain
temperature_log = [entry[0] for entry in sensor_readings]
pressure_log = [entry[1] for entry in sensor_readings]
avg_temp = sum(temperature_log) / len(temperature_log)
avg_press = sum(pressure_log) / len(pressure_log)

temp_deviation_map = list(map(lambda t: round(abs(t - avg_temp), 2), temperature_log))

# Red herring: complex but irrelevant bit manipulation
def generate_diagnostic_key(timestamp_parts):
    key = 0
    for val in timestamp_parts:
        key ^= int(val * 10) << (val % 4)
        key = (key + 17) % 256
    return key

diagnostic_token = generate_diagnostic_key([2023, 11, 5, 14, 30])

# Real computation begins: calibration sequence based on reference values
calibration_sequence = [0.98, 1.02, 0.99, 1.01, 1.00]

# Data slicing for quality window
recent_batch = sensor_readings[-4:]  # Use only last 4 readings

# Linear search for anomalous humidity entry
anomaly_index = -1
for idx, reading in enumerate(recent_batch):
    if reading[2] > 50:
        anomaly_index = idx
        break

# Conditional adjustment path (only one branch is logically active)
adjusted_values = []
if anomaly_index >= 0:
    for i, row in enumerate(recent_batch):
        adj_row = [
            row[0] * calibration_sequence[i+1],
            row[1] / calibration_sequence[i+1],
            row[2] - 2 if i == anomaly_index else row[2]
        ]
        adjusted_values.append(adj_row)
else:
    # Dead code path - never executed given current data
    adjusted_values = [[t*1.1, p*0.9, h] for t, p, h in recent_batch]

# Secondary filtering via string-encoded rules (distractor)
rule_set = "filter_humid adjust_temp scale_press"
active_filters = rule_set.split(' ')

# Apply only temperature and pressure correction using combinatorics-inspired weighting
weights = [math.comb(4, i) for i in range(4)]  # [1, 4, 6, 4]
total_weight = sum(weights)

weighted_temp_sum = sum(weights[j] * adjusted_values[j][0] for j in range(4))
weighted_press_sum = sum(weights[j] * adjusted_values[j][1] for j in range(4))

final_temp = weighted_temp_sum / total_weight
final_press = weighted_press_sum / total_weight

# Primary calculation function that integrates multiple concepts
def calculate_filtration(data_slice, calib):
    # Extract humidity values from original recent batch
    humidities = [row[2] for row in data_slice]
    
    # Simple sorting to find median (robustness measure)
    sorted_humid = sorted(humidities)
    median_humid = sorted_humid[1] if len(sorted_humid) % 2 == 0 else sorted_humid[2]
    
    # Summation with conditional scaling
    base_score = 0
    for i, h in enumerate(humidities):
        if h >= median_humid:
            base_score += h * calib[i+1]  # Skip first calibration factor
        else:
            base_score += h * 0.95
    
    # Bitwise combination of integer components (red herring operation)
    int_part = int(base_score)
    fractional_bits = int((base_score - int_part) * 64)
    masked = (int_part << 2) ^ fractional_bits  # Manipulated but not used directly
    
    # Final adjustment using lambda-sliced transformation
    modifier = lambda x: round(x, 3)
    slice_window = humidities[1:3]
    adjustment_factor = modifier(sum(slice_window) / 2 / 50)  # Normalize to 50%
    
    # Actual answer computation
    filtration_result = base_score * adjustment_factor * (final_temp / 20.0)
    
    return modifier(filtration_result)

# Execution point of interest
filtration_score = calculate_filtration(sensor_data=recent_batch, calibration_sequence=calibration_sequence)

# Target result output
print(f"Target result: {filtration_score}")