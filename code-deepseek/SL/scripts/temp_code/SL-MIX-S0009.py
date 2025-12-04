data_entries = [15, 22, 38, 45, 51]
processed_entries = []
intermediate_calc = 0

# Process data with enumerate
for index, value in enumerate(data_entries):
    processed_value = value + index * 2
    processed_entries.append(processed_value)
    # Distractor calculation that doesn't affect final result
    intermediate_calc += value * 3

# Additional processing step (distractor)
temp_processing = [x % 10 for x in processed_entries]

# Create enumerated data for final calculation
enumerated_data = []
for idx, val in enumerate(processed_entries):
    enumerated_data.append(idx + val)

# Another distractor operation
preliminary_sum = sum(temp_processing)

# Final analysis calculation
final_analysis_result = sum(enumerated_data) / len(processed_entries)

print(f"Target result: {final_analysis_result}")