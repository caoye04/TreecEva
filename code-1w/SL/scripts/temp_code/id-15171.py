from itertools import compress

data = [12, -7, 0, 15, 23, -4, 8, 11]
threshold = 10

# Create a boolean mask for values above threshold or even
mask = [(x > threshold) or (x % 2 == 0) for x in data]

# Use compress to filter original data based on mask
filtered_values = list(compress(data, mask))

# Compute the sum of filtered values
filtered_sum = sum(filtered_values)

# Print result as required
print(f"Result: {filtered_sum}")