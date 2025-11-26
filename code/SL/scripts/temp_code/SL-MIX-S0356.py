data_values = [12, 8, 15, 23, 7, 19]
threshold = 10

# Filter values above threshold
filtered_values = [x for x in data_values if x > threshold]

# Create some intermediate calculations (distractor)
intermediate_sum = sum(data_values)
intermediate_count = len(data_values)

# Process data with transformations
processed_data = [x % 7 + 2 for x in filtered_values]

# Unused calculation that seems relevant but isn't
unused_calculation = intermediate_sum // intermediate_count

# Another distractor operation
dummy_operation = [x * 2 for x in data_values if x < threshold]

# Final calculation
final_result = sum([x * y for x, y in zip(filtered_values, processed_data)])

print(f"Result: {final_result}")