import math

# Simulated sensor array data from industrial filtration system
raw_readings = [3.2, 1.8, 4.5, 0.9, 2.1, 5.3, 6.7, 2.2, 1.1, 8.8, 3.4, 2.6, 7.1]

timestamp_epochs = [1623456780, 1623456840, 1623456900, 1623456960, 1623457020,
                    1623457080, 1623457140, 1623457200, 1623457260, 1623457320,
                    1623457380, 1623457440, 1623457500]

# Irrelevant calibration coefficients (distractor)
calibration_factors = [0.98, 1.02, 0.99, 1.01, 1.00, 0.97, 1.03, 0.96, 1.04, 0.95, 1.05, 0.94, 1.06]
adjusted_readings = [raw * cal for raw, cal in zip(raw_readings, calibration_factors)]

# Decoy function: looks relevant but unused
def compute_stability_index(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return math.sqrt(variance) if variance > 0 else 0

# Another red herring: temperature drift compensation (never applied)
temperature_log = [22.1, 22.3, 21.9, 22.0, 22.5, 22.7, 23.0, 22.8, 22.6, 22.9, 23.1, 23.3, 23.5]
drift_compensation = [math.exp(-(t - 22.0) * 0.05) for t in temperature_log]

# Critical processing path begins here
status_flags = ['OK', 'OK', 'FAULT', 'OK', 'OK', 'OK', 'OK', 'FAULT', 'OK', 'OK', 'OK', 'OK', 'OK']

# Identify valid sensors based on status and baseline threshold
valid_sensors = []
for i, flag in enumerate(status_flags):
    if flag == 'OK' and raw_readings[i] >= 1.0:
        valid_sensors.append(i)

# Extract readings from valid sensors only
filtered_measurements = []
for idx in valid_sensors:
    filtered_measurements.append(raw_readings[idx])

# Secondary filter: remove outliers beyond 2 standard deviations (recomputed)
mean_filtered = sum(filtered_measurements) / len(filtered_measurements)
std_filtered = math.sqrt(sum((x - mean_filtered) ** 2 for x in filtered_measurements) / len(filtered_measurements))
outlier_threshold = 2 * std_filtered

# Apply outlier removal
final_measurements = [x for x in filtered_measurements if abs(x - mean_filtered) <= outlier_threshold]

# Additional irrelevant transformation: frequency domain analysis (unused)
frequency_components = [math.sin(2 * math.pi * x * 0.1) for x in final_measurements]

# Key assignment - target intervention point
filtration_yield = sum(final_measurements)

# Dead code path: simulation of alternate algorithm (never reached)
if False:
    cumulative_weight = 0
    for reading in adjusted_readings:
        cumulative_weight += reading * 1.15

# Irrelevant aggregation (distractor)
avg_adjusted = sum(adjusted_readings) / len(adjusted_readings)
median_raw = sorted(raw_readings)[len(raw_readings)//2]

# Set operations as required feature: determine overlap between high readings and high timestamps
high_readings_indices = {i for i, v in enumerate(raw_readings) if v > 4.0}
high_time_indices = {i for i, t in enumerate(timestamp_epochs) if t > 1623457200}
common_indices = high_readings_indices & high_time_indices
conflicting_indices = high_readings_indices ^ high_time_indices

# Unused derived metric
consistency_score = len(common_indices) - len(conflicting_indices)

# Print result as required
Result: filtration_yield