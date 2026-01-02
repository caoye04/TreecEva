import itertools

# Simulate sensor readings with some noise
data_stream = [3, -1, 4, 1, 5, -2, 6, -3, 2]

# Define a lambda to classify valid sensor readings (positive and > 2)
is_valid_reading = lambda x: x > 2

# Use itertools.filterfalse to get invalid readings (for system logging, not used in final result)
invalid_readings = list(itertools.filterfalse(is_valid_reading, data_stream))

# Filter only valid readings for processing
cleaned_data = list(filter(is_valid_reading, data_stream))

# Apply scaling factor to valid readings using map and lambda
calibrated_readings = list(map(lambda x: x * 1.5, cleaned_data))

# Further filter readings above threshold for final analysis
filtered_data = [x for x in calibrated_readings if x >= 4.5]

# Compute final aggregated result
filtered_sum = sum(filtered_data)

# Log intermediate count (distraction - not affecting result)
log_count = len(invalid_readings)

print(f"Result: {filtered_sum}")