data_stream = [12, -5, 8, 17, 3, 21, 0, 9, -4, 15]
offset = 3
adjusted_values = [x + offset for x in data_stream]
threshold = 10
temp_multiplier = 2  # irrelevant variable (distractor)
processed_data = [x * 2 for x in adjusted_values if x % 2 == 0]
filtered_sum = sum([x for x in processed_data if x > threshold])
# Additional irrelevant operation
dummy_count = len([x for x in data_stream if x < 0])
Result: filtered_sum