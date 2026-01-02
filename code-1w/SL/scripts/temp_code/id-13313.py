def transform_data(sequence, shift):
    processed = sequence[shift:] + sequence[:shift]
    mapped = list(map(lambda x: x ** 2 - shift, processed))
    filtered = [val for val in mapped if val > 10]
    return sum(filtered) // len(filtered) if filtered else 0

data = [3, 1, 4, 1, 5, 9, 2, 6]
offset = 3
auxiliary_var = 'ignored string'
temp_result = [x * 2 for x in data]  # distractor computation
result = transform_data(data, offset)
print(f"Target result: {result}")