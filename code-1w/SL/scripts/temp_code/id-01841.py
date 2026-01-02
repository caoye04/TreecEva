def process_data(data, limit):
    filtered = [x for x in data if x > limit]
    indexed = enumerate(filtered)
    transform = lambda i, val: val * (i + 1)
    mapped = [transform(i, v) for i, v in indexed]
    return sum(mapped) // len(mapped) if mapped else 0

values = [12, 7, 15, 3, 9, 14]
thresh = 8
temp_var_ignore = "irrelevant"
result = process_data(values, thresh)
print(f"Target result: {result}")