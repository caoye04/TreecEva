import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 22.3, 20.9, 26.1, 24.7, 23.0]
humidity_readings = [45, 52, 61, 48, 55, 58, 43, 50, 47]
pressure_readings = [1013, 1015, 1012, 1018, 1014, 1016, 1011, 1017, 1013]

# Irrelevant auxiliary arrays (distractor)
legacy_codes = ['A7', 'B2', 'C9', 'D4', 'E1', 'F8', 'G5', 'H3', 'I6']
station_ids = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009]

# Calibration parameters (only calibration_factor is actually used)
bias_offset = 0.87
scaling_factor = 1.02
noise_floor = 0.05
threshold_limit = 21.5
calibration_factor = 0.93

# Decoy function - appears useful but unused
def legacy_transform(x):
    return [val * 1.1 for val in x if val > 20]

# Auxiliary transformation not part of main logic
inverted_temps = [round(100 / (t + 1), 2) for t in temperature_readings]

# Primary processing pipeline
valid_indices = []
for i, temp in enumerate(temperature_readings):
    if temp >= threshold_limit:
        valid_indices.append(i)

# Masked selection using indices
filtered_data = []
for idx in valid_indices:
    composite_score = (temperature_readings[idx] * 0.6) + (humidity_readings[idx] * 0.3)
    filtered_data.append(composite_score)

# Dead code path - never executed due to prior filtering (red herring)
if len(pressure_readings) < 5:
    adjusted_pressure = [p * scaling_factor for p in pressure_readings]
else:
    dummy_var = sum(pressure_readings) / len(pressure_readings)

# Simulate diagnostic checksum (unused)
diagnostic_sum = 0
for i, val in enumerate(humidity_readings):
    diagnostic_sum += val * (i + 1)

# Core calculation chain
running_total = 0.0
weight_sequence = [0.1, 0.2, 0.4, 0.2, 0.1]  # Weighting for moving average simulation

for i, score in enumerate(filtered_data):
    weighted_contribution = score * weight_sequence[i % len(weight_sequence)]
    running_total += weighted_contribution

# Secondary adjustment using zip and enumerate (critical)
adjustment_accum = 0.0
for j, (temp, humid) in enumerate(zip(temperature_readings, humidity_readings)):
    if j in valid_indices:
        delta = math.sin(math.radians(temp)) * math.log(humid + 1)
        adjustment_accum += delta * (j + 1)

# Final aggregation with decoy variables
baseline = sum(filtered_data) / len(filtered_data)
volatility_index = max(filtered_data) - min(filtered_data)

# Actual answer computation (uses calibration_factor)
intermediate_result = baseline * (1 + (adjustment_accum / 100))
final_diagnostic = round(intermediate_result * calibration_factor, 6)

# Output target variable
print(f"Result: {final_diagnostic}")