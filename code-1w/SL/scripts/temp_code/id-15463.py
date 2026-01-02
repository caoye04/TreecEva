from itertools import compress

# Sensor data stream with periodic calibration markers
data_stream = [102, 98, 105, 100, 99, 103, 97, 101, 104, 96, 100, 95, 106, 99, 98]
calibration_mask = [i % 3 == 0 for i in range(len(data_stream))]  # Every 3rd reading is a calibration point

# Extract non-calibration sensor readings using boolean masking
valid_readings = list(compress(data_stream, [not x for x in calibration_mask]))

# Process: take last 7 valid readings and apply smoothing by dividing by 1.5
sliced_elements = [x / 1.5 for x in valid_readings[-7:]]

# Final aggregation
filtered_sum = sum(sliced_elements)

# Debug line (irrelevant to final result)
dropped_count = len(data_stream) - len(valid_readings)

Result: filtered_sum