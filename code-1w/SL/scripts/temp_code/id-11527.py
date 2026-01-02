data_points = [12, -5, 8, 17, 3, 21, 0, 9]
offset = 3
processed_data = [x + offset for x in data_points]
threshold = 10
temp_var = [y for y in processed_data if y % 2 == 0]  # irrelevant filtering (distractor)
filtered_sum = sum([x for x in processed_data if x > threshold])
Result: filtered_sum