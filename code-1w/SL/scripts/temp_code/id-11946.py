data = [7, 2, 9, 1, 5, 8, 3]
offset = 2
processed = [x + offset for x in data]
sorted_data = sorted(processed)
ignored_value = sorted_data[0]
filtered_sum = sum(sorted_data[1::2])
Result: filtered_sum