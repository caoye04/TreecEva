def transform_strings(items):
    process_func = lambda s: sum(ord(c) for c in s if c.isalpha())
    values = [process_func(item) for item in items]
    return sum(values)

data_items = ['Python', 'Code', 'Benchmark']
processed_total = transform_strings(data_items)
print(f"Result: {processed_total}")