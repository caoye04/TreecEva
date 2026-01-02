from itertools import compress

data_stream = [12, -5, 8, 17, -22, 4, 9, 11]
threshold_mask = [x > 0 and x % 2 == 0 for x in data_stream]

# Apply filtering using itertools.compress
decoded_values = list(compress(data_stream, threshold_mask))

# Additional transformation: square each valid reading
corrected_readings = [val**2 for val in decoded_values]

# Extract final subset based on secondary condition
filtered_values = [v for v in corrected_readings if len(str(v)) == 2]

filtered_sum = sum(filtered_values)
print(f"Result: {filtered_sum}")