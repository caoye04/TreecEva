data_sequence = [x for x in range(-15, 16)]
processed_data = [x ** 2 for x in data_sequence if x % 2 != 0]
normalized_data = [y - 100 for y in processed_data]
selection_condition = len(processed_data) > 10
filtered_data = normalized_data[::2] if selection_condition else normalized_data[1::2]
filtered_sum = sum(filtered_data)
print(f"Result: {filtered_sum}")