data_points = [23, 45, 12, 67, 34, 89, 56]
scaling_factor = 0.5
temp_values = [x * scaling_factor for x in data_points]
processed_data = [int(x) for x in temp_values if x % 2 == 0]
threshold = 20
filtered_sum = sum([x for x in processed_data if x > threshold])
Result: filtered_sum