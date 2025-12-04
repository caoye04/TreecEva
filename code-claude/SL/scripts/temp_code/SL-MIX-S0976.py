import itertools

# Sensor readings from a temperature monitoring system
temperature_data = [22.5, 23.1, 22.8, -99.9, 23.2, -99.9, 22.7, 23.0]

# Filter out error values (represented as -99.9) and calculate statistics
valid_data = [t for t in temperature_data if t > 0]

# Process data with a calibration offset
calibration = 0.3
processed_data = [round(t - calibration, 1) for t in valid_data]

# Get the most frequent values using itertools
value_counts = itertools.groupby(sorted(processed_data))
frequent_values = [k for k, g in value_counts if len(list(g)) >= 1]

# Extract a slice of the processed data for analysis
analysis_slice = processed_data[1:4]

# Calculate sum of filtered data
filtered_sum = sum(processed_data)

print(f"Result: {filtered_sum}")