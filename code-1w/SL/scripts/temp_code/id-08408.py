import math

# Sensor data readings with some noise
data_stream = [12, -5, 8, 15, -3, 9, 0, 7, -1, 11]

# Irrelevant metadata (distractor)
device_id = "SNSR-7X"
location = "Room 2B"

# Process: extract valid positive readings above threshold
valid_readings = [x for x in data_stream if x > 0]
threshold_filtered = [x for x in valid_readings if x >= 7]

# Apply square root transformation to reduce skew
transformed_data = [math.sqrt(x) for x in threshold_filtered]

# Round to nearest integer for discretization
rounded_data = [round(x) for x in transformed_data]

# Remove duplicates using set operation
unique_data = list(set(rounded_data))

# Sort and take middle slice (non-trivial slicing)
ordered_data = sorted(unique_data)
trimmed_slice = ordered_data[1:-1]  # Exclude min and max equivalents

# Final filtering: only even numbers
filtered_data = [x for x in trimmed_slice if x % 2 == 0]

# Critical assignment point
filtered_sum = sum(filtered_data)

print(f"Result: {filtered_sum}")