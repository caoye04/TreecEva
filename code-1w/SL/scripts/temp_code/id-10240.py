data = [3, 8, 12, 1, 7, 15, 4]
offset = 2
adjusted_data = [x + offset for x in data]
processed_data = [x * 2 for x in adjusted_data if x % 2 == 0]
threshold = 10
filtered_sum = sum([x for x in processed_data if x > threshold])
# Additional unrelated but harmless computation
temp_result = len(data) * 2 - 1
Result: filtered_sum