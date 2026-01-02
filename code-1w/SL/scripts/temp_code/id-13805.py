def transform_sequence(seq, threshold):
    shifted = [x >> 1 for x in seq]
    mapped = list(map(lambda y: y ** 2 if y > threshold else y + 1, shifted))
    return mapped

raw_values = [12, 34, 56, 78, 91]
threshold_limit = 20

converted = [ord(str(x)[-1]) for x in raw_values]
transformed_data = transform_sequence(converted, threshold_limit)

processed_data = transformed_data[1::2]
filtered_sum = sum(processed_data)
print(f"Target result: {filtered_sum}")