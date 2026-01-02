from itertools import compress

# Sensor data calibration and filtering process
data_readings = [105, 203, 98, 110, 250, 95, 115, 205, 300]
threshold = 100

# Apply basic calibration adjustment
calibrated_readings = [x - 5 for x in data_readings]

# Generate filter mask: keep values within acceptable range (100-200)
valid_range_mask = [(100 <= x <= 200) for x in calibrated_readings]

# Extract valid readings using itertools.compress
filtered_data = list(compress(calibrated_readings, valid_range_mask))

# Final aggregation step
total_count = len(data_readings)
discard_count = total_count - len(filtered_data)
filtered_sum = sum(filtered_data)

print(f"Result: {filtered_sum}")