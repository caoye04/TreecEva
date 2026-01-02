data_sequence = [12, -7, 3, 15, 0, 9, -4, 6]
offset = 5
adjusted_data = [x + offset for x in data_sequence]
processed_data = [x**2 for x in adjusted_data if x % 2 == 0]
threshold = 50
filtered_sum = sum([x for x in processed_data if x > threshold])
Result: filtered_sum