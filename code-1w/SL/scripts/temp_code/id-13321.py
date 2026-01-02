from itertools import compress

# Simulate sensor readings with noise
data_stream = [12, 17, 23, 30, 42, 53, 60, 71, 85, 90]

# Apply calibration offset
adjusted_readings = [x - 2 for x in data_stream]

# Denoise by filtering outliers beyond dynamic threshold
dynamic_threshold = sum(adjusted_readings) / len(adjusted_readings)
processed_values = list(filter(lambda x: x <= dynamic_threshold + 5, adjusted_readings))

# Irrelevant distraction: secondary flag computation (not used in final result)
flag_sequence = [True if x % 4 == 0 else False for x in adjusted_readings]
valid_flags = list(compress(range(len(flag_sequence)), flag_sequence))
other_metric = len(valid_flags)  # Unused distractor

# Key computation step
temp_result = [x * 2 for x in processed_values if x > 0]
filtered_sum = sum(filter(lambda x: (x % 3 == 0) or (x % 5 == 0), temp_result))

print(f"Result: {filtered_sum}")