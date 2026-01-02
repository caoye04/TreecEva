data_stream = [3, 1, 4, 1, 5, 9, 2, 6]

# Normalize data by scaling values above threshold
dynamic_offset = 0.5
adjusted_data = [x + dynamic_offset for x in data_stream]

# Extract magnitude information
magnitude_data = [abs(int(x)) for x in adjusted_data]

# Sort and trim outliers (first and last elements)
sorted_values = sorted(magnitude_data)

# Compute sum excluding minimum and maximum values
filtered_sum = sum(sorted_values[1:-1])

# Irrelevant tracking variable (minimal distraction)
count_valid = len([v for v in sorted_values if v > 2])

print(f"Result: {filtered_sum}")