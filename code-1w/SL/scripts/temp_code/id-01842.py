from itertools import compress

# Simulate sensor readings with some noise
data_stream = [104, 95, 110, 90, 120, 85, 115, 98]

# Threshold condition: valid if reading is above 95 and below 115
clean_mask = [(95 < x < 115) for x in data_stream]

# Extract valid readings using compress
filtered_data = list(compress(data_stream, clean_mask))

# Apply correction factor using lambda
corrected_values = list(map(lambda x: x * 0.98 + 2, filtered_data))

# Final aggregation
filtered_sum = sum(filtered_data)

# Print result as required
print(f"Result: {filtered_sum}")