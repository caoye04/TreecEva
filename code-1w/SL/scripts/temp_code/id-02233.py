from itertools import compress

# Sensor readings from structural load test
effective_sensors = [True, False, True, True, False, True]
raw_readings = [120.5, 115.0, 130.2, 128.7, 119.3, 135.8]
baseline_offset = 10.0

# Apply baseline correction and filter malfunctioning sensors
adjusted_weights = []
for i, reading in enumerate(raw_readings):
    corrected = reading - baseline_offset
    if effective_sensors[i]:
        adjusted_weights.append(corrected)

# Final aggregation after filtering and adjustment
total_load = sum(adjusted_weights)
print(f"Result: {total_load}")