data_sequence = [3, 8, 15, 22, 30, 38, 45]
offset = 2
even_shifted = [val - offset for val in data_sequence]
squared_values = [x**2 for x in even_shifted]
processed_data = [y // 3 for y in squared_values if y % 2 == 0]
threshold = 100
filtered_sum = sum([x for x in processed_data if x > threshold])
print(f"Result: {filtered_sum}")