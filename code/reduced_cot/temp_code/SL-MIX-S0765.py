import itertools

# Process temperature readings with threshold filtering
readings = [23.5, 19.8, 25.1, 18.2, 27.3, 16.9, 22.7]
temp_threshold = 20.0

# Filter readings above threshold using lambda
filter_func = lambda x: x > temp_threshold
filtered_values = list(filter(filter_func, readings))

# Calculate sum of filtered values
filtered_total = sum(filtered_values)

print(f"Result: {filtered_total}")