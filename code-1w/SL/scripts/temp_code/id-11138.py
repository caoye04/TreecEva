data_points = [2, 7, 1, 8, 2, 8, 4, 5]
offset = 3
adjusted_data = [x + offset for x in data_points]
processed_values = [x * 2 for x in adjusted_data if x % 2 == 0]
threshold = 10
filtered_sum = sum([x for x in processed_values if x > threshold])
Result: filtered_sum