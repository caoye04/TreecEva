data_stream = [18, 23, 16, 47, 42, 38, 51, 64, 73, 77, 82, 89, 94, 99, 104]

# Extract slices: every third element starting from index 1
tertiary_slice = data_stream[1::3]

# Get indices where values exceed 50
high_value_indices = {i for i, val in enumerate(data_stream) if val > 50}

# Create set of positions from another slice: last 7 elements
dynamic_range = data_stream[-7:]
span_indices = {data_stream.index(x) for x in dynamic_range}

# Define critical positions as intersection of two index sets
critical_positions = high_value_indices & span_indices

# Generate valid slice positions: indices from tertiary_slice
element_positions = [data_stream.index(x) for x in tertiary_slice]
valid_slices = set(element_positions)

# Key computation step
result = len(valid_slices & critical_positions)

print(f"Result: {result}")