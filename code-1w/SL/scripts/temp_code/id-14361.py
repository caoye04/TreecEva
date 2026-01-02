import itertools

# Simulate sensor readings with noise
data_stream = [15, 23, 9, 44, 67, 2, 81, 13, 55, 38]
noise_offset = 5

# Apply noise correction and filter valid signals
adjusted_data = [x - noise_offset for x in data_stream]
smoothed_data = [sum(pair) // 2 for pair in itertools.pairwise(adjusted_data)]
temp_result = [val for val in smoothed_data if val > 0]  # Remove negative values after smoothing

threshold = 25
processed_data = [x + 1 for x in temp_result]  # Final calibration step

filtered_sum = sum([x for x in processed_data if x > threshold])

Result: filtered_sum