from itertools import compress

data_stream = '42,57,33,89,12,74,63,28,91'
values = [int(x) for x in data_stream.split(',')]

# Calculate parity flags (irrelevant but plausible)
even_flags = [v % 2 == 0 for v in values]
dummy_result = list(compress(values, even_flags))  # Unused operation

# Key filtering logic: keep values > 50 and < 80
threshold_mask = [(50 < v < 80) for v in values]
filtered_values = list(compress(values, threshold_mask))

# Final computation
filtered_sum = sum(filtered_values)
print(f"Result: {filtered_sum}")