def transform_values(data):
    shifted = [val + 2 for val in data]
    return [val * 2 for val in shifted]

raw_input = [1, 3, 5, 7, 9, 11]
processed_data = transform_values(raw_input)
dummy_var = [x for x in processed_data if x > 10]  # distraction
irrelevant_counter = 0
for item in dummy_var:
    irrelevant_counter += 1

filtered_sum = sum([x for x in processed_data if x % 3 == 0])
print(f"Result: {filtered_sum}")