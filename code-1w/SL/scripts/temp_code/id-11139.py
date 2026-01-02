data_sequence = [24, 57, 13, 81, 46, 93, 68, 102]

# Preprocess: apply transformation to each element
doubled_data = [num * 2 for num in data_sequence]
offset_data = [val - 10 for val in doubled_data]
processed_data = [item + 1 for item in offset_data]

# Filtering condition applied on transformed values
filtered_sum = sum([x for x in processed_data if x % 3 == 0])

print(f"Result: {filtered_sum}")