from itertools import takewhile

# Sensor readings simulation with decay filter
current_readings = [23.5, 24.1, 19.8, 18.7, 25.3, 26.0, 17.5, 22.0]
base_threshold = 20.0
decay_factor = 0.9
adjustment = 1.2

# Irrelevant calibration offset (distractor)
offset_correction = 0.5
filtered_count = 0
threshold_count = 0

for reading in current_readings:
    adjusted_reading = (reading + offset_correction) * decay_factor - adjustment
    if adjusted_reading < base_threshold:
        # Count how many fall below threshold after adjustment
        threshold_count += 1
    else:
        # Exit early when above threshold
        break

Result: threshold_count