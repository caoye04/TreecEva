def transform_data(data, limit):
    processed = list(map(lambda x: x ** 2 if x > limit else x + 1, data))
    filtered = [val for val in processed if val % 2 == 0]
    shifted = sum([v >> 1 for v in filtered])
    return shifted

values = [3, 8, 5, 2, 9]
threshold = 6
temp_var = "irrelevant_string"
result = transform_data(values, threshold)
print(f"Result: {result}")