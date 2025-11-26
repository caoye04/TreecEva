data_points = [15, 23, 8, 42, 17, 31, 56]
scaling_factor = 3
threshold = 20

filtered_data = [x for x in data_points if x > threshold]
processing_buffer = [x + 5 for x in filtered_data]

if len(filtered_data) >= 3:
    target_value = filtered_data[2] * scaling_factor
else:
    target_value = -1

print(f"Target result: {target_value}")