data = [3, 8, 15, 22, 30, 11, 7, 16]
offset = 5
adjusted_data = [x + offset for x in data]
processed_data = [y * 2 for y in adjusted_data if y % 2 == 0]
threshold = 30
filtered_sum = sum([x for x in processed_data if x > threshold])
Result: filtered_sum