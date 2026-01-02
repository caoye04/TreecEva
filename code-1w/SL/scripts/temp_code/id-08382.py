def transform_data(values, shift):
    shifted = list(map(lambda x: x + shift, values))
    return sum(shifted[1::2])  # Sum every second element starting from index 1

raw_data = [3, 7, 2, 8, 4, 6]
processed = [x * 2 for x in raw_data if x > 4]
offset = len(raw_data) - len(processed)
result = transform_data(processed, offset)
print(f"Target result: {result}")