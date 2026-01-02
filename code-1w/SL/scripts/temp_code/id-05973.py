from itertools import compress

# Simulate sensor readings with periodic noise
data_stream = [14, 17, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49]

# Generate pattern mask: True for every even-indexed element (0-based)
index_parity_mask = [(i % 2 == 0) for i in range(len(data_stream))]

# Extract values at even indices using compress
even_indexed_values = list(compress(data_stream, index_parity_mask))

# Apply modular arithmetic to detect cyclic patterns modulo 10
mod_values = [val % 10 for val in even_indexed_values]

# Filter values that are strictly greater than 3
filtered_mod_values = [x for x in mod_values if x > 3]

# Final computation step
result = sum(filtered_mod_values)

print(f"Result: {result}")