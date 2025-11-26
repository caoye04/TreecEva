data_points = [25, 18, 42, 7, 33, 56, 12, 29, 41, 8]
threshold = 20

# Process and filter data
filtered_values = []
processed_indices = []
temp_analysis = []

for idx, value in enumerate(data_points):
    if value > threshold:
        filtered_values.append(value)
        processed_indices.append(idx)
    # Distractor operation - not used in final result
    temp_value = value * 2 - 5
    temp_analysis.append(temp_value)

# Intermediate calculations that don't affect final result
preliminary_sum = sum(data_points[:5])
average_check = preliminary_sum / len(data_points[:5])

# Key operation that determines final result
processed_data = sum(filtered_values) // len(processed_indices)

# More distraction operations
alternate_calc = max(data_points) - min(data_points)
scaled_result = processed_data * 3

# Final assignment
final_result = processed_data

print(f"Result: {final_result}")