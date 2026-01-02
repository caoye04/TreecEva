data_stream = [12, -5, 8, 17, 3, 21, 0, 9, -4, 14]
offset = 3
adjusted_values = [x + offset for x in data_stream]
processed_data = [x * 2 for x in adjusted_values if x % 2 == 0]
threshold = 20
irrelevant_counter = 0
temp_result = 0
for val in processed_data:
    if val < threshold:
        temp_result += val
    else:
        irrelevant_counter += 1
filtered_sum = sum([x for x in processed_data if x > threshold])
print(f"Result: {filtered_sum}")