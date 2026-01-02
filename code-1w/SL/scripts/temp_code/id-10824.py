data_input = [12, -5, 8, 17, 3, 21, 0, 9]
offset = 3
adjusted_data = [x + offset for x in data_input]
processed_data = [x * 2 for x in adjusted_data]
threshold = 20
irrelevant_counter = 0
for val in processed_data:
    if val < 0:
        irrelevant_counter += 1
filtered_sum = sum([x for x in processed_data if x > threshold])
print(f"Result: {filtered_sum}")