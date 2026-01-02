from itertools import compress

data_stream = [12, 15, 22, 35, 40, 47, 55, 64, 73, 80]
threshold = 50

# Generate boolean mask for values above threshold
above_threshold = [x > threshold for x in data_stream]

# Apply mask to select only high-value readings
tagged_data = list(compress(data_stream, above_threshold))

# Perform transformation: square each value and extract digit sum
digit_sums = []
for val in tagged_data:
    squared = val ** 2
    digit_sum = sum(int(d) for d in str(squared))
    digit_sums.append(digit_sum)

# Filter digit sums that are even
even_digit_sums = [s for s in digit_sums if s % 2 == 0]

# Final computation step
filtered_sum = sum(even_digit_sums)

print(f"Result: {filtered_sum}")