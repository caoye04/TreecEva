from itertools import compress

# Sensor data calibration and noise filtering simulation
data_readings = [107, 214, 198, 203, 156, 189, 204, 175, 162, 218]
baseline_threshold = 180
noise_floor = 150

# Identify valid high-intensity readings above threshold
elevated_mask = [x > baseline_threshold for x in data_readings]

# Apply secondary filter to exclude potential noise near floor
stable_mask = [x > noise_floor for x in data_readings]

# Combined mask using logical compression
valid_mask = [e and s for e, s in zip(elevated_mask, stable_mask)]

# Extract clean readings using boolean compression
filtered_data = list(compress(data_readings, valid_mask))

# Final aggregation of validated measurements
filtered_sum = sum(filtered_data)

# Intermediate calculations for system diagnostics (distractor)
avg_reading = sum(data_readings) / len(data_readings)
peak_value = max(data_readings)

# Output result
print(f"Result: {filtered_sum}")