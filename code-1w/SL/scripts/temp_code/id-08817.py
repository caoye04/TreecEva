def process_item(x):
    return x * 2 + 1

filter_threshold = 5
transform = lambda val: val ** 2

raw_values = [1, 3, 4, 6, 7]
processed = []

for item in raw_values:
    if item > filter_threshold:
        processed.append(transform(process_item(item)))

summary = sum(processed)
data = [2, 4, 6]
processor = lambda arr: sum([x * 3 for x in arr])
result = processor(data)
print(f"Target result: {result}")