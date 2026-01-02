from itertools import compress

data_stream = [12, 15, 22, 35, 40, 49, 55, 60]
threshold = 30

# Generate boolean mask for values exceeding threshold
mask = [x > threshold for x in data_stream]

# Extract values where corresponding mask is True
selected = list(compress(data_stream, mask))

# Apply transformation: square root of even numbers, leave odd as-is
transformed = [int(x**0.5) if x % 2 == 0 else x for x in selected]

# Filter out single-digit results
digit_check = lambda n: n >= 10
filtered_values = [val for val in transformed if digit_check(val)]

filtered_sum = sum(filtered_values)
print(f"Result: {filtered_sum}")