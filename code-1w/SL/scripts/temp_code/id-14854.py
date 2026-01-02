from collections import defaultdict

# Simulate sensor data with noise and redundancy
data_stream = [
    ('temp', 23.5), ('humidity', 45), ('temp', 24.1), ('pressure', 1013),
    ('humidity', 47), ('temp', 22.9), ('pressure', 1015), ('temp', 24.0),
    ('humidity', 46), ('pressure', 1012), ('temp', 23.8)
]

# Irrelevant backup of raw stream (distractor)
raw_backup = [x for x in data_stream]

# Process and group sensor readings by type
sensor_readings = defaultdict(list)
for sensor_type, value in data_stream:
    sensor_readings[sensor_type].append(value)

# Calculate averages (core logic)
averages = {}
for s_type in sensor_readings:
    avg = sum(sensor_readings[s_type]) / len(sensor_readings[s_type])
    averages[s_type] = round(avg, 2)

# Noise threshold filter - unused but plausible (distractor)
noise_floor = 0.5
def apply_noise_filter(values, floor):
    return [v for v in values if abs(v - sum(values)/len(values)) > floor]

# Simulated calibration offset (semi-relevant but not used directly)
calibration_map = {'temp': -0.2, 'humidity': 1.0, 'pressure': 2}
adjusted_averages = {k: averages[k] + calibration_map[k] for k in averages}

# Weighted contribution factors (some weights are irrelevant)
weight_factors = defaultdict(float)
weight_factors['temp'] = 0.4
weight_factors['humidity'] = 0.3
weight_factors['pressure'] = 0.3
weight_factors['altitude'] = 0.0  # Dead weight (distractor)

# Intermediate score calculation based on adjusted averages
temp_score = (adjusted_averages['temp'] - 20) * 10
humidity_score = max(100 - adjusted_averages['humidity'], 0)
pressure_score = adjusted_averages['pressure'] / 10

# Composite scoring with redundant steps
intermediate_total = temp_score * weight_factors['temp']
intermediate_total += humidity_score * weight_factors['humidity']
intermediate_total += pressure_score * weight_factors['pressure']

# Normalization factor (plausible but overcomplicated)
normalization_constant = sum(weight_factors.values()) or 1
normalized_score = intermediate_total / normalization_constant

# Final nonlinear transformation (key logic step)
def calculate_final_score(score_dict):
    base = normalized_score  # Closure over computed value
    if base > 30:
        return int((base * 1.1) - 5)
    elif base > 20:
        return int(base)
    else:
        return int(base * 0.9)

# Execute final computation
final_score = calculate_final_score(adjusted_averages)

# Print result as required
print(f"Result: {final_score}")