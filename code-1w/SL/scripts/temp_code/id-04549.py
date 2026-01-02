def process_item(x):
    return x ** 2 if x % 2 == 0 else x + 1

transform = lambda lst: [process_item(y) for y in lst]

filter_and_sum = lambda arr: sum([z for z in arr if z > 10])

data = [3, 4, 5, 6, 7]
temp_data = [x * 2 for x in data]  # Distractor: not directly used
processed = transform(data)
result = filter_and_sum(processed)
print(f"Target result: {result}")